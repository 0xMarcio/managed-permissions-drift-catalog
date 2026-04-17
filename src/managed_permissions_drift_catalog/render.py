from __future__ import annotations

from pathlib import Path
from typing import Any

from .config import DATASETS


def render_dataset_diff_markdown(diff: dict[str, Any]) -> str:
    lines = [
        f"## {diff['dataset']}",
        "",
        f"- Platform: `{diff['platform']}`",
        f"- Objects: `{diff['counts']['previous_objects']}` -> `{diff['counts']['current_objects']}`",
        f"- Added objects: `{diff['counts']['added_objects']}`",
        f"- Removed objects: `{diff['counts']['removed_objects']}`",
        f"- Changed objects: `{diff['counts']['changed_objects']}`",
        f"- Added atoms: `{diff['counts']['added_atoms']}`",
        f"- Removed atoms: `{diff['counts']['removed_atoms']}`",
    ]
    if diff["warnings"]:
        lines.extend(["", "Warnings:"])
        lines.extend(f"- {warning}" for warning in diff["warnings"])

    if diff["changed_objects"]:
        lines.extend(["", "Changed objects:"])
        for change in diff["changed_objects"][:20]:
            lines.append(f"- `{change['stable_id']}` ({change['display_name']})")
    return "\n".join(lines) + "\n"


def render_daily_report(run_date: str, summary: dict[str, Any], diffs: list[dict[str, Any]]) -> str:
    lines = [
        f"# Daily Drift Report: {run_date}",
        "",
        f"- Generated at: `{summary['generated_at_utc']}`",
        f"- Winner: **{summary['winner']}**",
        "",
        "## Platform scores",
        "",
        "| Platform | Net score | Added atoms | Removed atoms |",
        "| --- | ---: | ---: | ---: |",
    ]
    for platform in summary["platforms"]:
        lines.append(
            f"| `{platform['platform']}` | `{platform['net_score']}` | `{platform['added_atoms']}` | `{platform['removed_atoms']}` |"
        )

    if summary["warnings_by_dataset"]:
        lines.extend(["", "## Source warnings", ""])
        for dataset, warnings in summary["warnings_by_dataset"].items():
            lines.append(f"### {dataset}")
            lines.extend(f"- {warning}" for warning in warnings)
            lines.append("")

    lines.extend(["## Dataset diffs", ""])
    for diff in sorted(diffs, key=lambda item: item["dataset"]):
        lines.append(render_dataset_diff_markdown(diff).rstrip())
        lines.append("")

    lines.extend(["## Caveats", ""])
    lines.extend(f"- {caveat}" for caveat in summary["caveats"])
    return "\n".join(lines).rstrip() + "\n"


