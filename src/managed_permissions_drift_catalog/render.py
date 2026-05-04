from __future__ import annotations

from collections import defaultdict
from datetime import date, timedelta
from typing import Any

from .config import DATASETS
from .scoring import score_dataset_diff

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
MONTH_NAMES = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
RECENT_ACTIVITY_WINDOWS = (7, 30)
MOVEMENT_COUNT_KEYS = ("added_objects", "changed_objects", "removed_objects", "added_atoms", "removed_atoms")


def _format_int(value: int) -> str:
    return f"{value:,}"


def _format_delta(value: int) -> str:
    if value > 0:
        return f"+{value:,}"
    return f"{value:,}"


def _plural(value: int, singular: str, plural: str | None = None) -> str:
    if abs(value) == 1:
        return singular
    return plural or f"{singular}s"


def _diff_date(diff: dict[str, Any]) -> str:
    return diff.get("current_snapshot_date") or diff.get("date") or ""


def _parse_iso_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def _format_date(value: str | None) -> str:
    parsed = _parse_iso_date(value)
    if parsed is None:
        return value or ""
    return f"{MONTH_NAMES[parsed.month - 1]} {parsed.day}, {parsed.year}"


def _has_movement(diff: dict[str, Any]) -> bool:
    counts = diff.get("counts", {})
    return any(int(counts.get(key, 0)) for key in MOVEMENT_COUNT_KEYS)


def _is_baseline_diff(diff: dict[str, Any]) -> bool:
    return not diff.get("previous_snapshot_date")


def _empty_counts() -> dict[str, int]:
    return {key: 0 for key in MOVEMENT_COUNT_KEYS}


def _empty_activity(*, dataset: str | None = None, platform: str | None = None) -> dict[str, Any]:
    return {
        "dataset": dataset,
        "platform": platform,
        "counts": _empty_counts(),
        "net_score": 0,
        "active_days": 0,
        "dates": [],
        "last_changed_date": None,
        "events": [],
    }


def _score_for_activity(diff: dict[str, Any]) -> int:
    if "atom_changes" in diff:
        return int(score_dataset_diff(diff)["score"])
    counts = diff.get("counts", {})
    return int(counts.get("added_atoms", 0)) - int(counts.get("removed_atoms", 0))


def _diff_magnitude(diff: dict[str, Any]) -> int:
    counts = diff.get("counts", {})
    return sum(abs(int(counts.get(key, 0))) for key in MOVEMENT_COUNT_KEYS)


def _add_diff_to_activity(activity: dict[str, Any], diff: dict[str, Any], score: int, diff_date: str) -> None:
    counts = diff.get("counts", {})
    for key in MOVEMENT_COUNT_KEYS:
        activity["counts"][key] += int(counts.get(key, 0))
    activity["net_score"] += score
    if diff_date not in activity["dates"]:
        activity["dates"].append(diff_date)
    activity["last_changed_date"] = max(activity["dates"])


def build_recent_activity(
    diff_history: list[dict[str, Any]],
    *,
    latest_date: str | None = None,
    windows: tuple[int, ...] = RECENT_ACTIVITY_WINDOWS,
) -> dict[str, Any] | None:
    latest_day = _parse_iso_date(latest_date)
    if latest_day is None:
        history_dates = [_parse_iso_date(_diff_date(diff)) for diff in diff_history]
        latest_day = max((item for item in history_dates if item is not None), default=None)
    if latest_day is None:
        return None

    result: dict[str, Any] = {"latest_date": latest_day.isoformat(), "windows": {}}
    for window_days in windows:
        start_day = latest_day - timedelta(days=window_days - 1)
        window: dict[str, Any] = {
            "days": window_days,
            "label": f"{window_days}d",
            "start_date": start_day.isoformat(),
            "end_date": latest_day.isoformat(),
            "available_dates": [],
            "baseline_diffs_skipped": 0,
            "datasets": {},
            "platforms": {},
            "events": [],
        }
        available_dates: set[str] = set()
        for diff in diff_history:
            diff_date_text = _diff_date(diff)
            diff_day = _parse_iso_date(diff_date_text)
            if diff_day is None or diff_day < start_day or diff_day > latest_day:
                continue
            available_dates.add(diff_date_text)
            if _is_baseline_diff(diff):
                window["baseline_diffs_skipped"] += 1
                continue
            if not _has_movement(diff):
                continue

            dataset = diff["dataset"]
            platform = diff["platform"]
            dataset_activity = window["datasets"].setdefault(
                dataset, _empty_activity(dataset=dataset, platform=platform)
            )
            platform_activity = window["platforms"].setdefault(platform, _empty_activity(platform=platform))
            score = _score_for_activity(diff)
            _add_diff_to_activity(dataset_activity, diff, score, diff_date_text)
            _add_diff_to_activity(platform_activity, diff, score, diff_date_text)
            event = {
                "date": diff_date_text,
                "dataset": dataset,
                "platform": platform,
                "score": score,
                "magnitude": _diff_magnitude(diff),
                "summary": _short_change_summary(diff),
                "diff": diff,
            }
            dataset_activity["events"].append(event)
            platform_activity["events"].append(event)
            window["events"].append(event)

        window["available_dates"] = sorted(available_dates)
        for collection in (window["datasets"], window["platforms"]):
            for activity in collection.values():
                activity["dates"].sort()
                activity["active_days"] = len(activity["dates"])
                activity["events"].sort(key=lambda item: (item["date"], item["magnitude"]), reverse=True)
        window["events"].sort(key=lambda item: (item["date"], item["magnitude"]), reverse=True)
        result["windows"][window_days] = window
    return result


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


