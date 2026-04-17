from __future__ import annotations

import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from ..config import GCP_PREDEFINED_ROLES, Settings
from ..normalize import build_object, build_snapshot
from ..storage import Storage
from ..utils import isoformat_utc, normalize_whitespace, sha256_json, stable_json_dumps

INDEX_URL = "https://docs.cloud.google.com/iam/docs/roles-permissions"
FILTER_JSON_URL = "https://docs.cloud.google.com/iam/json/role-permission-filter.json"
ROLES_API_URL = "https://iam.googleapis.com/v1/roles?view=FULL&pageSize=1000"


def parse_filter_index(payload: dict[str, Any]) -> dict[str, Any]:
    if "roles" not in payload or "services" not in payload:
        raise ValueError("Unexpected GCP role filter JSON shape")
    return payload


def parse_service_page(html: str, source_url: str) -> list[dict[str, Any]]:
    soup = BeautifulSoup(html, "lxml")
    items = []
    for row in soup.select("tbody.list tr"):
        description_cell = row.select_one("td.role-description")
        permissions_cell = row.select_one("td.role-permissions")
        if description_cell is None or permissions_cell is None:
            continue
        title_tag = description_cell.select_one("h4.role-title")
        code_tag = description_cell.find("code")
        if title_tag is None or code_tag is None:
            continue
        role_name = code_tag.get_text("", strip=True).replace("\u200b", "")
        role_id = role_name.split("/", 1)[1] if "/" in role_name else role_name
        description_lines = [
            normalize_whitespace(p.get_text(" ", strip=True))
            for p in description_cell.select("span.role-description p")
            if normalize_whitespace(p.get_text(" ", strip=True))
        ]
        stage_nodes = description_cell.select('[class*="launch-stage"]')
        stage = normalize_whitespace(" ".join(node.get_text(" ", strip=True) for node in stage_nodes)) or "GA"
        included_permissions: list[str] = []
        for child in permissions_cell.children:
            name = getattr(child, "name", None)
            if name == "p":
                code = child.find("code")
                if code is not None:
                    included_permissions.append(code.get_text("", strip=True).replace("\u200b", ""))
            elif name == "devsite-expandable":
                for code in child.select("ul li code"):
                    included_permissions.append(code.get_text("", strip=True).replace("\u200b", ""))
        items.append(
            {
                "name": role_name,
                "role_id": role_id,
                "title": normalize_whitespace(title_tag.get_text(" ", strip=True)),
                "description": " ".join(description_lines),
                "stage": stage,
                "includedPermissions": sorted(set(included_permissions)),
                "deleted": False,
                "source_url": f"{source_url}#{role_id}",
                "stage_inferred": not stage_nodes,
            }
        )
    return items


def _fetch_roles_api(settings: Settings, raw_dir: Path) -> int:
    access_token = os.getenv("MANAGED_PERMISSIONS_GCP_ACCESS_TOKEN") or os.getenv("GOOGLE_OAUTH_ACCESS_TOKEN")
    if not access_token:
        raise RuntimeError("Authenticated GCP fallback requested but no access token is available")

    roles: list[dict[str, Any]] = []
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {access_token}",
            "User-Agent": settings.user_agent,
        }
    )
    next_page_token: str | None = None
    while True:
        url = ROLES_API_URL
        if next_page_token:
            url = f"{url}&pageToken={next_page_token}"
        response = session.get(url, timeout=settings.http_timeout_seconds)
        response.raise_for_status()
        payload = response.json()
        roles.extend(payload.get("roles", []))
        next_page_token = payload.get("nextPageToken")
        if not next_page_token:
            break
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "authenticated-roles.json").write_text(stable_json_dumps(roles), encoding="utf-8")
    return len(roles)


