from __future__ import annotations

from managed_permissions_drift_catalog.diffing import build_dataset_diff
from managed_permissions_drift_catalog.models import DatasetSnapshot
from managed_permissions_drift_catalog.normalize import build_object, build_snapshot


def _snapshot(atoms: list[str], description: str, *, version: str | None = None) -> DatasetSnapshot:
    obj = build_object(
        platform="aws",
        dataset="aws-managed-policies",
        kind="policy",
        stable_id="arn:aws:iam::aws:policy/Test",
        display_name="Test",
        description=description,
        source_url="https://example.test/policy",
        source_version=version,
        source_revision=None,
        fetched_at_utc="2026-04-16T00:00:00Z",
        metadata={"notes": "example"},
        grants_by_facet={"allow_actions": [atom.split(":", 2)[2] for atom in atoms if atom.startswith("aws:allow_action:")]},
        restrictions_by_facet={},
        derived_atoms=atoms,
        raw_hash="hash",
    )
    return build_snapshot(
        dataset="aws-managed-policies",
        platform="aws",
        generated_at_utc="2026-04-16T00:00:00Z",
        source_urls=["https://example.test/policy"],
        warnings=[],
        objects=[obj],
    )


def test_diff_detects_atom_and_metadata_changes() -> None:
    previous = _snapshot(["aws:allow_action:s3:GetObject"], "before", version="v1")
    current = _snapshot(
        ["aws:allow_action:s3:GetObject", "aws:allow_action:s3:PutObject"],
        "after",
        version="v2",
    )
    diff = build_dataset_diff(
        dataset="aws-managed-policies",
        platform="aws",
        current_snapshot=current,
        previous_snapshot=previous,
        previous_snapshot_date="2026-04-15",
        current_snapshot_date="2026-04-16",
        compared_at_utc="2026-04-16T12:00:00Z",
        warnings=[],
    )
    assert diff["counts"]["changed_objects"] == 1
    assert diff["atom_changes"]["added"] == ["aws:allow_action:s3:PutObject"]
    metadata_fields = [item["field"] for item in diff["changed_objects"][0]["metadata_changes"]]
    assert "description" in metadata_fields
    assert "source_version" in metadata_fields

