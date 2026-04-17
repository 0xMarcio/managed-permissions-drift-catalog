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


def _source_health_line(latest_run: dict[str, Any] | None) -> str | None:
    if not latest_run:
        return None
    per_source = latest_run.get("per_source") or {}
    if not per_source:
        return None
    total = len(per_source)
    ok = sum(1 for item in per_source.values() if item.get("status") == "ok")
    failures = sorted(dataset for dataset, item in per_source.items() if item.get("status") != "ok")
    if not failures:
        return f"`{ok}/{total}` datasets refreshed cleanly."
    failure_list = ", ".join(f"`{dataset}`" for dataset in failures)
    return f"`{ok}/{total}` datasets refreshed cleanly; issues: {failure_list}."


def _baseline_note(diffs: list[dict[str, Any]]) -> str | None:
    baseline = [
        diff
        for diff in diffs
        if diff["counts"]["previous_objects"] == 0 and diff["counts"]["current_objects"] > 0
    ]
    if not baseline:
        return None
    labels = ", ".join(_dataset_label(diff["dataset"]) for diff in baseline)
    return (
        f"`{len(baseline)}/{len(diffs)}` datasets were first captured in this report: {labels}. "
        "Large positive scores on those datasets reflect initial inventory capture, not day-over-day expansion."
    )


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


def _headline_line(summary: dict[str, Any] | None, diffs: list[dict[str, Any]]) -> str | None:
    if not summary:
        return None
    winner_platform, direction = _pick_winner_platform(summary.get("platforms", []))
    if winner_platform is None:
        total_object_changes = sum(
            diff["counts"]["added_objects"] + diff["counts"]["changed_objects"] + diff["counts"]["removed_objects"]
            for diff in diffs
        )
        if total_object_changes:
            return (
                "No platform had net privilege drift, "
                f"but `{_format_int(total_object_changes)}` objects were added, removed, or changed."
            )
        return "No platform had net privilege drift."

    driver = _driver_dataset(winner_platform)
    diff_by_dataset = {item["dataset"]: item for item in diffs}
    detail = ""
    if driver and driver["dataset"] in diff_by_dataset:
        detail = f", driven by {_dataset_label(driver['dataset'])}: {_dataset_today_line(diff_by_dataset[driver['dataset']]).lower()}"
    if direction == "increase":
        return (
            f"{_platform_label(winner_platform['platform'])} had the largest net privilege increase "
            f"({_format_delta(winner_platform['net_score'])}){detail}"
        )
    return (
        f"{_platform_label(winner_platform['platform'])} had the largest net privilege decrease "
        f"({_format_delta(winner_platform['net_score'])}){detail}"
    )


def _driver_text(platform_entry: dict[str, Any], diff_by_dataset: dict[str, dict[str, Any]]) -> str:
    driver = _driver_dataset(platform_entry)
    if not driver:
        return "No dataset drift"
    diff = diff_by_dataset.get(driver["dataset"])
    if not diff:
        return f"{_dataset_label(driver['dataset'])} ({_format_delta(driver['score'])})"
    counts = diff["counts"]
    if counts["previous_objects"] == 0 and counts["current_objects"] > 0:
        return (
            f"{_dataset_label(driver['dataset'])}: initial `{_format_int(counts['current_objects'])}` objects, "
            f"`+{_format_int(counts['added_atoms'])}` atoms"
        )
    return (
        f"{_dataset_label(driver['dataset'])}: "
        f"`+{_format_int(counts['added_objects'])} / ~{_format_int(counts['changed_objects'])} / -{_format_int(counts['removed_objects'])}` objects, "
        f"`+{_format_int(counts['added_atoms'])} / -{_format_int(counts['removed_atoms'])}` atoms"
    )


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
    counts = diff["counts"]
    if counts["previous_objects"] == 0 and counts["current_objects"] > 0:
        atom_parts = []
        if counts["added_atoms"]:
            atom_parts.append(f"+{_format_int(counts['added_atoms'])} atoms")
        if counts["removed_atoms"]:
            atom_parts.append(f"-{_format_int(counts['removed_atoms'])} atoms")
        atoms_text = ", ".join(atom_parts) if atom_parts else "no atom-level change"
        return f"Initial inventory: `{_format_int(counts['current_objects'])}` objects, {atoms_text}."

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

    if not object_parts and not atom_parts:
        return "No drift detected."
    if object_parts and atom_parts:
        return f"{', '.join(object_parts)}; {', '.join(atom_parts)}."
    if object_parts:
        return f"{', '.join(object_parts)}; no atom-level change."
    return f"{', '.join(atom_parts)}."


def _dataset_movement_lines(diff: dict[str, Any], run_date: str) -> list[str]:
    lines = [
        f"### {_dataset_label(diff['dataset'])}",
        "",
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
    if diff["warnings"]:
        lines.append(f"- Warnings: {'; '.join(diff['warnings'])}")
    lines.append(
        "- Files: "
        f"[snapshot](data/latest/{diff['dataset']}.json) · "
        f"[diff](data/diffs/{run_date}/{diff['dataset']}.json) · "
        f"[reverse index](data/reverse-index/{diff['dataset']}.json)"
    )
    lines.append("")
    return lines


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
    latest_diffs: list[dict[str, Any]],
) -> str:
    lines = [
        "# managed-permissions-drift-catalog",
        "",
        "Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.",
        "",
        "## Latest snapshot",
        "",
    ]
    if latest_summary:
        lines.append(f"- Report date: [`{latest_summary['date']}`](docs/daily/{latest_summary['date']}.md)")
    if latest_run:
        lines.append(f"- Updated at: `{latest_run['finished_at']}`")
    source_health = _source_health_line(latest_run)
    if source_health:
        lines.append(f"- Source refresh: {source_health}")
    headline = _headline_line(latest_summary, latest_diffs)
    if headline:
        lines.append(f"- Headline: {headline}")
    baseline_note = _baseline_note(latest_diffs)
    if baseline_note:
        lines.append(f"- Baseline note: {baseline_note}")

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

    lines.extend(["", "## Latest dataset movement", ""])
    diff_map = {item["dataset"]: item for item in latest_diffs}
    for dataset in DATASETS:
        diff = diff_map.get(dataset)
        if diff is None:
            continue
        lines.extend(_dataset_movement_lines(diff, latest_summary["date"] if latest_summary else "latest"))

    lines.extend(
        [
            "## Browse outputs",
            "",
            "- [Full daily reports](docs/daily)",
            "- [Platform pages](docs/platforms)",
            "- [Docs index](docs/index.md)",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"
