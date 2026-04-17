from __future__ import annotations

from typing import Any, Iterable

from .models import DatasetSnapshot, NormalizedObject
from .utils import canonicalize, normalize_whitespace, unique_sorted


def normalize_facet_map(value: dict[str, Iterable[str]]) -> dict[str, list[str]]:
    normalized: dict[str, list[str]] = {}
    for facet, items in value.items():
        normalized[facet] = unique_sorted(str(item).strip() for item in items if str(item).strip())
    return {key: normalized[key] for key in sorted(normalized)}


def build_object(**kwargs: Any) -> NormalizedObject:
    obj = NormalizedObject(**kwargs)
    obj.display_name = normalize_whitespace(obj.display_name)
    obj.description = normalize_whitespace(obj.description)
    obj.metadata = canonicalize(obj.metadata)
    obj.grants_by_facet = normalize_facet_map(obj.grants_by_facet)
    obj.restrictions_by_facet = normalize_facet_map(obj.restrictions_by_facet)
    obj.derived_atoms = unique_sorted(obj.derived_atoms)
    return obj


def build_snapshot(
    *,
    dataset: str,
    platform: str,
    generated_at_utc: str,
    source_urls: list[str],
    warnings: list[str],
    objects: list[NormalizedObject],
) -> DatasetSnapshot:
    return DatasetSnapshot(
        dataset=dataset,
        platform=platform,
        generated_at_utc=generated_at_utc,
        source_urls=sorted(set(source_urls)),
        warnings=sorted(set(warnings)),
        objects=sorted(objects, key=lambda item: item.stable_id),
    )

