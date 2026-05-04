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
    assert "Leading platform:" not in readme
    assert "## Dataset overview" in readme
    assert "- Inventory: `2` objects." in readme
    assert "Biggest additions: `ReadOnlyAccess` (+10 atoms), `SupportPolicy` (+2 atoms)." in readme


def test_render_readme_uses_weekly_activity_when_recent_diffs_are_available() -> None:
    def diff(
        *,
        dataset: str,
        platform: str,
        run_date: str,
        previous_date: str | None,
        current_objects: int,
        added_objects: int = 0,
        changed_objects: int = 0,
        removed_objects: int = 0,
        added_atoms: list[str] | None = None,
        removed_atoms: list[str] | None = None,
    ) -> dict:
        added_atoms = added_atoms or []
        removed_atoms = removed_atoms or []
        return {
            "dataset": dataset,
            "platform": platform,
            "previous_snapshot_date": previous_date,
            "current_snapshot_date": run_date,
            "counts": {
                "previous_objects": current_objects - added_objects + removed_objects,
                "current_objects": current_objects,
                "added_objects": added_objects,
                "removed_objects": removed_objects,
                "changed_objects": changed_objects,
                "added_atoms": len(added_atoms),
                "removed_atoms": len(removed_atoms),
            },
            "atom_changes": {"added": added_atoms, "removed": removed_atoms},
            "added_objects": [
                {"stable_id": "added", "display_name": "Added item", "source_url": "u", "atoms_added": added_atoms}
            ][:added_objects],
            "removed_objects": [],
            "changed_objects": [
                {
                    "stable_id": "changed",
                    "display_name": "Changed item",
                    "source_url": "u",
                    "facet_changes": {"grants": {"permissions": {"added": added_atoms, "removed": removed_atoms}}},
                }
            ][:changed_objects],
        }

    latest_run = {"finished_at": "2026-05-04T04:35:48Z"}
    latest_summary = {
        "date": "2026-05-04",
        "generated_at_utc": "2026-05-04T04:35:48Z",
        "leader": None,
        "platforms": [
            {"platform": "aws", "net_score": 0, "added_atoms": 0, "removed_atoms": 0, "datasets": []},
            {"platform": "azure", "net_score": 0, "added_atoms": 0, "removed_atoms": 0, "datasets": []},
            {"platform": "gcp", "net_score": 0, "added_atoms": 0, "removed_atoms": 0, "datasets": []},
            {"platform": "github", "net_score": 0, "added_atoms": 0, "removed_atoms": 0, "datasets": []},
        ],
    }
    latest_diffs = [
        diff(
            dataset="aws-managed-policies",
            platform="aws",
            run_date="2026-05-04",
            previous_date="2026-05-03",
            current_objects=10,
        ),
        diff(
            dataset="azure-built-in-roles",
            platform="azure",
            run_date="2026-05-04",
            previous_date="2026-04-17",
            current_objects=3,
        ),
        diff(
            dataset="gcp-predefined-roles",
            platform="gcp",
            run_date="2026-05-04",
            previous_date="2026-04-21",
            current_objects=4,
        ),
        diff(
            dataset="github-fgpat-permissions",
            platform="github",
            run_date="2026-05-04",
            previous_date="2026-05-02",
            current_objects=2,
        ),
    ]
    recent_diffs = [
        *latest_diffs,
        diff(
            dataset="aws-managed-policies",
            platform="aws",
            run_date="2026-05-03",
            previous_date="2026-05-02",
            current_objects=10,
            changed_objects=1,
            added_atoms=["aws:allow_action:one", "aws:allow_action:two"],
        ),
        diff(
            dataset="github-fgpat-permissions",
            platform="github",
            run_date="2026-05-02",
            previous_date="2026-05-01",
            current_objects=2,
            added_objects=1,
            added_atoms=["github:fgpat:contents:read"],
        ),
        diff(
            dataset="gcp-predefined-roles",
            platform="gcp",
            run_date="2026-04-21",
            previous_date="2026-04-17",
            current_objects=4,
            changed_objects=1,
            added_atoms=["gcp:permission:one"],
        ),
        diff(
            dataset="azure-built-in-roles",
            platform="azure",
            run_date="2026-04-17",
            previous_date=None,
            current_objects=3,
            added_objects=3,
            added_atoms=["azure:action:one", "azure:action:two", "azure:action:three"],
        ),
    ]

    readme = render_readme(
        latest_run=latest_run,
        latest_summary=latest_summary,
        latest_diffs=latest_diffs,
        recent_diffs=recent_diffs,
    )

    assert "| Platform | Last 7 days | Last 30 days | Main recent driver |" in readme
    assert "| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |" in readme
    assert "Today: No drift detected." not in readme
    assert "+0 / ~0 / -0" not in readme
    assert "Recent windows:" not in readme
    assert "AWS managed policies (7d, last changed [2026-05-03]" in readme
    assert "GCP predefined roles (30d, last changed [2026-04-21]" in readme
    assert "| Azure built-in roles | `3` | No movement | No movement | No movement |" in readme
    assert "- Last 7 days: `+2` net · `~1` object · `+2` atoms · 1 active day." in readme
    assert "2026-05-03: ~1 changed, +2 atoms (`Changed item` (+2))" in readme
