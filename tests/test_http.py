from __future__ import annotations

from pathlib import Path

from managed_permissions_drift_catalog.http import HttpClient


class _FakeResponse:
    def __init__(self, *, status_code: int, text: str = "", headers: dict[str, str] | None = None, url: str = "https://example.test") -> None:
        self.status_code = status_code
        self.text = text
        self.headers = headers or {}
        self.url = url

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError(f"unexpected status {self.status_code}")


def test_get_text_sanitizes_cached_304_content(tmp_path: Path, monkeypatch) -> None:
    google_token = "AIza" + ("A" * 35)
    cache_path = tmp_path / "cached.html"
    cache_path.write_text(f"before {google_token} after", encoding="utf-8")

    client = HttpClient(user_agent="test-agent")

    def fake_get(url: str, *, headers: dict[str, str], timeout: int) -> _FakeResponse:
        assert url == "https://example.test"
        assert isinstance(headers, dict)
        assert timeout == 30
        return _FakeResponse(status_code=304, headers={})

    monkeypatch.setattr(client.session, "get", fake_get)

    response = client.get_text(
        "https://example.test",
        cache_path=cache_path,
        text_transform=lambda text: text.replace(google_token, "GOOGLE_API_KEY_REDACTED"),
    )

    assert response.from_cache is True
    assert response.status_code == 304
    assert response.text == "before GOOGLE_API_KEY_REDACTED after"
    assert cache_path.read_text(encoding="utf-8") == "before GOOGLE_API_KEY_REDACTED after"


def test_get_text_sanitizes_fresh_response_before_write(tmp_path: Path, monkeypatch) -> None:
    cache_path = tmp_path / "fresh.html"
    client = HttpClient(user_agent="test-agent")
    stripe_token = "pk_live_" + ("A" * 40)

    def fake_get(url: str, *, headers: dict[str, str], timeout: int) -> _FakeResponse:
        assert url == "https://example.test"
        assert isinstance(headers, dict)
        assert timeout == 30
        return _FakeResponse(status_code=200, text=stripe_token, headers={}, url=url)

    monkeypatch.setattr(client.session, "get", fake_get)

    response = client.get_text(
        "https://example.test",
        cache_path=cache_path,
        text_transform=lambda text: text.replace(stripe_token, "STRIPE_PUBLISHABLE_KEY_REDACTED"),
    )

    assert response.from_cache is False
    assert response.status_code == 200
    assert response.text == "STRIPE_PUBLISHABLE_KEY_REDACTED"
    assert cache_path.read_text(encoding="utf-8") == "STRIPE_PUBLISHABLE_KEY_REDACTED"
