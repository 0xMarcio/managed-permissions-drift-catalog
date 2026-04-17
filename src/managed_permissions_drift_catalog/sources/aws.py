from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from ..config import AWS_MANAGED_POLICIES, Settings
from ..normalize import build_object, build_snapshot
from ..storage import Storage
from ..utils import isoformat_utc, listify, normalize_whitespace, sha256_json, stable_json_dumps

POLICY_LIST_URL = "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html"


def parse_policy_list(html: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "lxml")
    policies: list[dict[str, str]] = []
    seen: set[str] = set()
    for anchor in soup.select("div.highlights a[href]"):
        href = anchor.get("href", "")
        if not href.endswith(".html"):
            continue
        url = urljoin(POLICY_LIST_URL, href)
        name = normalize_whitespace(anchor.get_text(" ", strip=True))
        if not name or url in seen:
            continue
        seen.add(url)
        policies.append({"name": name, "url": url, "filename": Path(url).name})
    if not policies:
        raise ValueError("AWS policy list parser found no policy links")
    return sorted(policies, key=lambda item: item["name"])


def parse_policy_page(html: str, source_url: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "lxml")
    title_tag = soup.find("h1")
    if title_tag is None:
        raise ValueError(f"AWS policy page is missing h1: {source_url}")
    name = normalize_whitespace(title_tag.get_text(" ", strip=True))

    paragraphs = []
    for element in title_tag.find_all_next():
        if getattr(element, "name", None) == "h2":
            break
        if getattr(element, "name", None) == "p":
            text = normalize_whitespace(element.get_text(" ", strip=True))
            if text:
                paragraphs.append(text)
    description = paragraphs[0] if paragraphs else ""

    details: dict[str, str] = {}
    for item in soup.select("div.itemizedlist li"):
        bold = item.find("b")
        if bold is None:
            continue
        label = normalize_whitespace(bold.get_text(" ", strip=True)).rstrip(":").lower()
        text = normalize_whitespace(item.get_text(" ", strip=True))
        value = text.split(":", 1)[1].strip() if ":" in text else ""
        details[label] = value

    version = ""
    for paragraph in soup.find_all("p"):
        text = normalize_whitespace(paragraph.get_text(" ", strip=True))
        if text.lower().startswith("policy version:"):
            version = text.split(":", 1)[1].strip()
            break

    pre = soup.find("pre")
    if pre is None:
        raise ValueError(f"AWS policy page is missing JSON policy document: {source_url}")
    code_block = pre.find("code") or pre
    policy_document = json.loads(code_block.get_text("", strip=False))
    return {
        "name": name,
        "description": description,
        "arn": details.get("arn"),
        "created_time": details.get("creation time"),
        "edited_time": details.get("edited time"),
        "policy_version": version,
        "policy_document": policy_document,
        "source_url": source_url,
    }


def _iter_policy_files(raw_dir: Path) -> list[Path]:
    policies_dir = raw_dir / "policies"
    return sorted(policies_dir.glob("*.html"))


def fetch(settings: Settings, storage: Storage, client: Any) -> dict[str, Any]:
    raw_dir = storage.raw_dir(AWS_MANAGED_POLICIES)
    fetched_at_utc = isoformat_utc()
    list_response = client.get_text(POLICY_LIST_URL, cache_path=raw_dir / "policy-list.html")
    policy_entries = parse_policy_list(list_response.text)
    (raw_dir / "policy-index.json").write_text(stable_json_dumps(policy_entries), encoding="utf-8")

    def fetch_policy(entry: dict[str, str]) -> None:
        client.get_text(entry["url"], cache_path=raw_dir / "policies" / entry["filename"])

    with ThreadPoolExecutor(max_workers=settings.max_workers) as pool:
        futures = [pool.submit(fetch_policy, entry) for entry in policy_entries]
        for future in as_completed(futures):
            future.result()

    return {
        "dataset": AWS_MANAGED_POLICIES,
        "fetched_at_utc": fetched_at_utc,
        "object_candidates": len(policy_entries),
    }


def normalize(settings: Settings, storage: Storage, fetched_at_utc: str) -> Any:
    raw_dir = storage.raw_dir(AWS_MANAGED_POLICIES)
    list_html = (raw_dir / "policy-list.html").read_text(encoding="utf-8")
    policy_entries = parse_policy_list(list_html)
    objects = []
    for entry in policy_entries:
        html_path = raw_dir / "policies" / entry["filename"]
        if not html_path.exists():
            raise FileNotFoundError(f"Missing cached AWS policy page: {html_path}")
        parsed = parse_policy_page(html_path.read_text(encoding="utf-8"), entry["url"])
        grants = {"allow_actions": []}
        restrictions = {
            "allow_not_actions": [],
            "deny_actions": [],
            "deny_not_actions": [],
        }
        atoms: list[str] = []
        statements = listify(parsed["policy_document"].get("Statement"))
        has_conditions = False
        has_non_wildcard_resource_scopes = False
        for statement in statements:
            if not isinstance(statement, dict):
                continue
            has_conditions = has_conditions or "Condition" in statement
            resource_values = listify(statement.get("Resource")) + listify(statement.get("NotResource"))
            if any(value != "*" for value in resource_values if isinstance(value, str)):
                has_non_wildcard_resource_scopes = True

            effect = str(statement.get("Effect", "")).lower()
            actions = [str(item) for item in listify(statement.get("Action")) if item]
            not_actions = [str(item) for item in listify(statement.get("NotAction")) if item]
            if effect == "allow":
                grants["allow_actions"].extend(actions)
                restrictions["allow_not_actions"].extend(not_actions)
                atoms.extend(f"aws:allow_action:{item}" for item in actions)
                atoms.extend(f"aws:allow_notaction:{item}" for item in not_actions)
            elif effect == "deny":
                restrictions["deny_actions"].extend(actions)
                restrictions["deny_not_actions"].extend(not_actions)
                atoms.extend(f"aws:deny_action:{item}" for item in actions)
                atoms.extend(f"aws:deny_notaction:{item}" for item in not_actions)

        objects.append(
            build_object(
                platform="aws",
                dataset=AWS_MANAGED_POLICIES,
                kind="policy",
                stable_id=parsed["arn"] or parsed["name"],
                display_name=parsed["name"],
                description=parsed["description"],
                source_url=parsed["source_url"],
                source_version=parsed["policy_version"],
                source_revision=parsed["edited_time"],
                fetched_at_utc=fetched_at_utc,
                metadata={
                    "arn": parsed["arn"],
                    "created_time": parsed["created_time"],
                    "edited_time": parsed["edited_time"],
                    "statement_count": len(statements),
                    "has_conditions": has_conditions,
                    "has_non_wildcard_resource_scopes": has_non_wildcard_resource_scopes,
                    "policy_document": parsed["policy_document"],
                },
                grants_by_facet=grants,
                restrictions_by_facet=restrictions,
                derived_atoms=atoms,
                raw_hash=sha256_json(parsed),
            )
        )

    return build_snapshot(
        dataset=AWS_MANAGED_POLICIES,
        platform="aws",
        generated_at_utc=fetched_at_utc,
        source_urls=[POLICY_LIST_URL],
        warnings=[],
        objects=objects,
    )
