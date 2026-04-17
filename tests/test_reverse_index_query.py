from __future__ import annotations

from pathlib import Path

from managed_permissions_drift_catalog.cli import query_permission
from managed_permissions_drift_catalog.diffing import build_reverse_index
from managed_permissions_drift_catalog.normalize import build_object, build_snapshot
from managed_permissions_drift_catalog.storage import Storage

from .conftest import ensure_repo_layout


def test_query_matches_exact_and_wildcard_atoms(tmp_path: Path) -> None:
    root = ensure_repo_layout(tmp_path)
    storage = Storage(root)
    snapshot = build_snapshot(
        dataset="aws-managed-policies",
        platform="aws",
        generated_at_utc="2026-04-17T00:00:00Z",
        source_urls=["https://example.test/policy"],
        warnings=[],
        objects=[
            build_object(
                platform="aws",
                dataset="aws-managed-policies",
                kind="policy",
                stable_id="policy-1",
                display_name="Exact",
                description="",
                source_url="https://example.test/exact",
                source_version=None,
                source_revision=None,
                fetched_at_utc="2026-04-17T00:00:00Z",
                metadata={},
                grants_by_facet={"allow_actions": ["s3:GetObject"]},
                restrictions_by_facet={},
                derived_atoms=["aws:allow_action:s3:GetObject"],
                raw_hash="a",
            ),
            build_object(
                platform="aws",
                dataset="aws-managed-policies",
                kind="policy",
                stable_id="policy-2",
                display_name="Wildcard",
                description="",
                source_url="https://example.test/wildcard",
                source_version=None,
                source_revision=None,
                fetched_at_utc="2026-04-17T00:00:00Z",
                metadata={},
                grants_by_facet={"allow_actions": ["s3:Get*"]},
                restrictions_by_facet={},
                derived_atoms=["aws:allow_action:s3:Get*"],
                raw_hash="b",
            ),
        ],
    )
    storage.write_json_if_changed(storage.latest_snapshot_path("aws-managed-policies"), snapshot.to_dict())
    storage.write_json_if_changed(storage.reverse_index_path("aws-managed-policies"), build_reverse_index(snapshot))
    results = query_permission(storage, "s3:GetObject")
    atoms = {item["atom"] for item in results}
    assert "aws:allow_action:s3:GetObject" in atoms
    assert "aws:allow_action:s3:Get*" in atoms


def test_query_does_not_match_universal_wildcards_cross_platform(tmp_path: Path) -> None:
    root = ensure_repo_layout(tmp_path)
    storage = Storage(root)
    aws_snapshot = build_snapshot(
        dataset="aws-managed-policies",
        platform="aws",
        generated_at_utc="2026-04-17T00:00:00Z",
        source_urls=["https://example.test/policy"],
        warnings=[],
        objects=[
            build_object(
                platform="aws",
                dataset="aws-managed-policies",
                kind="policy",
                stable_id="policy-star",
                display_name="Star",
                description="",
                source_url="https://example.test/star",
                source_version=None,
                source_revision=None,
                fetched_at_utc="2026-04-17T00:00:00Z",
                metadata={},
                grants_by_facet={"allow_actions": ["*"]},
                restrictions_by_facet={},
                derived_atoms=["aws:allow_action:*"],
                raw_hash="x",
            )
        ],
    )
    github_snapshot = build_snapshot(
        dataset="github-token-permissions",
        platform="github",
        generated_at_utc="2026-04-17T00:00:00Z",
        source_urls=["https://example.test/token"],
        warnings=[],
        objects=[
            build_object(
                platform="github",
                dataset="github-token-permissions",
                kind="permission_schema",
                stable_id="github-token:contents",
                display_name="contents",
                description="",
                source_url="https://example.test/contents",
                source_version=None,
                source_revision=None,
                fetched_at_utc="2026-04-17T00:00:00Z",
                metadata={"allowed_values": ["none", "read", "write"]},
                grants_by_facet={"levels": ["read", "write"]},
                restrictions_by_facet={},
                derived_atoms=["github:token:contents:read", "github:token:contents:write"],
                raw_hash="y",
            )
        ],
    )
    storage.write_json_if_changed(storage.latest_snapshot_path("aws-managed-policies"), aws_snapshot.to_dict())
    storage.write_json_if_changed(storage.reverse_index_path("aws-managed-policies"), build_reverse_index(aws_snapshot))
    storage.write_json_if_changed(storage.latest_snapshot_path("github-token-permissions"), github_snapshot.to_dict())
    storage.write_json_if_changed(
        storage.reverse_index_path("github-token-permissions"),
        build_reverse_index(github_snapshot),
    )
    results = query_permission(storage, "contents:write")
    atoms = {item["atom"] for item in results}
    assert "github:token:contents:write" in atoms
    assert "aws:allow_action:*" not in atoms
