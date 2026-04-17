from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

from ..config import (
    GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS,
    GITHUB_FGPAT_PERMISSIONS,
    GITHUB_TOKEN_PERMISSIONS,
    Settings,
)
from ..normalize import build_object, build_snapshot
from ..storage import Storage
from ..utils import isoformat_utc, normalize_whitespace, sha256_json, slugify, stable_json_dumps

FGPAT_URL = "https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens"
WORKFLOW_SYNTAX_URL = "https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax"
ACTIONS_PERMISSIONS_URL = "https://docs.github.com/en/rest/actions/permissions"


def extract_next_data(html: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "lxml")
    script = soup.find("script", id="__NEXT_DATA__")
    if script is None or not script.string:
        raise ValueError("GitHub docs page is missing __NEXT_DATA__ payload")
    return json.loads(script.string)


def strip_html(text: str) -> str:
    return normalize_whitespace(BeautifulSoup(text, "lxml").get_text(" ", strip=True))


def _write_next_data(raw_dir: Path, filename: str, data: dict[str, Any]) -> None:
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / filename).write_text(stable_json_dumps(data), encoding="utf-8")


def fetch_fgpat(settings: Settings, storage: Storage, client: Any) -> dict[str, Any]:
    raw_dir = storage.raw_dir(GITHUB_FGPAT_PERMISSIONS)
    fetched_at_utc = isoformat_utc()
    response = client.get_text(FGPAT_URL, cache_path=raw_dir / "page.html")
    _write_next_data(raw_dir, "next-data.json", extract_next_data(response.text))
    return {"dataset": GITHUB_FGPAT_PERMISSIONS, "fetched_at_utc": fetched_at_utc}


def normalize_fgpat(settings: Settings, storage: Storage, fetched_at_utc: str) -> Any:
    raw_dir = storage.raw_dir(GITHUB_FGPAT_PERMISSIONS)
    next_data = json.loads((raw_dir / "next-data.json").read_text(encoding="utf-8"))
    page_props = next_data["props"]["pageProps"]
    current_version = page_props.get("currentVersion")
    apps_items = page_props["appsItems"]
    objects = []
    for item in apps_items.values():
        display_title = item.get("displayTitle") or item["title"]
        prefix = display_title.split(" permissions", 1)[0].strip().lower()
        domain = {
            "organization": "organization",
            "repository": "repository",
            "account": "account",
            "user": "user",
        }.get(prefix, prefix.replace(" ", "-"))
        title = item["title"]
        levels = sorted({entry["access"] for entry in item.get("permissions", []) if entry.get("access")})
        endpoint_strings = []
        for entry in item.get("permissions", []):
            suffix = " + additional permissions" if entry.get("additional-permissions") else ""
            endpoint_strings.append(
                f"{entry['verb'].upper()} {entry['requestPath']} -> {entry['access']}{suffix}"
            )
        stable_slug = slugify(title)
        objects.append(
            build_object(
                platform="github",
                dataset=GITHUB_FGPAT_PERMISSIONS,
                kind="permission_schema",
                stable_id=f"github-fgpat:{domain}:{stable_slug}",
                display_name=title,
                description=f"{display_title} permission schema",
                source_url=f"{FGPAT_URL}#{slugify(display_title.replace('\"', ''))}",
                source_version=current_version,
                source_revision=None,
                fetched_at_utc=fetched_at_utc,
                metadata={
                    "domain": domain,
                    "display_title": display_title,
                    "additional_permissions_required": any(
                        bool(entry.get("additional-permissions")) for entry in item.get("permissions", [])
                    ),
                    "endpoint_records": item.get("permissions", []),
                },
                grants_by_facet={
                    "levels": levels,
                    "endpoints": endpoint_strings,
                },
                restrictions_by_facet={},
                derived_atoms=[f"github:fgpat:{domain}:{stable_slug}:{level}" for level in levels],
                raw_hash=sha256_json(item),
            )
        )

    return build_snapshot(
        dataset=GITHUB_FGPAT_PERMISSIONS,
        platform="github",
        generated_at_utc=fetched_at_utc,
        source_urls=[FGPAT_URL],
        warnings=[],
        objects=objects,
    )