def render_platform_page(platform: str, snapshots: dict[str, dict[str, Any]]) -> str:
    lines = [
        f"# {platform.upper()}",
        "",
        "Latest dataset snapshots for this platform.",
        "",
    ]
    relevant = [snapshots[name] for name in DATASETS if name in snapshots and snapshots[name]["platform"] == platform]
    for snapshot in relevant:
        lines.extend(
            [
                f"## {snapshot['dataset']}",
                "",
                f"- Objects: `{snapshot['object_count']}`",
                f"- Latest snapshot: [`data/latest/{snapshot['dataset']}.json`](../../data/latest/{snapshot['dataset']}.json)",
                f"- Reverse index: [`data/reverse-index/{snapshot['dataset']}.json`](../../data/reverse-index/{snapshot['dataset']}.json)",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_docs_index(latest_summary: dict[str, Any] | None, snapshots: dict[str, dict[str, Any]]) -> str:
    lines = [
        "# Managed Permissions Drift Catalog",
        "",
        "Static reports generated from official public documentation and schema surfaces.",
        "",
        "## Datasets",
        "",
        "| Dataset | Platform | Objects | Latest snapshot |",
        "| --- | --- | ---: | --- |",
    ]
    for dataset in DATASETS:
        snapshot = snapshots.get(dataset)
        if not snapshot:
            continue
        lines.append(
            f"| `{dataset}` | `{snapshot['platform']}` | `{snapshot['object_count']}` | [`data/latest/{dataset}.json`](../data/latest/{dataset}.json) |"
        )
    if latest_summary:
        lines.extend(
            [
                "",
                "## Latest daily report",
                "",
                f"- Date: `{latest_summary['date']}`",
                f"- Winner: **{latest_summary['winner']}**",
                f"- Daily report: [`docs/daily/{latest_summary['date']}.md`](daily/{latest_summary['date']}.md)",
                "",
            ]
        )
    lines.extend(
        [
            "## Platform pages",
            "",
            "- [AWS](platforms/aws.md)",
            "- [Azure](platforms/azure.md)",
            "- [GCP](platforms/gcp.md)",
            "- [GitHub](platforms/github.md)",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def render_readme(
    *,
    latest_run: dict[str, Any] | None,
    latest_summary: dict[str, Any] | None,
    snapshots: dict[str, dict[str, Any]],
) -> str:
    last_successful_run = latest_run["finished_at"] if latest_run else "Not run yet"
    lines = [
        "# managed-permissions-drift-catalog",
        "",
        "Tracks documented permission drift in AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.",
        "",
        "## Supported datasets",
        "",
        "- `aws-managed-policies`",
        "- `azure-built-in-roles`",
        "- `gcp-predefined-roles`",
        "- `github-fgpat-permissions`",
        "- `github-token-permissions`",
        "- `github-actions-default-workflow-settings`",
        "",
        f"Last successful run: `{last_successful_run}`",
    ]
    if latest_summary:
        lines.extend(
            [
                f"Latest summary: **{latest_summary['winner']}** on `{latest_summary['date']}`.",
                "",
            ]
        )
    else:
        lines.append("")

    lines.extend(
        [
            "## Local usage",
            "",
            "```bash",
            "python -m pip install -r requirements.txt",
            "python -m pip install -e .",
            "python -m managed_permissions_drift_catalog.cli update",
            "```",
            "",
            "Other commands:",
            "",
            "```bash",
            "python -m managed_permissions_drift_catalog.cli fetch --dataset aws-managed-policies",
            "python -m managed_permissions_drift_catalog.cli normalize --dataset aws-managed-policies",
            "python -m managed_permissions_drift_catalog.cli diff",
            "python -m managed_permissions_drift_catalog.cli render",
            "python -m managed_permissions_drift_catalog.cli query --permission s3:GetObject",
            "python -m managed_permissions_drift_catalog.cli validate",
            "```",
            "",
            "## Reverse-index queries",
            "",
            "Query by concrete permission and the CLI will return exact matches plus wildcard-bearing objects that match the query.",
            "",
            "Examples:",
            "",
            "```bash",
            "python -m managed_permissions_drift_catalog.cli query --permission s3:GetObject",
            "python -m managed_permissions_drift_catalog.cli query --permission Microsoft.Authorization/*/Delete",
            "python -m managed_permissions_drift_catalog.cli query --permission contents:write",
            "```",
            "",
            "## Caveats",
            "",
            "- Privilege scoring is a documented heuristic, not a proof of effective runtime access.",
            "- AWS wildcard actions are not expanded, and conditions/resource scope are only preserved as metadata.",
            "- Source fetch failures leave the existing platform snapshot in place and are reported as stale-source warnings.",
            "",
            "## Repository outputs",
            "",
            "- `data/latest/` stores latest normalized snapshots.",
            "- `data/snapshots/` stores daily gzipped historical snapshots.",
            "- `data/diffs/` stores per-day JSON diffs.",
            "- `data/reverse-index/` stores atom reverse indexes.",
            "- `data/summaries/` stores daily privilege-drift summaries.",
            "- `docs/` stores browseable Markdown reports.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"

