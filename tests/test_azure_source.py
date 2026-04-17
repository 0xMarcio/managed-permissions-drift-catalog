from __future__ import annotations

from pathlib import Path

from managed_permissions_drift_catalog.config import AZURE_BUILT_IN_ROLES, Settings
from managed_permissions_drift_catalog.sources import azure
from managed_permissions_drift_catalog.storage import Storage

from .conftest import ensure_repo_layout


FIXTURES = Path(__file__).parent / "fixtures" / "azure"


def test_parse_azure_landing_categories() -> None:
    html = (FIXTURES / "landing.html").read_text(encoding="utf-8")
    parsed = azure.parse_landing_categories(html)
    assert parsed == ["https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged"]


def test_parse_azure_category_page() -> None:
    html = (FIXTURES / "privileged.html").read_text(encoding="utf-8")
    parsed = azure.parse_category_page(
        html,
        "https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged",
    )
    assert parsed[0]["role_definition"]["roleName"] == "Contributor"
    assert parsed[0]["role_definition"]["permissions"][0]["notActions"] == ["Microsoft.Authorization/*/Delete"]


def test_normalize_azure_snapshot(tmp_path: Path) -> None:
    root = ensure_repo_layout(tmp_path)
    storage = Storage(root)
    raw_dir = storage.raw_dir(AZURE_BUILT_IN_ROLES)
    (raw_dir / "categories").mkdir(parents=True, exist_ok=True)
    (raw_dir / "landing.html").write_text((FIXTURES / "landing.html").read_text(encoding="utf-8"), encoding="utf-8")
    (raw_dir / "categories" / "privileged.html").write_text(
        (FIXTURES / "privileged.html").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    settings = Settings.from_root(root)
    snapshot = azure.normalize(settings, storage, "2026-04-17T00:00:00Z")
    assert len(snapshot.objects) == 1
    obj = snapshot.objects[0]
    assert obj.stable_id == "b24988ac-6180-42a0-ab88-20f7382dd24c"
    assert "azure:action:*" in obj.derived_atoms
    assert "azure:not_action:Microsoft.Authorization/*/Delete" in obj.derived_atoms

