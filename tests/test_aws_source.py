from __future__ import annotations

import json
from pathlib import Path

from managed_permissions_drift_catalog.config import AWS_MANAGED_POLICIES, Settings
from managed_permissions_drift_catalog.sources import aws
from managed_permissions_drift_catalog.storage import Storage

from .conftest import ensure_repo_layout


FIXTURES = Path(__file__).parent / "fixtures" / "aws"


def test_parse_aws_policy_list() -> None:
    html = (FIXTURES / "policy-list.html").read_text(encoding="utf-8")
    parsed = aws.parse_policy_list(html)
    assert parsed == [
        {
            "name": "ReadOnlyAccess",
            "url": "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html",
            "filename": "ReadOnlyAccess.html",
        }
    ]


def test_parse_aws_policy_page() -> None:
    html = (FIXTURES / "ReadOnlyAccess.html").read_text(encoding="utf-8")
    parsed = aws.parse_policy_page(
        html,
        "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html",
    )
    assert parsed["arn"] == "arn:aws:iam::aws:policy/ReadOnlyAccess"
    assert parsed["policy_version"] == "v182 (default)"
    assert parsed["policy_document"]["Statement"][0]["Action"] == ["s3:GetObject", "ec2:Describe*"]


def test_normalize_aws_snapshot(tmp_path: Path) -> None:
    root = ensure_repo_layout(tmp_path)
    storage = Storage(root)
    raw_dir = storage.raw_dir(AWS_MANAGED_POLICIES)
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "policies").mkdir(parents=True, exist_ok=True)
    (raw_dir / "policy-list.html").write_text((FIXTURES / "policy-list.html").read_text(encoding="utf-8"), encoding="utf-8")
    (raw_dir / "policies" / "ReadOnlyAccess.html").write_text(
        (FIXTURES / "ReadOnlyAccess.html").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    settings = Settings.from_root(root)
    snapshot = aws.normalize(settings, storage, "2026-04-17T00:00:00Z")
    assert snapshot.dataset == AWS_MANAGED_POLICIES
    assert len(snapshot.objects) == 1
    obj = snapshot.objects[0]
    assert "aws:allow_action:s3:GetObject" in obj.derived_atoms
    assert "aws:deny_action:organizations:LeaveOrganization" in obj.derived_atoms

