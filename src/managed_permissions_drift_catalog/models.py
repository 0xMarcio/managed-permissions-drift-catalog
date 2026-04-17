from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .utils import canonicalize, unique_sorted


@dataclass(slots=True)
class NormalizedObject:
    platform: str
    dataset: str
    kind: str
    stable_id: str
    display_name: str
    description: str
    source_url: str
    source_version: str | None
    source_revision: str | None
    fetched_at_utc: str
    metadata: dict[str, Any] = field(default_factory=dict)
    grants_by_facet: dict[str, list[str]] = field(default_factory=dict)
    restrictions_by_facet: dict[str, list[str]] = field(default_factory=dict)
    derived_atoms: list[str] = field(default_factory=list)
    raw_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "platform": self.platform,
            "dataset": self.dataset,
            "kind": self.kind,
            "stable_id": self.stable_id,
            "display_name": self.display_name,
            "description": self.description,
            "source_url": self.source_url,
            "source_version": self.source_version,
            "source_revision": self.source_revision,
            "fetched_at_utc": self.fetched_at_utc,
            "metadata": canonicalize(self.metadata),
            "grants_by_facet": {key: unique_sorted(values) for key, values in sorted(self.grants_by_facet.items())},
            "restrictions_by_facet": {
                key: unique_sorted(values) for key, values in sorted(self.restrictions_by_facet.items())
            },
            "derived_atoms": unique_sorted(self.derived_atoms),
            "raw_hash": self.raw_hash,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "NormalizedObject":
        return cls(
            platform=data["platform"],
            dataset=data["dataset"],
            kind=data["kind"],
            stable_id=data["stable_id"],
            display_name=data["display_name"],
            description=data.get("description", ""),
            source_url=data["source_url"],
            source_version=data.get("source_version"),
            source_revision=data.get("source_revision"),
            fetched_at_utc=data["fetched_at_utc"],
            metadata=data.get("metadata", {}),
            grants_by_facet=data.get("grants_by_facet", {}),
            restrictions_by_facet=data.get("restrictions_by_facet", {}),
            derived_atoms=data.get("derived_atoms", []),
            raw_hash=data.get("raw_hash", ""),
        )


@dataclass(slots=True)
class DatasetSnapshot:
    dataset: str
    platform: str
    generated_at_utc: str
    source_urls: list[str]
    warnings: list[str]
    objects: list[NormalizedObject]

    def to_dict(self) -> dict[str, Any]:
        return {
            "dataset": self.dataset,
            "platform": self.platform,
            "generated_at_utc": self.generated_at_utc,
            "source_urls": sorted(self.source_urls),
            "warnings": sorted(self.warnings),
            "object_count": len(self.objects),
            "objects": [obj.to_dict() for obj in sorted(self.objects, key=lambda item: item.stable_id)],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "DatasetSnapshot":
        return cls(
            dataset=data["dataset"],
            platform=data["platform"],
            generated_at_utc=data["generated_at_utc"],
            source_urls=data.get("source_urls", []),
            warnings=data.get("warnings", []),
            objects=[NormalizedObject.from_dict(item) for item in data.get("objects", [])],
        )

