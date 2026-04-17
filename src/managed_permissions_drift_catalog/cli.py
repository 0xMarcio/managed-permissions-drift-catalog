from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from fnmatch import fnmatch
from pathlib import Path
from typing import Any

from .config import DATASETS, Settings
from .diffing import atom_to_permission_terms, build_dataset_diff, build_reverse_index
from .http import HttpClient
from .models import DatasetSnapshot
from .render import render_daily_report, render_docs_index, render_platform_page, render_readme
from .scoring import summarize_daily_scores
from .sources import REGISTRY
from .storage import Storage
from .utils import canonicalize, isoformat_utc, stable_json_dumps


def repo_root() -> Path:
    current = Path.cwd().resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "pyproject.toml").exists() and (candidate / "src" / "managed_permissions_drift_catalog").exists():
            return candidate
    return Path(__file__).resolve().parents[2]


def git_head_sha(root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def load_snapshot_summaries(storage: Storage) -> dict[str, dict[str, Any]]:
    snapshots: dict[str, dict[str, Any]] = {}
    for dataset in DATASETS:
        snapshot = storage.read_snapshot(dataset)
        if snapshot is None:
            continue
        snapshot_dict = snapshot.to_dict()
        snapshots[dataset] = {
            "dataset": snapshot_dict["dataset"],
            "platform": snapshot_dict["platform"],
            "generated_at_utc": snapshot_dict["generated_at_utc"],
            "object_count": snapshot_dict["object_count"],
        }
    return snapshots


def load_diffs_for_date(storage: Storage, run_date: str) -> list[dict[str, Any]]:
    diffs: list[dict[str, Any]] = []
    for dataset in DATASETS:
        path = storage.diff_path(run_date, dataset)
        if not path.exists():
            continue
        diffs.append(json.loads(path.read_text(encoding="utf-8")))
    return diffs


def snapshot_semantic_signature(snapshot: DatasetSnapshot) -> dict[str, Any]:
    data = snapshot.to_dict()
    data["generated_at_utc"] = ""
    for item in data["objects"]:
        item["fetched_at_utc"] = ""
    return canonicalize(data)


def snapshots_semantically_equal(left: DatasetSnapshot | None, right: DatasetSnapshot | None) -> bool:
    if left is None or right is None:
        return left is right
    return snapshot_semantic_signature(left) == snapshot_semantic_signature(right)


def write_docs_and_readme(
    *,
    settings: Settings,
    storage: Storage,
    latest_run: dict[str, Any] | None,
    summary: dict[str, Any] | None,
    latest_diffs: list[dict[str, Any]],
) -> bool:
    changed = False
    snapshots = load_snapshot_summaries(storage)
    changed |= storage.write_text_if_changed(storage.docs_index_path(), render_docs_index(summary, snapshots))
    for platform in ("aws", "azure", "gcp", "github"):
        changed |= storage.write_text_if_changed(
            storage.docs_platform_path(platform),
            render_platform_page(platform, snapshots),
        )
    changed |= storage.write_text_if_changed(
        settings.root / "README.md",
        render_readme(latest_run=latest_run, latest_summary=summary, snapshots=snapshots, latest_diffs=latest_diffs),
    )
    return changed


def query_permission(storage: Storage, permission: str, *, glob_aware: bool = True) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for dataset in DATASETS:
        snapshot = storage.read_snapshot(dataset)
        if snapshot is None:
            continue
        reverse_index_path = storage.reverse_index_path(dataset)
        if not reverse_index_path.exists():
            continue
        reverse_index = json.loads(reverse_index_path.read_text(encoding="utf-8"))
        for atom, objects in reverse_index.get("exact", {}).items():
            terms = atom_to_permission_terms(atom)
            if permission == atom or permission in terms:
                results.append({"dataset": dataset, "atom": atom, "matches": objects, "match_type": "exact"})
        if not glob_aware:
            continue
        for item in reverse_index.get("wildcard_atoms", []):
            if any(_wildcard_term_matches(permission, term) for term in item["terms"]):
                results.append(
                    {
                        "dataset": dataset,
                        "atom": item["atom"],
                        "matches": [item["object"]],
                        "match_type": "wildcard",
                    }
                )
    deduped: dict[tuple[str, str, str], dict[str, Any]] = {}
    for result in results:
        for match in result["matches"]:
            key = (result["dataset"], result["atom"], match["stable_id"])
            deduped[key] = {
                "dataset": result["dataset"],
                "atom": result["atom"],
                "match_type": result["match_type"],
                "object": match,
            }
    return sorted(deduped.values(), key=lambda item: (item["dataset"], item["atom"], item["object"]["stable_id"]))


def _wildcard_term_matches(permission: str, term: str) -> bool:
    if "*" not in term and "?" not in term:
        return False
    if not fnmatch(permission, term):
        return False
    literal_chunks = [chunk for chunk in re.split(r"[*?]+", term) if chunk]
    if not literal_chunks:
        return False
    return any(permission.startswith(chunk) or permission.endswith(chunk) or chunk in permission for chunk in literal_chunks)


def validate_outputs(storage: Storage) -> list[str]:
    errors: list[str] = []
    for dataset in DATASETS:
        snapshot = storage.read_snapshot(dataset)
        if snapshot is None:
            errors.append(f"Missing latest snapshot for {dataset}")
            continue
        seen_ids: set[str] = set()
        for obj in snapshot.objects:
            if obj.stable_id in seen_ids:
                errors.append(f"Duplicate stable_id {obj.stable_id} in {dataset}")
            seen_ids.add(obj.stable_id)
            if obj.derived_atoms != sorted(set(obj.derived_atoms)):
                errors.append(f"Non-deterministic derived_atoms ordering for {obj.stable_id}")
            if not obj.source_url:
                errors.append(f"Missing source_url for {obj.stable_id}")
        reverse_index_path = storage.reverse_index_path(dataset)
        if not reverse_index_path.exists():
            errors.append(f"Missing reverse index for {dataset}")
    return errors


def orchestrate_update(settings: Settings, selected_datasets: list[str] | None = None) -> int:
    storage = Storage(settings.root)
    client = HttpClient(
        user_agent=settings.user_agent,
        timeout_seconds=settings.http_timeout_seconds,
        max_retries=settings.max_retries,
    )
    datasets = selected_datasets or DATASETS
    started_at = isoformat_utc()
    warnings_by_dataset: dict[str, list[str]] = {}
    diffs: list[dict[str, Any]] = []
    outputs_changed = False
    any_dataset_changed = False
    fetch_status: dict[str, Any] = {}

    for dataset in datasets:
        adapter = REGISTRY[dataset]
        previous_snapshot = storage.read_snapshot(dataset)
        previous_snapshot_date = storage.previous_snapshot(dataset, exclude_date=settings.today_utc)
        previous_for_diff: DatasetSnapshot | None
        previous_date_value: str | None
        if previous_snapshot is not None:
            previous_for_diff = previous_snapshot
            previous_date_value = previous_snapshot.generated_at_utc[:10]
        elif previous_snapshot_date is not None:
            previous_date_value, previous_for_diff = previous_snapshot_date
        else:
            previous_for_diff = None
            previous_date_value = None

        try:
            fetch_result = adapter.fetch(settings, storage, client)
            new_snapshot = adapter.normalize(settings, storage, fetch_result["fetched_at_utc"])
            semantic_changed = not snapshots_semantically_equal(previous_snapshot, new_snapshot)
            if semantic_changed:
                any_dataset_changed = True
                snapshot = new_snapshot
                outputs_changed |= storage.write_json_if_changed(storage.latest_snapshot_path(dataset), snapshot.to_dict())
                outputs_changed |= storage.write_gzip_json_if_changed(
                    storage.snapshot_path(dataset, settings.today_utc),
                    snapshot.to_dict(),
                )
                reverse_index = build_reverse_index(snapshot)
                outputs_changed |= storage.write_json_if_changed(storage.reverse_index_path(dataset), reverse_index)
                diff = build_dataset_diff(
                    dataset=dataset,
                    platform=adapter.platform,
                    current_snapshot=snapshot,
                    previous_snapshot=previous_for_diff,
                    previous_snapshot_date=previous_date_value,
                    current_snapshot_date=settings.today_utc,
                    compared_at_utc=settings.generated_at_utc,
                    warnings=snapshot.warnings,
                )
                outputs_changed |= storage.write_json_if_changed(storage.diff_path(settings.today_utc, dataset), diff)
            else:
                snapshot = previous_snapshot or new_snapshot
                diff_path = storage.diff_path(settings.today_utc, dataset)
                if diff_path.exists():
                    diff = json.loads(diff_path.read_text(encoding="utf-8"))
                else:
                    diff = build_dataset_diff(
                        dataset=dataset,
                        platform=adapter.platform,
                        current_snapshot=snapshot,
                        previous_snapshot=previous_for_diff,
                        previous_snapshot_date=previous_date_value,
                        current_snapshot_date=settings.today_utc,
                        compared_at_utc=settings.generated_at_utc,
                        warnings=snapshot.warnings,
                    )
                    outputs_changed |= storage.write_json_if_changed(diff_path, diff)
                reverse_index_path = storage.reverse_index_path(dataset)
                if not reverse_index_path.exists():
                    outputs_changed |= storage.write_json_if_changed(reverse_index_path, build_reverse_index(snapshot))
            warnings_by_dataset[dataset] = list(snapshot.warnings)
            diffs.append(diff)
            fetch_status[dataset] = {
                "status": "ok",
                "warnings": snapshot.warnings,
                "fetched_at_utc": fetch_result["fetched_at_utc"],
            }
        except Exception as exc:  # noqa: BLE001
            warning = f"Source update failed; keeping previous data. Error: {exc}"
            warnings_by_dataset[dataset] = [warning]
            fetch_status[dataset] = {"status": "error", "errors": [str(exc)]}
            if previous_snapshot is not None:
                diff = build_dataset_diff(
                    dataset=dataset,
                    platform=adapter.platform,
                    current_snapshot=previous_snapshot,
                    previous_snapshot=previous_for_diff,
                    previous_snapshot_date=previous_date_value,
                    current_snapshot_date=settings.today_utc,
                    compared_at_utc=settings.generated_at_utc,
                    warnings=[warning],
                )
                outputs_changed |= storage.write_json_if_changed(storage.diff_path(settings.today_utc, dataset), diff)
                diffs.append(diff)

    required_daily_outputs = [
        storage.summary_path(settings.today_utc),
        storage.docs_daily_path(settings.today_utc),
        storage.run_manifest_path(settings.today_utc),
        storage.docs_index_path(),
        storage.docs_platform_path("aws"),
        storage.docs_platform_path("azure"),
        storage.docs_platform_path("gcp"),
        storage.docs_platform_path("github"),
        settings.root / "README.md",
    ]
    if not any_dataset_changed and all(path.exists() for path in required_daily_outputs):
        return 0

    summary = summarize_daily_scores(
        run_date=settings.today_utc,
        compared_at_utc=settings.generated_at_utc,
        diffs=diffs,
        warnings_by_dataset=warnings_by_dataset,
    )
    outputs_changed |= storage.write_json_if_changed(storage.summary_path(settings.today_utc), summary)
    outputs_changed |= storage.write_text_if_changed(
        storage.docs_daily_path(settings.today_utc),
        render_daily_report(settings.today_utc, summary, diffs),
    )
    finished_at = isoformat_utc()
    run_manifest = {
        "date": settings.today_utc,
        "started_at": started_at,
        "finished_at": finished_at,
        "git_commit_sha": git_head_sha(settings.root),
        "outputs_changed": outputs_changed,
        "per_source": fetch_status,
        "warnings_by_dataset": warnings_by_dataset,
    }
    outputs_changed |= storage.write_json_if_changed(storage.run_manifest_path(settings.today_utc), run_manifest)
    outputs_changed |= write_docs_and_readme(
        settings=settings,
        storage=storage,
        latest_run=run_manifest,
        summary=summary,
        latest_diffs=diffs,
    )
    return 0


def command_fetch(args: argparse.Namespace) -> int:
    settings = Settings.from_root(repo_root())
    storage = Storage(settings.root)
    client = HttpClient(
        user_agent=settings.user_agent,
        timeout_seconds=settings.http_timeout_seconds,
        max_retries=settings.max_retries,
    )
    adapter = REGISTRY[args.dataset]
    result = adapter.fetch(settings, storage, client)
    sys.stdout.write(stable_json_dumps(result))
    return 0


def command_normalize(args: argparse.Namespace) -> int:
    settings = Settings.from_root(repo_root())
    storage = Storage(settings.root)
    adapter = REGISTRY[args.dataset]
    snapshot = adapter.normalize(settings, storage, settings.generated_at_utc)
    storage.write_json_if_changed(storage.latest_snapshot_path(args.dataset), snapshot.to_dict())
    storage.write_gzip_json_if_changed(storage.snapshot_path(args.dataset, settings.today_utc), snapshot.to_dict())
    sys.stdout.write(stable_json_dumps(snapshot.to_dict()))
    return 0


def command_diff(args: argparse.Namespace) -> int:
    settings = Settings.from_root(repo_root())
    storage = Storage(settings.root)
    datasets = [args.dataset] if args.dataset else DATASETS
    rendered: list[dict[str, Any]] = []
    for dataset in datasets:
        snapshot = storage.read_snapshot(dataset)
        if snapshot is None:
            continue
        previous = storage.previous_snapshot(dataset, exclude_date=settings.today_utc)
        previous_date, previous_snapshot = previous if previous else (None, None)
        platform = REGISTRY[dataset].platform
        diff = build_dataset_diff(
            dataset=dataset,
            platform=platform,
            current_snapshot=snapshot,
            previous_snapshot=previous_snapshot,
            previous_snapshot_date=previous_date,
            current_snapshot_date=settings.today_utc,
            compared_at_utc=settings.generated_at_utc,
            warnings=snapshot.warnings,
        )
        storage.write_json_if_changed(storage.diff_path(settings.today_utc, dataset), diff)
        rendered.append(diff)
    sys.stdout.write(stable_json_dumps(rendered))
    return 0


def command_render(args: argparse.Namespace) -> int:
    settings = Settings.from_root(repo_root())
    storage = Storage(settings.root)
    render_date = args.date or settings.today_utc
    summary_path = storage.summary_path(render_date)
    summary = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else None
    latest_run_path = storage.run_manifest_path(render_date)
    latest_run = json.loads(latest_run_path.read_text(encoding="utf-8")) if latest_run_path.exists() else None
    write_docs_and_readme(
        settings=settings,
        storage=storage,
        latest_run=latest_run,
        summary=summary,
        latest_diffs=load_diffs_for_date(storage, render_date),
    )
    return 0


def command_query(args: argparse.Namespace) -> int:
    storage = Storage(repo_root())
    results = query_permission(storage, args.permission, glob_aware=not args.exact_only)
    if args.json:
        sys.stdout.write(stable_json_dumps(results))
        return 0
    if not results:
        sys.stdout.write("No matches found.\n")
        return 0
    for result in results:
        obj = result["object"]
        sys.stdout.write(
            f"{result['dataset']} | {result['match_type']} | {result['atom']} | {obj['stable_id']} | {obj['display_name']}\n"
        )
    return 0


def command_validate(args: argparse.Namespace) -> int:
    storage = Storage(repo_root())
    errors = validate_outputs(storage)
    if errors:
        for error in errors:
            sys.stderr.write(f"{error}\n")
        return 1
    sys.stdout.write("Validation passed.\n")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="managed_permissions_drift_catalog")
    subparsers = parser.add_subparsers(dest="command", required=True)

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--dataset", action="append", choices=DATASETS)
    update_parser.set_defaults(func=lambda args: orchestrate_update(Settings.from_root(repo_root()), args.dataset))

    fetch_parser = subparsers.add_parser("fetch")
    fetch_parser.add_argument("--dataset", required=True, choices=DATASETS)
    fetch_parser.set_defaults(func=command_fetch)

    normalize_parser = subparsers.add_parser("normalize")
    normalize_parser.add_argument("--dataset", required=True, choices=DATASETS)
    normalize_parser.set_defaults(func=command_normalize)

    diff_parser = subparsers.add_parser("diff")
    diff_parser.add_argument("--dataset", choices=DATASETS)
    diff_parser.set_defaults(func=command_diff)

    render_parser = subparsers.add_parser("render")
    render_parser.add_argument("--date")
    render_parser.set_defaults(func=command_render)

    query_parser = subparsers.add_parser("query")
    query_parser.add_argument("--permission", required=True)
    query_parser.add_argument("--exact-only", action="store_true")
    query_parser.add_argument("--json", action="store_true")
    query_parser.set_defaults(func=command_query)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.set_defaults(func=command_validate)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
