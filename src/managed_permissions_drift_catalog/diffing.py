from __future__ import annotations

from collections import defaultdict
from typing import Any

from .models import DatasetSnapshot, NormalizedObject
from .utils import canonicalize


IGNORED_METADATA_FIELDS = {
    "endpoint_records",
    "policy_document",
    "raw_role_definition",
}


def _facet_delta(previous: dict[str, list[str]], current: dict[str, list[str]]) -> dict[str, dict[str, list[str]]]:
    facets = sorted(set(previous) | set(current))
    changes: dict[str, dict[str, list[str]]] = {}
    for facet in facets:
        prev_values = set(previous.get(facet, []))
        curr_values = set(current.get(facet, []))
        added = sorted(curr_values - prev_values)
        removed = sorted(prev_values - curr_values)
        if added or removed:
            changes[facet] = {"added": added, "removed": removed}
    return changes


def _metadata_changes(previous: NormalizedObject, current: NormalizedObject) -> list[dict[str, Any]]:
    changes: list[dict[str, Any]] = []
    scalar_fields = [
        "display_name",
        "description",
        "source_url",
        "source_version",
        "source_revision",
    ]
    for field_name in scalar_fields:
        before = getattr(previous, field_name)
        after = getattr(current, field_name)
        if before != after:
            changes.append({"field": field_name, "before": before, "after": after})

    previous_meta = {k: v for k, v in previous.metadata.items() if k not in IGNORED_METADATA_FIELDS}
    current_meta = {k: v for k, v in current.metadata.items() if k not in IGNORED_METADATA_FIELDS}
    for key in sorted(set(previous_meta) | set(current_meta)):
        before = canonicalize(previous_meta.get(key))
        after = canonicalize(current_meta.get(key))
        if before != after:
            changes.append({"field": f"metadata.{key}", "before": before, "after": after})
    return changes


def _all_atoms_by_facet(obj: NormalizedObject) -> dict[str, list[str]]:
    combined: dict[str, list[str]] = {}
    for facet, values in obj.grants_by_facet.items():
        combined[f"grant:{facet}"] = values
    for facet, values in obj.restrictions_by_facet.items():
        combined[f"restriction:{facet}"] = values
    return combined


def diff_object(previous: NormalizedObject, current: NormalizedObject) -> dict[str, Any] | None:
    grants = _facet_delta(previous.grants_by_facet, current.grants_by_facet)
    restrictions = _facet_delta(previous.restrictions_by_facet, current.restrictions_by_facet)
    metadata_changes = _metadata_changes(previous, current)
    if not grants and not restrictions and not metadata_changes:
        return None
    return {
        "stable_id": current.stable_id,
        "display_name": current.display_name,
        "source_url": current.source_url,
        "facet_changes": {
            "grants": grants,
            "restrictions": restrictions,
        },
        "metadata_changes": metadata_changes,
    }