def _window(recent_activity: dict[str, Any] | None, days: int) -> dict[str, Any] | None:
    if not recent_activity:
        return None
    return recent_activity.get("windows", {}).get(days)


def _activity_for_platform(recent_activity: dict[str, Any] | None, days: int, platform: str) -> dict[str, Any]:
    window = _window(recent_activity, days)
    if not window:
        return _empty_activity(platform=platform)
    return window.get("platforms", {}).get(platform, _empty_activity(platform=platform))


def _activity_for_dataset(
    recent_activity: dict[str, Any] | None,
    days: int,
    dataset: str,
    platform: str | None = None,
) -> dict[str, Any]:
    window = _window(recent_activity, days)
    if not window:
        return _empty_activity(dataset=dataset, platform=platform)
    return window.get("datasets", {}).get(dataset, _empty_activity(dataset=dataset, platform=platform))


def _format_count_parts(counts: dict[str, int]) -> list[str]:
    parts: list[str] = []
    if counts.get("added_objects"):
        value = counts["added_objects"]
        parts.append(f"`+{_format_int(value)}` {_plural(value, 'object')}")
    if counts.get("changed_objects"):
        value = counts["changed_objects"]
        parts.append(f"`~{_format_int(value)}` {_plural(value, 'object')}")
    if counts.get("removed_objects"):
        value = counts["removed_objects"]
        parts.append(f"`-{_format_int(value)}` {_plural(value, 'object')}")
    if counts.get("added_atoms"):
        value = counts["added_atoms"]
        parts.append(f"`+{_format_int(value)}` {_plural(value, 'atom')}")
    if counts.get("removed_atoms"):
        value = counts["removed_atoms"]
        parts.append(f"`-{_format_int(value)}` {_plural(value, 'atom')}")
    return parts


def _format_activity(activity: dict[str, Any], *, include_active_days: bool = True) -> str:
    if not activity or not activity.get("active_days"):
        return "No movement"
    parts: list[str] = []
    net_score = int(activity.get("net_score", 0))
    if net_score:
        parts.append(f"`{_format_delta(net_score)}` net")
    parts.extend(_format_count_parts(activity.get("counts", {})))
    if include_active_days:
        active_days = int(activity["active_days"])
        parts.append(f"{active_days} active {_plural(active_days, 'day')}")
    return " · ".join(parts) if parts else "No movement"


def _activity_sort_key(activity: dict[str, Any]) -> tuple[int, int, int, int, str]:
    counts = activity.get("counts", {})
    object_movement = sum(int(counts.get(key, 0)) for key in ("added_objects", "changed_objects", "removed_objects"))
    atom_movement = sum(int(counts.get(key, 0)) for key in ("added_atoms", "removed_atoms"))
    return (
        abs(int(activity.get("net_score", 0))),
        atom_movement,
        object_movement,
        int(activity.get("active_days", 0)),
        activity.get("last_changed_date") or "",
    )


def _recent_driver_text(platform: str, recent_activity: dict[str, Any] | None, data_prefix: str = "data") -> str:
    for days in (7, 30):
        window = _window(recent_activity, days)
        if not window:
            continue
        candidates = [
            activity
            for activity in window.get("datasets", {}).values()
            if activity.get("platform") == platform and activity.get("active_days")
        ]
        if not candidates:
            continue
        winner = sorted(candidates, key=_activity_sort_key, reverse=True)[0]
        changed_date = winner["last_changed_date"]
        dataset = winner["dataset"]
        return (
            f"{_dataset_label(dataset)} ({days}d, last changed "
            f"[{_format_date(changed_date)}]({data_prefix}/diffs/{changed_date}/{dataset}.json))"
        )
    return "No movement"


