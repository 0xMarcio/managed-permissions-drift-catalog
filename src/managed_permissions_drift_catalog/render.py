from __future__ import annotations

from collections import defaultdict
from typing import Any

from .config import DATASETS

DATASET_LABELS = {
    "aws-managed-policies": "AWS managed policies",
    "azure-built-in-roles": "Azure built-in roles",
    "gcp-predefined-roles": "GCP predefined roles",
    "github-fgpat-permissions": "GitHub fine-grained PAT permissions",
    "github-token-permissions": "GitHub GITHUB_TOKEN permissions",
    "github-actions-default-workflow-settings": "GitHub Actions default workflow settings",
}
PLATFORM_LABELS = {
    "aws": "AWS",
    "azure": "Azure",
    "gcp": "GCP",
    "github": "GitHub",
}


def _format_int(value: int) -> str:
    return f"{value:,}"


def _format_delta(value: int) -> str:
    if value > 0:
        return f"+{value:,}"
    return f"{value:,}"


def _dataset_label(dataset: str) -> str:
    return DATASET_LABELS.get(dataset, dataset)


def _platform_label(platform: str) -> str:
    return PLATFORM_LABELS.get(platform, platform.upper())


def _pick_winner_platform(platforms: list[dict[str, Any]]) -> tuple[dict[str, Any] | None, str]:
    positives = [item for item in platforms if item["net_score"] > 0]
    if positives:
        return sorted(positives, key=lambda item: (-item["net_score"], item["platform"]))[0], "increase"
    negatives = [item for item in platforms if item["net_score"] < 0]
    if negatives:
        return sorted(negatives, key=lambda item: (item["net_score"], item["platform"]))[0], "decrease"
    return None, "none"