def fetch_token_permissions(settings: Settings, storage: Storage, client: Any) -> dict[str, Any]:
    raw_dir = storage.raw_dir(GITHUB_TOKEN_PERMISSIONS)
    fetched_at_utc = isoformat_utc()
    response = client.get_text(WORKFLOW_SYNTAX_URL, cache_path=raw_dir / "page.html")
    _write_next_data(raw_dir, "next-data.json", extract_next_data(response.text))
    return {"dataset": GITHUB_TOKEN_PERMISSIONS, "fetched_at_utc": fetched_at_utc}


def _parse_token_permissions(rendered_page: str) -> tuple[dict[str, list[str]], dict[str, str]]:
    soup = BeautifulSoup(rendered_page, "lxml")
    yaml_code = None
    for code in soup.select("pre > code"):
        text = code.get_text("", strip=False)
        if "permissions:" in text and "actions:" in text and "id-token:" in text:
            yaml_code = text
            break
    if yaml_code is None:
        raise ValueError("Failed to locate GITHUB_TOKEN permission YAML block")

    allowed_values: dict[str, list[str]] = {}
    for line in yaml_code.splitlines()[1:]:
        if ":" not in line:
            continue
        key, raw_values = line.strip().split(":", 1)
        allowed_values[key.strip()] = [value.strip() for value in raw_values.split("|") if value.strip()]

    descriptions: dict[str, str] = {}
    table = soup.find("table", attrs={"aria-labelledby": "permissions"})
    if table is None:
        raise ValueError("Failed to locate GITHUB_TOKEN permissions table")
    for row in table.select("tbody tr"):
        cells = row.find_all("td")
        if len(cells) != 2:
            continue
        key = cells[0].get_text(" ", strip=True).strip()
        descriptions[key] = normalize_whitespace(cells[1].get_text(" ", strip=True))
    return allowed_values, descriptions


def normalize_token_permissions(settings: Settings, storage: Storage, fetched_at_utc: str) -> Any:
    raw_dir = storage.raw_dir(GITHUB_TOKEN_PERMISSIONS)
    next_data = json.loads((raw_dir / "next-data.json").read_text(encoding="utf-8"))
    page_props = next_data["props"]["pageProps"]
    article_context = page_props["articleContext"]
    allowed_values, descriptions = _parse_token_permissions(article_context["renderedPage"])
    current_version = page_props["mainContext"].get("currentVersion")
    objects = []
    for key, values in sorted(allowed_values.items()):
        grant_levels = [value for value in values if value != "none"]
        objects.append(
            build_object(
                platform="github",
                dataset=GITHUB_TOKEN_PERMISSIONS,
                kind="permission_schema",
                stable_id=f"github-token:{key}",
                display_name=key,
                description=descriptions.get(key, ""),
                source_url=f"{WORKFLOW_SYNTAX_URL}#defining-access-for-the-github_token-scopes",
                source_version=current_version,
                source_revision=article_context.get("effectiveDate"),
                fetched_at_utc=fetched_at_utc,
                metadata={
                    "allowed_values": values,
                },
                grants_by_facet={"levels": grant_levels},
                restrictions_by_facet={},
                derived_atoms=[f"github:token:{key}:{value}" for value in grant_levels],
                raw_hash=sha256_json({"key": key, "values": values, "description": descriptions.get(key, "")}),
            )
        )
    return build_snapshot(
        dataset=GITHUB_TOKEN_PERMISSIONS,
        platform="github",
        generated_at_utc=fetched_at_utc,
        source_urls=[WORKFLOW_SYNTAX_URL],
        warnings=[],
        objects=objects,
    )


def fetch_actions_settings(settings: Settings, storage: Storage, client: Any) -> dict[str, Any]:
    raw_dir = storage.raw_dir(GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS)
    fetched_at_utc = isoformat_utc()
    response = client.get_text(ACTIONS_PERMISSIONS_URL, cache_path=raw_dir / "page.html")
    _write_next_data(raw_dir, "next-data.json", extract_next_data(response.text))
    return {"dataset": GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS, "fetched_at_utc": fetched_at_utc}