def build_dataset_diff(
    *,
    dataset: str,
    platform: str,
    current_snapshot: DatasetSnapshot,
    previous_snapshot: DatasetSnapshot | None,
    previous_snapshot_date: str | None,
    current_snapshot_date: str,
    compared_at_utc: str,
    warnings: list[str] | None = None,
) -> dict[str, Any]:
    previous_map = {obj.stable_id: obj for obj in previous_snapshot.objects} if previous_snapshot else {}
    current_map = {obj.stable_id: obj for obj in current_snapshot.objects}

    added_objects: list[dict[str, Any]] = []
    removed_objects: list[dict[str, Any]] = []
    changed_objects: list[dict[str, Any]] = []

    atom_changes = {"added": [], "removed": []}
    by_facet_added: dict[str, list[str]] = defaultdict(list)
    by_facet_removed: dict[str, list[str]] = defaultdict(list)

    for stable_id in sorted(set(current_map) - set(previous_map)):
        obj = current_map[stable_id]
        added_objects.append(
            {
                "stable_id": obj.stable_id,
                "display_name": obj.display_name,
                "source_url": obj.source_url,
                "atoms_added": list(obj.derived_atoms),
            }
        )
        atom_changes["added"].extend(obj.derived_atoms)
        for facet, values in _all_atoms_by_facet(obj).items():
            by_facet_added[facet].extend(values)

    for stable_id in sorted(set(previous_map) - set(current_map)):
        obj = previous_map[stable_id]
        removed_objects.append(
            {
                "stable_id": obj.stable_id,
                "display_name": obj.display_name,
                "source_url": obj.source_url,
                "atoms_removed": list(obj.derived_atoms),
            }
        )
        atom_changes["removed"].extend(obj.derived_atoms)
        for facet, values in _all_atoms_by_facet(obj).items():
            by_facet_removed[facet].extend(values)

    for stable_id in sorted(set(previous_map) & set(current_map)):
        before = previous_map[stable_id]
        after = current_map[stable_id]
        object_change = diff_object(before, after)
        if not object_change:
            continue
        changed_objects.append(object_change)
        before_atoms = set(before.derived_atoms)
        after_atoms = set(after.derived_atoms)
        atom_changes["added"].extend(sorted(after_atoms - before_atoms))
        atom_changes["removed"].extend(sorted(before_atoms - after_atoms))

        previous_facets = _all_atoms_by_facet(before)
        current_facets = _all_atoms_by_facet(after)
        for facet in sorted(set(previous_facets) | set(current_facets)):
            before_values = set(previous_facets.get(facet, []))
            after_values = set(current_facets.get(facet, []))
            by_facet_added[facet].extend(sorted(after_values - before_values))
            by_facet_removed[facet].extend(sorted(before_values - after_values))

    return {
        "dataset": dataset,
        "platform": platform,
        "compared_at_utc": compared_at_utc,
        "previous_snapshot_date": previous_snapshot_date,
        "current_snapshot_date": current_snapshot_date,
        "counts": {
            "previous_objects": len(previous_map),
            "current_objects": len(current_map),
            "added_objects": len(added_objects),
            "removed_objects": len(removed_objects),
            "changed_objects": len(changed_objects),
            "added_atoms": len(atom_changes["added"]),
            "removed_atoms": len(atom_changes["removed"]),
        },
        "added_objects": added_objects,
        "removed_objects": removed_objects,
        "changed_objects": changed_objects,
        "atom_changes": {
            "added": sorted(atom_changes["added"]),
            "removed": sorted(atom_changes["removed"]),
            "by_facet": {
                "added": {key: sorted(values) for key, values in sorted(by_facet_added.items()) if values},
                "removed": {key: sorted(values) for key, values in sorted(by_facet_removed.items()) if values},
            },
        },
    }


def atom_to_permission_terms(atom: str) -> list[str]:
    if atom.startswith("aws:"):
        return [atom.split(":", 2)[2], atom]
    if atom.startswith("azure:"):
        return [atom.split(":", 2)[2], atom]
    if atom.startswith("gcp:permission:"):
        return [atom.split(":", 2)[2], atom]
    if atom.startswith("github:fgpat:"):
        _, _, domain, slug, level = atom.split(":", 4)
        return [f"{domain}:{slug}:{level}", f"{slug}:{level}", atom]
    if atom.startswith("github:token:"):
        _, _, key, level = atom.split(":", 3)
        return [f"{key}:{level}", atom]
    if atom.startswith("github:"):
        parts = atom.split(":")
        if len(parts) >= 4:
            return [":".join(parts[2:]), atom]
    return [atom]


def build_reverse_index(snapshot: DatasetSnapshot) -> dict[str, Any]:
    exact: dict[str, list[dict[str, str]]] = defaultdict(list)
    wildcard_atoms: list[dict[str, Any]] = []
    for obj in snapshot.objects:
        ref = {
            "stable_id": obj.stable_id,
            "display_name": obj.display_name,
            "source_url": obj.source_url,
        }
        for atom in obj.derived_atoms:
            exact[atom].append(ref)
            raw_terms = atom_to_permission_terms(atom)
            if any("*" in term or "?" in term for term in raw_terms):
                wildcard_atoms.append({"atom": atom, "terms": raw_terms, "object": ref})
    return {
        "dataset": snapshot.dataset,
        "platform": snapshot.platform,
        "generated_at_utc": snapshot.generated_at_utc,
        "exact": {key: sorted(value, key=lambda item: item["stable_id"]) for key, value in sorted(exact.items())},
        "wildcard_atoms": sorted(wildcard_atoms, key=lambda item: (item["atom"], item["object"]["stable_id"])),
    }