def _platform_rollups(diffs: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    rollups: dict[str, dict[str, int]] = defaultdict(
        lambda: {"added_objects": 0, "changed_objects": 0, "removed_objects": 0}
    )
    for diff in diffs:
        counts = diff["counts"]
        rollup = rollups[diff["platform"]]
        rollup["added_objects"] += counts["added_objects"]
        rollup["changed_objects"] += counts["changed_objects"]
        rollup["removed_objects"] += counts["removed_objects"]
    return dict(rollups)


def _driver_dataset(platform_entry: dict[str, Any]) -> dict[str, Any] | None:
    datasets = platform_entry.get("datasets", [])
    if not datasets:
        return None
    return sorted(
        datasets,
        key=lambda item: (
            -abs(item["score"]),
            -(item["added_atoms"] + item["removed_atoms"]),
            -item["changed_objects"],
            item["dataset"],
        ),
    )[0]


def _driver_text(platform_entry: dict[str, Any], diff_by_dataset: dict[str, dict[str, Any]]) -> str:
    driver = _driver_dataset(platform_entry)
    if not driver:
        return "No dataset drift"
    diff = diff_by_dataset.get(driver["dataset"])
    if not diff:
        return f"{_dataset_label(driver['dataset'])} ({_format_delta(driver['score'])})"
    return f"{_dataset_label(driver['dataset'])} ({_short_change_summary(diff)})"


def _leader_lines(summary: dict[str, Any] | None, diffs: list[dict[str, Any]]) -> list[str]:
    if not summary:
        return []
    winner_platform, _direction = _pick_winner_platform(summary.get("platforms", []))
    if winner_platform is None:
        return ["- Leading platform: none"]
    driver = _driver_dataset(winner_platform)
    lines = [f"- Leading platform: `{_platform_label(winner_platform['platform'])}` (`{_format_delta(winner_platform['net_score'])}` net score)"]
    if driver:
        diff_by_dataset = {item["dataset"]: item for item in diffs}
        driver_diff = diff_by_dataset.get(driver["dataset"])
        if driver_diff:
            lines.append(f"- Driver: `{_dataset_label(driver['dataset'])}` ({_short_change_summary(driver_diff)})")
    return lines


def _short_change_summary(diff: dict[str, Any]) -> str:
    counts = diff["counts"]
    object_parts = []
    if counts["added_objects"]:
        object_parts.append(f"+{_format_int(counts['added_objects'])} objects")
    if counts["changed_objects"]:
        object_parts.append(f"~{_format_int(counts['changed_objects'])} changed")
    if counts["removed_objects"]:
        object_parts.append(f"-{_format_int(counts['removed_objects'])} removed")

    atom_parts = []
    if counts["added_atoms"]:
        atom_parts.append(f"+{_format_int(counts['added_atoms'])} atoms")
    if counts["removed_atoms"]:
        atom_parts.append(f"-{_format_int(counts['removed_atoms'])} atoms")

    parts = object_parts + atom_parts
    if not parts:
        return "no drift"
    return ", ".join(parts)


def _dataset_table_rows(diffs: list[dict[str, Any]]) -> list[str]:
    rows: list[str] = []
    for diff in sorted(diffs, key=lambda item: item["dataset"]):
        counts = diff["counts"]
        rows.append(
            f"| {_dataset_label(diff['dataset'])} | {_platform_label(diff['platform'])} | "
            f"`{_format_int(counts['current_objects'])}` | "
            f"`+{_format_int(counts['added_objects'])} / ~{_format_int(counts['changed_objects'])} / -{_format_int(counts['removed_objects'])}` | "
            f"`+{_format_int(counts['added_atoms'])} / -{_format_int(counts['removed_atoms'])}` | "
            f"[snapshot](../data/latest/{diff['dataset']}.json) |"
        )
    return rows


def _dataset_table_rows_for_readme(diffs: list[dict[str, Any]], run_date: str) -> list[str]:
    rows: list[str] = []
    for diff in sorted(diffs, key=lambda item: item["dataset"]):
        counts = diff["counts"]
        rows.append(
            f"| {_dataset_label(diff['dataset'])} | `{_format_int(counts['current_objects'])}` | "
            f"`+{_format_int(counts['added_objects'])} / ~{_format_int(counts['changed_objects'])} / -{_format_int(counts['removed_objects'])}` | "
            f"`+{_format_int(counts['added_atoms'])} / -{_format_int(counts['removed_atoms'])}` | "
            f"[snapshot](data/latest/{diff['dataset']}.json) · [diff](data/diffs/{run_date}/{diff['dataset']}.json) · [reverse index](data/reverse-index/{diff['dataset']}.json) |"
        )
    return rows


def _top_added_objects(diff: dict[str, Any], limit: int = 3) -> list[str]:
    objects = sorted(
        diff["added_objects"],
        key=lambda item: (-len(item.get("atoms_added", [])), item["display_name"], item["stable_id"]),
    )[:limit]
    formatted = []
    for item in objects:
        atom_count = len(item.get("atoms_added", []))
        if atom_count:
            formatted.append(f"`{item['display_name']}` (+{_format_int(atom_count)} atoms)")
        else:
            formatted.append(f"`{item['display_name']}`")
    return formatted


def _top_removed_objects(diff: dict[str, Any], limit: int = 3) -> list[str]:
    objects = sorted(
        diff["removed_objects"],
        key=lambda item: (-len(item.get("atoms_removed", [])), item["display_name"], item["stable_id"]),
    )[:limit]
    formatted = []
    for item in objects:
        atom_count = len(item.get("atoms_removed", []))
        if atom_count:
            formatted.append(f"`{item['display_name']}` (-{_format_int(atom_count)} atoms)")
        else:
            formatted.append(f"`{item['display_name']}`")
    return formatted


def _changed_object_magnitude(change: dict[str, Any]) -> tuple[int, int]:
    added = 0
    removed = 0
    facet_changes = change.get("facet_changes", {})
    for section in ("grants", "restrictions"):
        for delta in facet_changes.get(section, {}).values():
            added += len(delta.get("added", []))
            removed += len(delta.get("removed", []))
    return added, removed


def _top_changed_objects(diff: dict[str, Any], limit: int = 3) -> list[str]:
    objects = sorted(
        diff["changed_objects"],
        key=lambda item: (
            -sum(_changed_object_magnitude(item)),
            item["display_name"],
            item["stable_id"],
        ),
    )[:limit]
    formatted = []
    for item in objects:
        added, removed = _changed_object_magnitude(item)
        parts = []
        if added:
            parts.append(f"+{_format_int(added)}")
        if removed:
            parts.append(f"-{_format_int(removed)}")
        if not parts and item.get("metadata_changes"):
            parts.append("metadata only")
        detail = ", ".join(parts) if parts else "changed"
        formatted.append(f"`{item['display_name']}` ({detail})")
    return formatted


def _dataset_today_line(diff: dict[str, Any]) -> str:
    summary = _short_change_summary(diff)
    if summary == "no drift":
        return "No drift detected."
    if "atoms" not in summary:
        return f"{summary}; no atom-level change."
    return f"{summary}."


def _dataset_movement_lines(diff: dict[str, Any], run_date: str, data_prefix: str = "data") -> list[str]:
    counts = diff["counts"]
    lines = [
        f"### {_dataset_label(diff['dataset'])}",
        "",
        f"- Inventory: `{_format_int(counts['current_objects'])}` objects.",
        f"- Today: {_dataset_today_line(diff)}",
    ]
    added = _top_added_objects(diff)
    if added:
        lines.append(f"- Biggest additions: {', '.join(added)}.")
    changed = _top_changed_objects(diff)
    if changed:
        lines.append(f"- Biggest changes: {', '.join(changed)}.")
    removed = _top_removed_objects(diff)
    if removed:
        lines.append(f"- Biggest removals: {', '.join(removed)}.")
    lines.append(
        "- Files: "
        f"[snapshot]({data_prefix}/latest/{diff['dataset']}.json) · "
        f"[diff]({data_prefix}/diffs/{run_date}/{diff['dataset']}.json) · "
        f"[reverse index]({data_prefix}/reverse-index/{diff['dataset']}.json)"
    )
    lines.append("")
    return lines


def render_dataset_diff_markdown(diff: dict[str, Any], run_date: str, data_prefix: str = "data") -> str:
    counts = diff["counts"]
    lines = [
        f"## {_dataset_label(diff['dataset'])}",
        "",
        f"- Inventory: `{_format_int(counts['current_objects'])}` objects.",
        f"- Today: {_dataset_today_line(diff)}",
    ]
    added = _top_added_objects(diff)
    if added:
        lines.append(f"- Biggest additions: {', '.join(added)}.")
    changed = _top_changed_objects(diff)
    if changed:
        lines.append(f"- Biggest changes: {', '.join(changed)}.")
    removed = _top_removed_objects(diff)
    if removed:
        lines.append(f"- Biggest removals: {', '.join(removed)}.")
    lines.append(
        "- Files: "
        f"[snapshot]({data_prefix}/latest/{diff['dataset']}.json) · "
        f"[diff]({data_prefix}/diffs/{run_date}/{diff['dataset']}.json) · "
        f"[reverse index]({data_prefix}/reverse-index/{diff['dataset']}.json)"
    )
    return "\n".join(lines) + "\n"


def render_daily_report(run_date: str, summary: dict[str, Any], diffs: list[dict[str, Any]]) -> str:
    platform_rollups = _platform_rollups(diffs)
    diff_by_dataset = {item["dataset"]: item for item in diffs}
    lines = [
        f"# Daily Drift Report: {run_date}",
        "",
        f"- Refreshed at: `{summary['generated_at_utc']}`",
    ]
    lines.extend(_leader_lines(summary, diffs))
    lines.extend([
        "",
        "## Platform overview",
        "",
        "| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |",
        "| --- | ---: | ---: | ---: | --- |",
    ])
    for platform in summary["platforms"]:
        rollup = platform_rollups.get(platform["platform"], {"added_objects": 0, "changed_objects": 0, "removed_objects": 0})
        lines.append(
            f"| {_platform_label(platform['platform'])} | `{_format_delta(platform['net_score'])}` | "
            f"`+{_format_int(rollup['added_objects'])} / ~{_format_int(rollup['changed_objects'])} / -{_format_int(rollup['removed_objects'])}` | "
            f"`+{_format_int(platform['added_atoms'])} / -{_format_int(platform['removed_atoms'])}` | "
            f"{_driver_text(platform, diff_by_dataset)} |"
        )

    lines.extend([
        "",
        "## Dataset overview",
        "",
        "| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) |",
        "| --- | --- | ---: | ---: | ---: |",
    ])
    for diff in sorted(diffs, key=lambda item: item["dataset"]):
        counts = diff["counts"]
        lines.append(
            f"| {_dataset_label(diff['dataset'])} | {_platform_label(diff['platform'])} | `{_format_int(counts['current_objects'])}` | "
            f"`+{_format_int(counts['added_objects'])} / ~{_format_int(counts['changed_objects'])} / -{_format_int(counts['removed_objects'])}` | "
            f"`+{_format_int(counts['added_atoms'])} / -{_format_int(counts['removed_atoms'])}` |"
        )

    lines.extend(["", "## Dataset details", ""])
    for diff in sorted(diffs, key=lambda item: item["dataset"]):
        lines.append(render_dataset_diff_markdown(diff, run_date, "../../data").rstrip())
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_platform_page(platform: str, diffs: list[dict[str, Any]], generated_at_utc: str | None = None, run_date: str | None = None) -> str:
    relevant = [diff for diff in diffs if diff["platform"] == platform]
    lines = [f"# {_platform_label(platform)}", ""]
    if generated_at_utc:
        lines.append(f"- Refreshed at: `{generated_at_utc}`")
        lines.append("")
    lines.extend([
        "## Dataset overview",
        "",
        "| Dataset | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |",
        "| --- | ---: | ---: | ---: | --- |",
    ])
    for diff in sorted(relevant, key=lambda item: item["dataset"]):
        counts = diff["counts"]
        report_date = run_date or diff["current_snapshot_date"]
        lines.append(
            f"| {_dataset_label(diff['dataset'])} | `{_format_int(counts['current_objects'])}` | "
            f"`+{_format_int(counts['added_objects'])} / ~{_format_int(counts['changed_objects'])} / -{_format_int(counts['removed_objects'])}` | "
            f"`+{_format_int(counts['added_atoms'])} / -{_format_int(counts['removed_atoms'])}` | "
            f"[snapshot](../../data/latest/{diff['dataset']}.json) · [diff](../../data/diffs/{report_date}/{diff['dataset']}.json) · [reverse index](../../data/reverse-index/{diff['dataset']}.json) |"
        )
    lines.extend(["", "## Dataset details", ""])
    for diff in sorted(relevant, key=lambda item: item["dataset"]):
        lines.extend(_dataset_movement_lines(diff, run_date or diff["current_snapshot_date"], "../../data"))
    return "\n".join(lines).rstrip() + "\n"


def render_docs_index(
    latest_summary: dict[str, Any] | None,
    latest_run: dict[str, Any] | None,
    diffs: list[dict[str, Any]],
) -> str:
    platform_rollups = _platform_rollups(diffs)
    diff_by_dataset = {item["dataset"]: item for item in diffs}
    lines = ["# Managed Permissions Drift Catalog", ""]
    if latest_run:
        report_link = ""
        if latest_summary:
            report_link = f" · [daily report](daily/{latest_summary['date']}.md)"
        lines.append(f"- Refreshed at: `{latest_run['finished_at']}`{report_link}")
    lines.extend(_leader_lines(latest_summary, diffs))
    lines.extend([
        "",
        "## Platform overview",
        "",
        "| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |",
        "| --- | ---: | ---: | ---: | --- |",
    ])
    if latest_summary:
        for platform in latest_summary["platforms"]:
            rollup = platform_rollups.get(platform["platform"], {"added_objects": 0, "changed_objects": 0, "removed_objects": 0})
            lines.append(
                f"| {_platform_label(platform['platform'])} | `{_format_delta(platform['net_score'])}` | "
                f"`+{_format_int(rollup['added_objects'])} / ~{_format_int(rollup['changed_objects'])} / -{_format_int(rollup['removed_objects'])}` | "
                f"`+{_format_int(platform['added_atoms'])} / -{_format_int(platform['removed_atoms'])}` | "
                f"{_driver_text(platform, diff_by_dataset)} |"
            )
    lines.extend([
        "",
        "## Dataset overview",
        "",
        "| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ])
    for diff in sorted(diffs, key=lambda item: item["dataset"]):
        counts = diff["counts"]
        report_date = latest_summary["date"] if latest_summary else diff["current_snapshot_date"]
        lines.append(
            f"| {_dataset_label(diff['dataset'])} | {_platform_label(diff['platform'])} | `{_format_int(counts['current_objects'])}` | "
            f"`+{_format_int(counts['added_objects'])} / ~{_format_int(counts['changed_objects'])} / -{_format_int(counts['removed_objects'])}` | "
            f"`+{_format_int(counts['added_atoms'])} / -{_format_int(counts['removed_atoms'])}` | "
            f"[snapshot](../data/latest/{diff['dataset']}.json) · [diff](../data/diffs/{report_date}/{diff['dataset']}.json) · [reverse index](../data/reverse-index/{diff['dataset']}.json) |"
        )
    lines.extend([
        "",
        "## Platform pages",
        "",
        "- [AWS](platforms/aws.md)",
        "- [Azure](platforms/azure.md)",
        "- [GCP](platforms/gcp.md)",
        "- [GitHub](platforms/github.md)",
    ])
    return "\n".join(lines).rstrip() + "\n"


def render_readme(
    *,
    latest_run: dict[str, Any] | None,
    latest_summary: dict[str, Any] | None,
    latest_diffs: list[dict[str, Any]],
) -> str:
    lines = [
        "# managed-permissions-drift-catalog",
        "",
        "Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.",
        "",
        "## Latest drift",
        "",
    ]
    if latest_run:
        report_link = ""
        if latest_summary:
            report_link = f" · [daily report](docs/daily/{latest_summary['date']}.md)"
        lines.append(f"- Refreshed at: `{latest_run['finished_at']}`{report_link}")
    lines.extend(_leader_lines(latest_summary, latest_diffs))

    lines.extend(["", "## Platform overview", "", "| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |", "| --- | ---: | ---: | ---: | --- |"])
    platform_rollups = _platform_rollups(latest_diffs)
    diff_by_dataset = {item["dataset"]: item for item in latest_diffs}
    if latest_summary:
        for platform in latest_summary["platforms"]:
            rollup = platform_rollups.get(platform["platform"], {"added_objects": 0, "changed_objects": 0, "removed_objects": 0})
            driver_text = _driver_text(platform, diff_by_dataset)
            lines.append(
                f"| {_platform_label(platform['platform'])} | `{_format_delta(platform['net_score'])}` | "
                f"`+{_format_int(rollup['added_objects'])} / ~{_format_int(rollup['changed_objects'])} / -{_format_int(rollup['removed_objects'])}` | "
                f"`+{_format_int(platform['added_atoms'])} / -{_format_int(platform['removed_atoms'])}` | {driver_text} |"
            )

    lines.extend([
        "",
        "## Dataset overview",
        "",
        "| Dataset | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |",
        "| --- | ---: | ---: | ---: | --- |",
    ])
    lines.extend(_dataset_table_rows_for_readme(latest_diffs, latest_summary["date"] if latest_summary else "latest"))

    lines.extend(["", "## Latest dataset movement", ""])
    diff_map = {item["dataset"]: item for item in latest_diffs}
    for dataset in DATASETS:
        diff = diff_map.get(dataset)
        if diff is None:
            continue
        lines.extend(_dataset_movement_lines(diff, latest_summary["date"] if latest_summary else "latest", "data"))
    return "\n".join(lines).rstrip() + "\n"
