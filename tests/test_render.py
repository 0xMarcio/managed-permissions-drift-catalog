from __future__ import annotations

from managed_permissions_drift_catalog.render import render_daily_report, render_readme


def test_render_daily_report_is_deterministic() -> None:
    summary = {
        "date": "2026-04-17",
        "generated_at_utc": "2026-04-17T12:00:00Z",
        "platforms": [
            {
                "platform": "aws",
                "net_score": 1,
                "added_atoms": 1,
                "removed_atoms": 0,
                "datasets": [
                    {
                        "dataset": "aws-managed-policies",
                        "platform": "aws",
                        "score": 1,
                        "added_atoms": 1,
                        "removed_atoms": 0,
                        "changed_objects": 1,
                    }
                ],
            }
        ],
        "leader": {"platform": "aws", "direction": "increase", "net_score": 1},
    }
    diffs = [
        {
            "dataset": "aws-managed-policies",
            "platform": "aws",
            "counts": {
                "previous_objects": 1,
                "current_objects": 1,
                "added_objects": 0,
                "removed_objects": 0,
                "changed_objects": 1,
                "added_atoms": 1,
                "removed_atoms": 0
            },
            "added_objects": [],
            "removed_objects": [],
            "changed_objects": [{"stable_id": "x", "display_name": "X", "source_url": "u"}]
        }
    ]
    first = render_daily_report("2026-04-17", summary, diffs)
    second = render_daily_report("2026-04-17", summary, diffs)
    assert first == second
    assert "## Caveats" not in first
    assert "## Source warnings" not in first
    assert "## Dataset overview" in first


def test_render_readme_surfaces_latest_movement() -> None:
    latest_run = {
        "finished_at": "2026-04-17T20:32:18Z",
        "per_source": {
            "aws-managed-policies": {"status": "ok"},
            "github-token-permissions": {"status": "ok"},
        },
    }
    latest_summary = {
        "date": "2026-04-17",
        "generated_at_utc": "2026-04-17T20:31:03Z",
        "leader": {"platform": "aws", "direction": "increase", "net_score": 12},
        "platforms": [
            {
                "platform": "aws",
                "net_score": 12,
                "added_atoms": 12,
                "removed_atoms": 0,
                "datasets": [
                    {
                        "dataset": "aws-managed-policies",
                        "platform": "aws",
                        "score": 12,
                        "added_atoms": 12,
                        "removed_atoms": 0,
                        "changed_objects": 0,
                    }
                ],
            },
            {
                "platform": "github",
                "net_score": 0,
                "added_atoms": 0,
                "removed_atoms": 0,
                "datasets": [
                    {
                        "dataset": "github-token-permissions",
                        "platform": "github",
                        "score": 0,
                        "added_atoms": 0,
                        "removed_atoms": 0,
                        "changed_objects": 0,
                    }
                ],
            },
        ],
    }
    diffs = [
        {
            "dataset": "aws-managed-policies",
            "platform": "aws",
            "counts": {
                "previous_objects": 0,
                "current_objects": 2,
                "added_objects": 2,
                "removed_objects": 0,
                "changed_objects": 0,
                "added_atoms": 12,
                "removed_atoms": 0,
            },
            "added_objects": [
                {
                    "stable_id": "a",
                    "display_name": "ReadOnlyAccess",
                    "source_url": "u",
                    "atoms_added": ["x"] * 10,
                },
                {
                    "stable_id": "b",
                    "display_name": "SupportPolicy",
                    "source_url": "u",
                    "atoms_added": ["x"] * 2,
                },
            ],
            "removed_objects": [],
            "changed_objects": [],
        },
        {
            "dataset": "github-token-permissions",
            "platform": "github",
            "counts": {
                "previous_objects": 1,
                "current_objects": 1,
                "added_objects": 0,
                "removed_objects": 0,
                "changed_objects": 0,
                "added_atoms": 0,
                "removed_atoms": 0,
            },
            "added_objects": [],
            "removed_objects": [],
            "changed_objects": [],
        },
    ]
    readme = render_readme(
        latest_run=latest_run,
        latest_summary=latest_summary,
        latest_diffs=diffs,
    )
    assert "## Latest drift" in readme
    assert "## Platform overview" in readme
    assert "## Latest dataset movement" in readme
    assert "Local usage" not in readme
    assert "## Caveats" not in readme
    assert "## Latest snapshot" not in readme
    assert "Source refresh:" not in readme
    assert "Baseline note:" not in readme
    assert "Report date:" not in readme
    assert "Updated at:" not in readme
    assert "Refreshed at:" in readme
    assert "## Browse outputs" not in readme
    assert "Leading platform: `AWS` (`+12` net score)" in readme
    assert "Driver: `AWS managed policies` (+2 objects, +12 atoms)" in readme
    assert "## Dataset overview" in readme
    assert "- Inventory: `2` objects." in readme
    assert "Biggest additions: `ReadOnlyAccess` (+10 atoms), `SupportPolicy` (+2 atoms)." in readme
