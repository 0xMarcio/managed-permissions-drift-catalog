from __future__ import annotations

from managed_permissions_drift_catalog.render import render_daily_report


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

