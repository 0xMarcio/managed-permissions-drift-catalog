from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Any

from .models import DatasetSnapshot
from .utils import read_text, stable_json_dumps


class Storage:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.data_dir = root / "data"
        self.docs_dir = root / "docs"

    def latest_snapshot_path(self, dataset: str) -> Path:
        return self.data_dir / "latest" / f"{dataset}.json"

    def snapshot_path(self, dataset: str, run_date: str) -> Path:
        return self.data_dir / "snapshots" / dataset / f"{run_date}.json.gz"

    def diff_path(self, run_date: str, dataset: str) -> Path:
        return self.data_dir / "diffs" / run_date / f"{dataset}.json"

    def reverse_index_path(self, dataset: str) -> Path:
        return self.data_dir / "reverse-index" / f"{dataset}.json"

    def summary_path(self, run_date: str) -> Path:
        return self.data_dir / "summaries" / f"{run_date}.json"

    def run_manifest_path(self, run_date: str) -> Path:
        return self.data_dir / "runs" / f"{run_date}.json"

    def raw_dir(self, dataset: str) -> Path:
        return self.data_dir / "raw" / "latest" / dataset

    def docs_daily_path(self, run_date: str) -> Path:
        return self.docs_dir / "daily" / f"{run_date}.md"

    def docs_platform_path(self, platform: str) -> Path:
        return self.docs_dir / "platforms" / f"{platform}.md"

    def docs_index_path(self) -> Path:
        return self.docs_dir / "index.md"

    def read_snapshot(self, dataset: str) -> DatasetSnapshot | None:
        path = self.latest_snapshot_path(dataset)
        if not path.exists():
            return None
        return DatasetSnapshot.from_dict(json.loads(read_text(path)))

    def read_snapshot_from_path(self, path: Path) -> DatasetSnapshot:
        if path.suffix == ".gz":
            data = json.loads(gzip.decompress(path.read_bytes()).decode("utf-8"))
        else:
            data = json.loads(read_text(path))
        return DatasetSnapshot.from_dict(data)

    def previous_snapshot(self, dataset: str, *, exclude_date: str | None = None) -> tuple[str, DatasetSnapshot] | None:
        snapshot_dir = self.data_dir / "snapshots" / dataset
        if not snapshot_dir.exists():
            return None
        candidates = sorted(snapshot_dir.glob("*.json.gz"))
        filtered: list[Path] = []
        for path in candidates:
            if exclude_date and path.name == f"{exclude_date}.json.gz":
                continue
            filtered.append(path)
        if not filtered:
            return None
        chosen = filtered[-1]
        return chosen.stem.replace(".json", ""), self.read_snapshot_from_path(chosen)

    def write_text_if_changed(self, path: Path, content: str) -> bool:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and path.read_text(encoding="utf-8") == content:
            return False
        path.write_text(content, encoding="utf-8")
        return True

    def write_json_if_changed(self, path: Path, data: Any) -> bool:
        return self.write_text_if_changed(path, stable_json_dumps(data))

    def write_gzip_json_if_changed(self, path: Path, data: Any) -> bool:
        path.parent.mkdir(parents=True, exist_ok=True)
        content = stable_json_dumps(data).encode("utf-8")
        payload = gzip.compress(content, mtime=0)
        if path.exists() and path.read_bytes() == payload:
            return False
        path.write_bytes(payload)
        return True