def fetch(settings: Settings, storage: Storage, client: Any) -> dict[str, Any]:
    raw_dir = storage.raw_dir(GCP_PREDEFINED_ROLES)
    fetched_at_utc = isoformat_utc()
    if settings.gcp_enable_authenticated_fallback:
        count = _fetch_roles_api(settings, raw_dir)
        return {
            "dataset": GCP_PREDEFINED_ROLES,
            "fetched_at_utc": fetched_at_utc,
            "object_candidates": count,
            "mode": "authenticated-api",
        }

    filter_response = client.get_text(FILTER_JSON_URL, cache_path=raw_dir / "role-permission-filter.json")
    payload = parse_filter_index(json.loads(filter_response.text))
    service_urls = sorted({urljoin(INDEX_URL, item["url"]) for item in payload["services"]})
    (raw_dir / "service-urls.json").write_text(stable_json_dumps(service_urls), encoding="utf-8")

    def fetch_service(url: str) -> None:
        filename = f"{Path(url).name}.html"
        client.get_text(url, cache_path=raw_dir / "services" / filename)

    with ThreadPoolExecutor(max_workers=settings.max_workers) as pool:
        futures = [pool.submit(fetch_service, url) for url in service_urls]
        for future in as_completed(futures):
            future.result()

    return {
        "dataset": GCP_PREDEFINED_ROLES,
        "fetched_at_utc": fetched_at_utc,
        "object_candidates": len(service_urls),
        "mode": "docs",
    }


def normalize(settings: Settings, storage: Storage, fetched_at_utc: str) -> Any:
    raw_dir = storage.raw_dir(GCP_PREDEFINED_ROLES)
    warnings: list[str] = []
    source_urls = [FILTER_JSON_URL]
    objects = []
    api_path = raw_dir / "authenticated-roles.json"
    if settings.gcp_enable_authenticated_fallback and api_path.exists():
        warnings.append("Using authenticated GCP roles API fallback instead of public docs.")
        role_entries = json.loads(api_path.read_text(encoding="utf-8"))
        source_urls = [ROLES_API_URL]
        for role in role_entries:
            objects.append(
                build_object(
                    platform="gcp",
                    dataset=GCP_PREDEFINED_ROLES,
                    kind="role",
                    stable_id=role["name"],
                    display_name=role.get("title", role["name"]),
                    description=role.get("description", ""),
                    source_url=ROLES_API_URL,
                    source_version=None,
                    source_revision=role.get("etag"),
                    fetched_at_utc=fetched_at_utc,
                    metadata={
                        "stage": role.get("stage"),
                        "deleted": role.get("deleted", False),
                    },
                    grants_by_facet={"included_permissions": role.get("includedPermissions", [])},
                    restrictions_by_facet={},
                    derived_atoms=[f"gcp:permission:{item}" for item in role.get("includedPermissions", [])],
                    raw_hash=sha256_json(role),
                )
            )
    else:
        payload = parse_filter_index(json.loads((raw_dir / "role-permission-filter.json").read_text(encoding="utf-8")))
        service_urls = json.loads((raw_dir / "service-urls.json").read_text(encoding="utf-8"))
        source_urls.extend(service_urls)
        seen: set[str] = set()
        for service_url in service_urls:
            filename = f"{Path(service_url).name}.html"
            html_path = raw_dir / "services" / filename
            if not html_path.exists():
                raise FileNotFoundError(f"Missing cached GCP service page: {html_path}")
            for parsed in parse_service_page(html_path.read_text(encoding="utf-8"), service_url):
                if parsed["name"] in seen:
                    continue
                seen.add(parsed["name"])
                objects.append(
                    build_object(
                        platform="gcp",
                        dataset=GCP_PREDEFINED_ROLES,
                        kind="role",
                        stable_id=parsed["name"],
                        display_name=parsed["title"],
                        description=parsed["description"],
                        source_url=parsed["source_url"],
                        source_version=None,
                        source_revision=None,
                        fetched_at_utc=fetched_at_utc,
                        metadata={
                            "stage": parsed["stage"],
                            "stage_inferred": parsed["stage_inferred"],
                            "deleted": parsed["deleted"],
                        },
                        grants_by_facet={"included_permissions": parsed["includedPermissions"]},
                        restrictions_by_facet={},
                        derived_atoms=[f"gcp:permission:{item}" for item in parsed["includedPermissions"]],
                        raw_hash=sha256_json(parsed),
                    )
                )
        if len(objects) < len(payload["roles"]) // 2:
            warnings.append("Parsed fewer GCP roles than expected from the docs index; check parser health.")

    return build_snapshot(
        dataset=GCP_PREDEFINED_ROLES,
        platform="gcp",
        generated_at_utc=fetched_at_utc,
        source_urls=source_urls,
        warnings=warnings,
        objects=objects,
    )