def _last_changed_text(activity: dict[str, Any], data_prefix: str = "data") -> str:
    changed_date = activity.get("last_changed_date")
    dataset = activity.get("dataset")
    if changed_date and dataset:
        return f"[{_format_date(changed_date)}]({data_prefix}/diffs/{changed_date}/{dataset}.json)"
    return "No movement"


def _recent_highlight_text(activity: dict[str, Any], limit: int = 3) -> str:
    events = activity.get("events", [])[:limit]
    if not events:
        return ""
    highlights: list[str] = []
    for event in events:
        diff = event["diff"]
        objects = (_top_added_objects(diff, 1) + _top_changed_objects(diff, 1) + _top_removed_objects(diff, 1))[:2]
        detail = f" ({', '.join(objects)})" if objects else ""
        highlights.append(f"{_format_date(event['date'])}: {event['summary']}{detail}")
    return "; ".join(highlights)


def _leader_lines(summary: dict[str, Any] | None, diffs: list[dict[str, Any]]) -> list[str]:
    if not summary:
        return []
    winner_platform, _direction = _pick_winner_platform(summary.get("platforms", []))
    if winner_platform is None:
        return []
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


def _dataset_movement_lines(
    diff: dict[str, Any],
    run_date: str,
    data_prefix: str = "data",
    recent_activity: dict[str, Any] | None = None,
) -> list[str]:
    counts = diff["counts"]
    lines = [
        f"### {_dataset_label(diff['dataset'])}",
        "",
        f"- Inventory: `{_format_int(counts['current_objects'])}` objects.",
    ]
    if recent_activity:
        seven_day = _activity_for_dataset(recent_activity, 7, diff["dataset"], diff["platform"])
        thirty_day = _activity_for_dataset(recent_activity, 30, diff["dataset"], diff["platform"])
        lines.append(f"- Last 7 days: {_format_activity(seven_day)}.")
        lines.append(f"- Last 30 days: {_format_activity(thirty_day)}.")
        highlight_source = seven_day if seven_day.get("active_days") else thirty_day
        highlights = _recent_highlight_text(highlight_source)
        if highlights:
            lines.append(f"- Recent highlights: {highlights}.")
    else:
        lines.append(f"- Today: {_dataset_today_line(diff)}")
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
        lines.append(f"- Refreshed: {_format_date(latest_run['finished_at'])}{report_link}")
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
    recent_diffs: list[dict[str, Any]] | None = None,
    recent_activity: dict[str, Any] | None = None,
) -> str:
    latest_date = latest_summary["date"] if latest_summary else None
    if recent_activity is None and recent_diffs is not None:
        recent_activity = build_recent_activity(
            recent_diffs,
            latest_date=latest_date,
        )
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
        lines.append(f"- Refreshed: {_format_date(latest_run['finished_at'])}{report_link}")

    lines.extend([
        "",
        "## Platform overview",
        "",
        "| Platform | Last 7 days | Last 30 days | Main recent driver |",
        "| --- | --- | --- | --- |",
    ])
    if latest_summary:
        for platform in latest_summary["platforms"]:
            platform_name = platform["platform"]
            lines.append(
                f"| {_platform_label(platform_name)} | {_format_activity(_activity_for_platform(recent_activity, 7, platform_name))} | "
                f"{_format_activity(_activity_for_platform(recent_activity, 30, platform_name))} | "
                f"{_recent_driver_text(platform_name, recent_activity)} |"
            )

    lines.extend([
        "",
        "## Dataset overview",
        "",
        "| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |",
        "| --- | ---: | --- | --- | --- | --- |",
    ])
    report_date = latest_summary["date"] if latest_summary else "latest"
    for diff in sorted(latest_diffs, key=lambda item: item["dataset"]):
        counts = diff["counts"]
        seven_day = _activity_for_dataset(recent_activity, 7, diff["dataset"], diff["platform"])
        thirty_day = _activity_for_dataset(recent_activity, 30, diff["dataset"], diff["platform"])
        lines.append(
            f"| {_dataset_label(diff['dataset'])} | `{_format_int(counts['current_objects'])}` | "
            f"{_last_changed_text(thirty_day)} | "
            f"{_format_activity(seven_day)} | "
            f"{_format_activity(thirty_day)} | "
            f"[snapshot](data/latest/{diff['dataset']}.json) · [diff](data/diffs/{report_date}/{diff['dataset']}.json) · [reverse index](data/reverse-index/{diff['dataset']}.json) |"
        )

    lines.extend(["", "## Latest dataset movement", ""])
    diff_map = {item["dataset"]: item for item in latest_diffs}
    for dataset in DATASETS:
        diff = diff_map.get(dataset)
        if diff is None:
            continue
        lines.extend(_dataset_movement_lines(diff, report_date, "data", recent_activity))
    return "\n".join(lines).rstrip() + "\n"
