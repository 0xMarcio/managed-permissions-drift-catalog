from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any, Iterable


JSONValue = dict[str, Any] | list[Any] | str | int | float | bool | None

NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
MULTISPACE_RE = re.compile(r"\s+")


def utc_now() -> datetime:
    return datetime.now(UTC)


def utc_today() -> date:
    return utc_now().date()


def isoformat_utc(value: datetime | None = None) -> str:
    current = value or utc_now()
    return current.astimezone(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalize_whitespace(value: str | None) -> str:
    if not value:
        return ""
    return MULTISPACE_RE.sub(" ", value).strip()


def slugify(value: str) -> str:
    lowered = normalize_whitespace(value).lower()
    lowered = NON_ALNUM_RE.sub("-", lowered)
    return lowered.strip("-")


def stable_json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_text(stable_json_dumps(value))


def unique_sorted(values: Iterable[str]) -> list[str]:
    return sorted({value for value in values if value})


def listify(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def canonicalize(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: canonicalize(value[key]) for key in sorted(value)}
    if isinstance(value, list):
        canonical_items = [canonicalize(item) for item in value]
        if all(isinstance(item, (str, int, float, bool)) or item is None for item in canonical_items):
            return sorted(canonical_items, key=lambda item: json.dumps(item, sort_keys=True))
        return sorted(canonical_items, key=lambda item: json.dumps(item, ensure_ascii=False, sort_keys=True))
    if isinstance(value, str):
        return value.strip()
    return value


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def maybe_read_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    return read_json(path)


def getenv_flag(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}

