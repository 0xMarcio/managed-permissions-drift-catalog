from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests

from .utils import maybe_read_json, stable_json_dumps


class HttpError(RuntimeError):
    """Raised when an HTTP fetch fails."""


@dataclass(slots=True)
class CachedResponse:
    url: str
    text: str
    status_code: int
    headers: dict[str, str]
    from_cache: bool = False


class HttpClient:
    def __init__(self, *, user_agent: str, timeout_seconds: int = 30, max_retries: int = 3) -> None:
        self.user_agent = user_agent
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})

    def get_text(self, url: str, *, cache_path: Path | None = None) -> CachedResponse:
        conditional_headers: dict[str, str] = {}
        meta_path = cache_path.with_suffix(cache_path.suffix + ".http.json") if cache_path else None
        cached_meta = maybe_read_json(meta_path) if meta_path else None
        if cached_meta:
            if cached_meta.get("etag"):
                conditional_headers["If-None-Match"] = cached_meta["etag"]
            if cached_meta.get("last_modified"):
                conditional_headers["If-Modified-Since"] = cached_meta["last_modified"]

        last_error: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(
                    url,
                    headers=conditional_headers,
                    timeout=self.timeout_seconds,
                )
                if response.status_code == 304 and cache_path and cache_path.exists():
                    return CachedResponse(
                        url=url,
                        text=cache_path.read_text(encoding="utf-8"),
                        status_code=304,
                        headers=dict(response.headers),
                        from_cache=True,
                    )
                response.raise_for_status()
                text = response.text
                if cache_path:
                    cache_path.parent.mkdir(parents=True, exist_ok=True)
                    cache_path.write_text(text, encoding="utf-8")
                    assert meta_path is not None
                    meta = {
                        "url": url,
                        "etag": response.headers.get("ETag"),
                        "last_modified": response.headers.get("Last-Modified"),
                        "status_code": response.status_code,
                    }
                    meta_path.write_text(stable_json_dumps(meta), encoding="utf-8")
                return CachedResponse(
                    url=str(response.url),
                    text=text,
                    status_code=response.status_code,
                    headers=dict(response.headers),
                    from_cache=False,
                )
            except requests.RequestException as exc:
                last_error = exc
                if attempt + 1 >= self.max_retries:
                    break
                time.sleep(2**attempt)

        raise HttpError(f"Failed to fetch {url}: {last_error}") from last_error