def _load_relevant_actions_operations(next_data: dict[str, Any]) -> list[dict[str, Any]]:
    operations = next_data["props"]["pageProps"]["restOperations"]
    targets = {
        "/orgs/{org}/actions/permissions": "org-actions-policy",
        "/repos/{owner}/{repo}/actions/permissions": "repo-actions-policy",
        "/orgs/{org}/actions/permissions/workflow": "org-workflow-defaults",
        "/repos/{owner}/{repo}/actions/permissions/workflow": "repo-workflow-defaults",
        "/orgs/{org}/actions/permissions/selected-actions": "org-selected-actions",
        "/repos/{owner}/{repo}/actions/permissions/selected-actions": "repo-selected-actions",
    }
    selected = []
    for operation in operations:
        if operation.get("verb") != "get":
            continue
        request_path = operation.get("requestPath")
        if request_path in targets:
            item = dict(operation)
            item["contract_id"] = targets[request_path]
            selected.append(item)
    if not selected:
        raise ValueError("Failed to locate GitHub Actions settings operations")
    return selected


def _operation_contract_values(operation: dict[str, Any]) -> tuple[dict[str, list[str]], list[str], str]:
    schema = {}
    code_examples = operation.get("codeExamples", [])
    if code_examples:
        schema = code_examples[0].get("response", {}).get("schema", {}) or {}
    properties = schema.get("properties", {})
    grants_by_facet: dict[str, list[str]] = {}
    atoms: list[str] = []
    contract_id = operation["contract_id"]
    atom_prefix = {
        "org-workflow-defaults": "github:workflow-default",
        "repo-workflow-defaults": "github:workflow-default",
        "org-actions-policy": "github:org-actions-policy",
        "repo-actions-policy": "github:repo-actions-policy",
        "org-selected-actions": "github:org-selected-actions",
        "repo-selected-actions": "github:repo-selected-actions",
    }[contract_id]
    for field_name, field_schema in properties.items():
        enum_values = field_schema.get("enum")
        if enum_values:
            grants_by_facet[field_name] = list(enum_values)
            atoms.extend(f"{atom_prefix}:{field_name}:{value}" for value in enum_values)
        elif field_schema.get("type") == "boolean":
            grants_by_facet[field_name] = ["false", "true"]
            atoms.extend(f"{atom_prefix}:{field_name}:false" for _ in [0])
            atoms.extend(f"{atom_prefix}:{field_name}:true" for _ in [0])
    return grants_by_facet, atoms, atom_prefix


def normalize_actions_settings(settings: Settings, storage: Storage, fetched_at_utc: str) -> Any:
    raw_dir = storage.raw_dir(GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS)
    next_data = json.loads((raw_dir / "next-data.json").read_text(encoding="utf-8"))
    page_props = next_data["props"]["pageProps"]
    operations = _load_relevant_actions_operations(next_data)
    objects = []
    for operation in operations:
        grants_by_facet, atoms, atom_prefix = _operation_contract_values(operation)
        objects.append(
            build_object(
                platform="github",
                dataset=GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS,
                kind="settings_contract",
                stable_id=f"github-actions-settings:{operation['contract_id']}",
                display_name=operation["title"],
                description=strip_html(operation.get("descriptionHTML", "")),
                source_url=f"{ACTIONS_PERMISSIONS_URL}#{slugify(operation['title'])}",
                source_version=page_props["mainContext"].get("currentVersion"),
                source_revision=None,
                fetched_at_utc=fetched_at_utc,
                metadata={
                    "request_path": operation["requestPath"],
                    "atom_prefix": atom_prefix,
                    "programmatic_access": operation.get("progAccess", {}),
                    "schema": operation.get("codeExamples", [{}])[0].get("response", {}).get("schema", {}),
                },
                grants_by_facet=grants_by_facet,
                restrictions_by_facet={},
                derived_atoms=atoms,
                raw_hash=sha256_json(operation),
            )
        )
    return build_snapshot(
        dataset=GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS,
        platform="github",
        generated_at_utc=fetched_at_utc,
        source_urls=[ACTIONS_PERMISSIONS_URL],
        warnings=[],
        objects=objects,
    )
