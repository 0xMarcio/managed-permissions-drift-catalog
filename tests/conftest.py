from __future__ import annotations

from pathlib import Path


def ensure_repo_layout(root: Path) -> Path:
    for relative in [
        "data/raw/latest",
        "data/latest",
        "data/snapshots",
        "data/diffs",
        "data/reverse-index",
        "data/summaries",
        "data/runs",
        "docs/daily",
        "docs/platforms",
    ]:
        (root / relative).mkdir(parents=True, exist_ok=True)
    return root

