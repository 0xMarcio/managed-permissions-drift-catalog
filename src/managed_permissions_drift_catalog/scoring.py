from __future__ import annotations

from collections import defaultdict
from typing import Any


def _github_level_weight(atom: str) -> int:
    if atom.endswith(":admin"):
        return 3
    if atom.endswith(":write"):
        return 2
    if atom.endswith(":read"):
        return 1
    if atom.endswith(":true"):
        return 1
    return 0


def score_atom_change(atom: str, *, added: bool) -> int:
    direction = 1 if added else -1
    if atom.startswith("aws:allow_action:"):
        return direction
    if atom.startswith(("aws:allow_notaction:", "aws:deny_action:", "aws:deny_notaction:")):
        return -direction

    if atom.startswith(("azure:action:", "azure:data_action:")):
        return direction
    if atom.startswith(("azure:not_action:", "azure:not_data_action:")):
        return -direction

    if atom.startswith("gcp:permission:"):
        return direction

    if atom.startswith(("github:fgpat:", "github:token:")):
        return direction * _github_level_weight(atom)

    if atom.startswith("github:workflow-default:default_workflow_permissions:"):
        return direction * _github_level_weight(atom)
    if atom.startswith("github:workflow-default:can_approve_pull_request_reviews:"):
        return direction * _github_level_weight(atom)
    if atom.startswith("github:org-actions-policy:allowed_actions:all"):
        return direction * 2
    if atom.startswith("github:org-actions-policy:allowed_actions:selected"):
        return direction
    if atom.startswith("github:org-actions-policy:allowed_actions:local_only"):
        return 0
    if atom.startswith("github:org-actions-policy:enabled:true"):
        return direction
    if atom.startswith("github:org-actions-policy:enabled:false"):
        return 0
    if atom.startswith("github:org-actions-policy:sha_pinning_required:true"):
        return -direction
    if atom.startswith("github:org-actions-policy:sha_pinning_required:false"):
        return 0
    if atom.startswith("github:repo-actions-policy:allowed_actions:all"):
        return direction * 2
    if atom.startswith("github:repo-actions-policy:allowed_actions:selected"):
        return direction
    if atom.startswith("github:repo-actions-policy:allowed_actions:local_only"):
        return 0
    if atom.startswith("github:repo-actions-policy:enabled:true"):
        return direction
    if atom.startswith("github:repo-actions-policy:enabled:false"):
        return 0
    if atom.startswith("github:repo-actions-policy:sha_pinning_required:true"):
        return -direction
    if atom.startswith("github:repo-actions-policy:sha_pinning_required:false"):
        return 0
    return 0


def score_dataset_diff(diff: dict[str, Any]) -> dict[str, Any]:
    added = diff["atom_changes"]["added"]
    removed = diff["atom_changes"]["removed"]
    score = sum(score_atom_change(atom, added=True) for atom in added)
    score += sum(score_atom_change(atom, added=False) for atom in removed)
    return {
        "dataset": diff["dataset"],
        "platform": diff["platform"],
        "score": score,
        "added_atoms": len(added),
        "removed_atoms": len(removed),
        "changed_objects": diff["counts"]["changed_objects"],
    }


def summarize_daily_scores(
    *,
    run_date: str,
    compared_at_utc: str,
    diffs: list[dict[str, Any]],
    warnings_by_dataset: dict[str, list[str]],
) -> dict[str, Any]:
    dataset_scores = [score_dataset_diff(diff) for diff in diffs]
    platform_totals: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"net_score": 0, "added_atoms": 0, "removed_atoms": 0, "datasets": []}
    )
    for item in dataset_scores:
        platform_entry = platform_totals[item["platform"]]
        platform_entry["net_score"] += item["score"]
        platform_entry["added_atoms"] += item["added_atoms"]
        platform_entry["removed_atoms"] += item["removed_atoms"]
        platform_entry["datasets"].append(item)

    ordered_platforms = [
        {
            "platform": platform,
            "net_score": values["net_score"],
            "added_atoms": values["added_atoms"],
            "removed_atoms": values["removed_atoms"],
            "datasets": sorted(values["datasets"], key=lambda item: item["dataset"]),
        }
        for platform, values in sorted(platform_totals.items())
    ]
    winner = "No platform became more privileged today"
    if ordered_platforms:
        top = max(ordered_platforms, key=lambda item: item["net_score"])
        if top["net_score"] > 0:
            winner = f"{top['platform'].upper()} became more privileged today"
        elif top["net_score"] < 0:
            winner = f"{top['platform'].upper()} became less privileged today"

    caveats = [
        "This score is a heuristic. It tracks documented permission-shape drift, not full effective access.",
        "AWS scoring does not evaluate conditions, resources, principals, or wildcard expansion.",
        "Azure and GCP scoring compare listed actions and permissions without tenant-specific scope evaluation.",
        "GitHub scores schema-level changes in documented permission levels and settings contracts, not your live organization settings.",
    ]
    return {
        "date": run_date,
        "generated_at_utc": compared_at_utc,
        "winner": winner,
        "platforms": ordered_platforms,
        "datasets": sorted(dataset_scores, key=lambda item: item["dataset"]),
        "warnings_by_dataset": {key: value for key, value in sorted(warnings_by_dataset.items()) if value},
        "caveats": caveats,
    }
