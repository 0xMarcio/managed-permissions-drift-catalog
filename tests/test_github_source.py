from __future__ import annotations

import shutil
from pathlib import Path

from managed_permissions_drift_catalog.config import (
    GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS,
    GITHUB_FGPAT_PERMISSIONS,
    GITHUB_TOKEN_PERMISSIONS,
    Settings,
)
from managed_permissions_drift_catalog.sources import github
from managed_permissions_drift_catalog.storage import Storage

from .conftest import ensure_repo_layout


FIXTURES = Path(__file__).parent / "fixtures" / "github"


def _write_fixture(root: Path, dataset: str, fixture_name: str) -> None:
    storage = Storage(root)
    raw_dir = storage.raw_dir(dataset)
    raw_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(FIXTURES / fixture_name, raw_dir / "next-data.json")


def test_normalize_fgpat_snapshot(tmp_path: Path) -> None:
    root = ensure_repo_layout(tmp_path)
    _write_fixture(root, GITHUB_FGPAT_PERMISSIONS, "fgpat-next-data.json")
    storage = Storage(root)
    settings = Settings.from_root(root)
    snapshot = github.normalize_fgpat(settings, storage, "2026-04-17T00:00:00Z")
    assert len(snapshot.objects) == 1
    obj = snapshot.objects[0]
    assert obj.stable_id == "github-fgpat:repository:contents"
    assert "github:fgpat:repository:contents:read" in obj.derived_atoms
    assert any("GET /repos/{owner}/{repo}/contents/{path} -> read" == item for item in obj.grants_by_facet["endpoints"])


def test_normalize_token_permissions_snapshot(tmp_path: Path) -> None:
    root = ensure_repo_layout(tmp_path)
    _write_fixture(root, GITHUB_TOKEN_PERMISSIONS, "workflow-next-data.json")
    storage = Storage(root)
    settings = Settings.from_root(root)
    snapshot = github.normalize_token_permissions(settings, storage, "2026-04-17T00:00:00Z")
    assert len(snapshot.objects) == 3
    actions = next(item for item in snapshot.objects if item.stable_id == "github-token:actions")
    assert actions.metadata["allowed_values"] == ["none", "read", "write"]
    assert "github:token:actions:write" in actions.derived_atoms


def test_normalize_actions_settings_snapshot(tmp_path: Path) -> None:
    root = ensure_repo_layout(tmp_path)
    _write_fixture(root, GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS, "actions-next-data.json")
    storage = Storage(root)
    settings = Settings.from_root(root)
    snapshot = github.normalize_actions_settings(settings, storage, "2026-04-17T00:00:00Z")
    assert len(snapshot.objects) == 2
    workflow = next(item for item in snapshot.objects if "workflow" in item.stable_id)
    assert "github:workflow-default:default_workflow_permissions:write" in workflow.derived_atoms
    repo_policy = next(item for item in snapshot.objects if item.stable_id == "github-actions-settings:repo-actions-policy")
    assert "github:repo-actions-policy:allowed_actions:selected" in repo_policy.derived_atoms
