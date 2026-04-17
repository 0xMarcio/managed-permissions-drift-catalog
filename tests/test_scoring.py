from __future__ import annotations

from managed_permissions_drift_catalog.scoring import score_dataset_diff, summarize_daily_scores


def test_score_dataset_diff_for_aws() -> None:
    diff = {
        "dataset": "aws-managed-policies",
        "platform": "aws",
        "atom_changes": {
            "added": ["aws:allow_action:s3:GetObject"],
            "removed": ["aws:deny_action:organizations:LeaveOrganization"],
        },
        "counts": {"changed_objects": 1},
    }
    scored = score_dataset_diff(diff)
    assert scored["score"] == 2


def test_summarize_daily_scores_picks_winner() -> None:
    diffs = [
        {
            "dataset": "aws-managed-policies",
            "platform": "aws",
            "atom_changes": {"added": ["aws:allow_action:s3:GetObject"], "removed": []},
            "counts": {"changed_objects": 1},
        },
        {
            "dataset": "github-token-permissions",
            "platform": "github",
            "atom_changes": {"added": [], "removed": ["github:token:contents:write"]},
            "counts": {"changed_objects": 1},
        },
    ]
    summary = summarize_daily_scores(
        run_date="2026-04-17",
        compared_at_utc="2026-04-17T12:00:00Z",
        diffs=diffs,
        warnings_by_dataset={},
    )
    assert summary["winner"] == "AWS became more privileged today"

