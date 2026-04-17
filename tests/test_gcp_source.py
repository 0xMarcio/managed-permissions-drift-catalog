from __future__ import annotations

import json
from pathlib import Path

from managed_permissions_drift_catalog.config import GCP_PREDEFINED_ROLES, Settings
from managed_permissions_drift_catalog.sources import gcp
from managed_permissions_drift_catalog.storage import Storage

from .conftest import ensure_repo_layout


FIXTURES = Path(__file__).parent / "fixtures" / "gcp"


def test_parse_gcp_filter_index() -> None:
    payload = json.loads((FIXTURES / "role-permission-filter.json").read_text(encoding="utf-8"))
    parsed = gcp.parse_filter_index(payload)
    assert parsed["roles"][0]["name"] == "roles/accessapproval.admin"


def test_parse_gcp_service_page() -> None:
    html = (FIXTURES / "accessapproval.html").read_text(encoding="utf-8")
    parsed = gcp.parse_service_page(html, "https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval")
    assert parsed[0]["name"] == "roles/accessapproval.admin"
    assert parsed[0]["includedPermissions"] == [
        "accessapproval.requests.approve",
        "accessapproval.requests.dismiss",
        "resourcemanager.projects.get",
    ]


def test_parse_gcp_service_page_with_empty_permissions() -> None:
    html = """
    <table class="fixed">
      <tbody class="list">
        <tr>
          <td class="role-description">
            <h4 class="role-title add-link" id="example.empty" tabindex="-1">Example Empty Role <sup class="launch-stage-pre-ga">Beta</sup></h4>
            <p class="iamperm-marginless">(<code translate="no" dir="ltr">roles/example.empty</code>)</p>
            <span class="role-description"><p>No listed permissions.</p></span>
          </td>
          <td class="role-permissions"></td>
        </tr>
      </tbody>
    </table>
    """
    parsed = gcp.parse_service_page(html, "https://docs.cloud.google.com/iam/docs/roles-permissions/example")
    assert parsed == [
        {
            "name": "roles/example.empty",
            "role_id": "example.empty",
            "title": "Example Empty Role Beta",
            "description": "No listed permissions.",
            "stage": "Beta",
            "includedPermissions": [],
            "deleted": False,
            "source_url": "https://docs.cloud.google.com/iam/docs/roles-permissions/example#example.empty",
            "stage_inferred": False,
        }
    ]


def test_normalize_gcp_snapshot(tmp_path: Path) -> None:
    root = ensure_repo_layout(tmp_path)
    storage = Storage(root)
    raw_dir = storage.raw_dir(GCP_PREDEFINED_ROLES)
    (raw_dir / "services").mkdir(parents=True, exist_ok=True)
    (raw_dir / "role-permission-filter.json").write_text(
        (FIXTURES / "role-permission-filter.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (raw_dir / "service-urls.json").write_text(
        json.dumps(["https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval"]),
        encoding="utf-8",
    )
    (raw_dir / "services" / "accessapproval.html").write_text(
        (FIXTURES / "accessapproval.html").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    settings = Settings.from_root(root)
    snapshot = gcp.normalize(settings, storage, "2026-04-17T00:00:00Z")
    assert len(snapshot.objects) == 1
    obj = snapshot.objects[0]
    assert obj.stable_id == "roles/accessapproval.admin"
    assert obj.metadata["stage"] == "GA"
    assert "gcp:permission:accessapproval.requests.approve" in obj.derived_atoms
