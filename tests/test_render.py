from __future__ import annotations

from managed_permissions_drift_catalog.render import render_daily_report, render_readme


def test_render_daily_report_is_deterministic() -> None:
    summary = {
        "date": "2026-04-17",
        "generated_at_utc": "2026-04-17T12:00:00Z",
        "winner": "AWS became more privileged today",
        "platforms": [
            {"platform": "aws", "net_score": 1, "added_atoms": 1, "removed_atoms": 0, "datasets": []}
        ],
        "warnings_by_dataset": {},
        "caveats": ["heuristic"],
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
            "warnings": [],
            "changed_objects": [{"stable_id": "x", "display_name": "X", "source_url": "u"}]
        }
    ]
    first = render_daily_report("2026-04-17", summary, diffs)
    second = render_daily_report("2026-04-17", summary, diffs)
    assert first == second


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
        "winner": "AWS became more privileged today",
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
        "warnings_by_dataset": {},
        "caveats": [],
    }
    snapshots = {
        "aws-managed-policies": {
            "dataset": "aws-managed-policies",
            "platform": "aws",
            "generated_at_utc": "2026-04-17T20:31:03Z",
            "object_count": 2,
        },
        "github-token-permissions": {
            "dataset": "github-token-permissions",
            "platform": "github",
            "generated_at_utc": "2026-04-17T20:31:03Z",
            "object_count": 1,
        },
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
            "warnings": [],
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
            "warnings": [],
            "added_objects": [],
            "removed_objects": [],
            "changed_objects": [],
        },
    ]
    readme = render_readme(
        latest_run=latest_run,
        latest_summary=latest_summary,
        snapshots=snapshots,
        latest_diffs=diffs,
    )
    assert "## Latest snapshot" in readme
    assert "## Platform overview" in readme
    assert "## Latest dataset movement" in readme
    assert "Local usage" not in readme
    assert "## Caveats" not in readme
    assert "AWS had the largest net privilege increase" in readme
    assert "Biggest additions: `ReadOnlyAccess` (+10 atoms), `SupportPolicy` (+2 atoms)." in readme
    assert "Baseline note:" in readme
