from __future__ import annotations

import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from ..config import AZURE_BUILT_IN_ROLES, Settings
from ..normalize import build_object, build_snapshot
from ..storage import Storage
from ..utils import isoformat_utc, listify, normalize_whitespace, sha256_json, slugify, stable_json_dumps

LANDING_URL = "https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles"
ROLE_DEFINITIONS_GUIDANCE_URL = "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions-list"


def parse_landing_categories(html: str) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    categories: set[str] = set()
    for anchor in soup.select("table a[href]"):
        href = anchor.get("href", "")
        if "built-in-roles/" not in href:
            continue
        categories.add(urljoin(LANDING_URL, href.split("#", 1)[0]))
    if not categories:
        raise ValueError("Azure landing page parser found no category links")
    return sorted(categories)


def parse_category_page(html: str, source_url: str) -> list[dict[str, Any]]:
    soup = BeautifulSoup(html, "lxml")
    blocks = []
    for code in soup.select("pre > code.lang-json"):
        role_definition = json.loads(code.get_text("\n", strip=True))
        blocks.append({"source_url": source_url, "role_definition": role_definition})
    if not blocks:
        raise ValueError(f"Azure category page contained no role JSON blocks: {source_url}")
    return blocks


def _role_permission_values(role_definition: dict[str, Any], key: str) -> list[str]:
    values: list[str] = []
    for permission_block in role_definition.get("permissions", []):
        values.extend(str(item) for item in listify(permission_block.get(key)) if item)
    return values


def _cli_fetch_role_definitions(raw_dir: Path) -> int:
    result = subprocess.run(
        ["az", "role", "definition", "list", "--output", "json"],
        check=True,
        capture_output=True,
        text=True,
    )
    raw_dir.mkdir(parents=True, exist_ok=True)
    payload = json.loads(result.stdout)
    (raw_dir / "azure-cli-role-definitions.json").write_text(stable_json_dumps(payload), encoding="utf-8")
    return len(payload)


def fetch(settings: Settings, storage: Storage, client: Any) -> dict[str, Any]:
    raw_dir = storage.raw_dir(AZURE_BUILT_IN_ROLES)
    fetched_at_utc = isoformat_utc()
    if settings.azure_enable_cli_fallback:
        count = _cli_fetch_role_definitions(raw_dir)
        return {
            "dataset": AZURE_BUILT_IN_ROLES,
            "fetched_at_utc": fetched_at_utc,
            "object_candidates": count,
            "mode": "azure-cli",
        }

    landing_response = client.get_text(LANDING_URL, cache_path=raw_dir / "landing.html")
    categories = parse_landing_categories(landing_response.text)
    (raw_dir / "categories.json").write_text(stable_json_dumps(categories), encoding="utf-8")

    def fetch_category(url: str) -> None:
        filename = f"{Path(url).name}.html"
        client.get_text(url, cache_path=raw_dir / "categories" / filename)

    with ThreadPoolExecutor(max_workers=settings.max_workers) as pool:
        futures = [pool.submit(fetch_category, url) for url in categories]
        for future in as_completed(futures):
            future.result()

    return {
        "dataset": AZURE_BUILT_IN_ROLES,
        "fetched_at_utc": fetched_at_utc,
        "object_candidates": len(categories),
        "mode": "docs",
    }


def normalize(settings: Settings, storage: Storage, fetched_at_utc: str) -> Any:
    raw_dir = storage.raw_dir(AZURE_BUILT_IN_ROLES)
    objects = []
    warnings: list[str] = []
    source_urls = [LANDING_URL]
    cli_path = raw_dir / "azure-cli-role-definitions.json"
    if settings.azure_enable_cli_fallback and cli_path.exists():
        role_definitions = json.loads(cli_path.read_text(encoding="utf-8"))
        raw_items = [{"source_url": ROLE_DEFINITIONS_GUIDANCE_URL, "role_definition": item} for item in role_definitions]
        warnings.append("Using Azure CLI authenticated fallback instead of docs scraping.")
        source_urls = [ROLE_DEFINITIONS_GUIDANCE_URL]
    else:
        landing_html = (raw_dir / "landing.html").read_text(encoding="utf-8")
        categories = parse_landing_categories(landing_html)
        raw_items = []
        for category_url in categories:
            filename = f"{Path(category_url).name}.html"
            html_path = raw_dir / "categories" / filename
            if not html_path.exists():
                raise FileNotFoundError(f"Missing cached Azure category page: {html_path}")
            raw_items.extend(parse_category_page(html_path.read_text(encoding="utf-8"), category_url))
        source_urls.extend(categories)

    seen_ids: set[str] = set()
    for item in raw_items:
        role_definition = item["role_definition"]
        role_type = role_definition.get("roleType")
        if role_type and role_type != "BuiltInRole":
            continue
        role_name = role_definition.get("roleName") or role_definition.get("properties", {}).get("roleName")
        role_id = str(role_definition.get("name") or "").strip()
        if not role_id and role_definition.get("id"):
            role_id = str(role_definition["id"]).rstrip("/").split("/")[-1]
        if not role_id or role_id in seen_ids:
            continue
        seen_ids.add(role_id)
        actions = _role_permission_values(role_definition, "actions")
        data_actions = _role_permission_values(role_definition, "dataActions")
        not_actions = _role_permission_values(role_definition, "notActions")
        not_data_actions = _role_permission_values(role_definition, "notDataActions")
        atoms = [f"azure:action:{value}" for value in actions]
        atoms.extend(f"azure:data_action:{value}" for value in data_actions)
        atoms.extend(f"azure:not_action:{value}" for value in not_actions)
        atoms.extend(f"azure:not_data_action:{value}" for value in not_data_actions)
        objects.append(
            build_object(
                platform="azure",
                dataset=AZURE_BUILT_IN_ROLES,
                kind="role",
                stable_id=role_id,
                display_name=role_name or role_id,
                description=role_definition.get("description", ""),
                source_url=f"{item['source_url']}#{slugify(role_name or role_id)}",
                source_version=None,
                source_revision=None,
                fetched_at_utc=fetched_at_utc,
                metadata={
                    "assignable_scopes": role_definition.get("assignableScopes", []),
                    "role_type": role_type,
                    "permission_block_count": len(role_definition.get("permissions", [])),
                    "raw_role_definition": role_definition,
                },
                grants_by_facet={
                    "actions": actions,
                    "data_actions": data_actions,
                },
                restrictions_by_facet={
                    "not_actions": not_actions,
                    "not_data_actions": not_data_actions,
                },
                derived_atoms=atoms,
                raw_hash=sha256_json(role_definition),
            )
        )

    return build_snapshot(
        dataset=AZURE_BUILT_IN_ROLES,
        platform="azure",
        generated_at_utc=fetched_at_utc,
        source_urls=source_urls,
        warnings=warnings,
        objects=objects,
    )

