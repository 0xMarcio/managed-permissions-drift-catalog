from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .utils import getenv_flag, isoformat_utc, utc_today


AWS_MANAGED_POLICIES = "aws-managed-policies"
AZURE_BUILT_IN_ROLES = "azure-built-in-roles"
GCP_PREDEFINED_ROLES = "gcp-predefined-roles"
GITHUB_FGPAT_PERMISSIONS = "github-fgpat-permissions"
GITHUB_TOKEN_PERMISSIONS = "github-token-permissions"
GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS = "github-actions-default-workflow-settings"

DATASETS = [
    AWS_MANAGED_POLICIES,
    AZURE_BUILT_IN_ROLES,
    GCP_PREDEFINED_ROLES,
    GITHUB_FGPAT_PERMISSIONS,
    GITHUB_TOKEN_PERMISSIONS,
    GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS,
]


@dataclass(slots=True)
class Settings:
    root: Path
    user_agent: str = "managed-permissions-drift-catalog/0.1.0 (+https://github.com/managed-permissions-drift-catalog)"
    http_timeout_seconds: int = 30
    max_retries: int = 3
    max_workers: int = 8
    today_utc: str = ""
    generated_at_utc: str = ""
    azure_enable_cli_fallback: bool = False
    gcp_enable_authenticated_fallback: bool = False
    gcp_access_token: str | None = None

    @classmethod
    def from_root(cls, root: Path) -> "Settings":
        return cls(
            root=root,
            today_utc=utc_today().isoformat(),
            generated_at_utc=isoformat_utc(),
            azure_enable_cli_fallback=getenv_flag("MANAGED_PERMISSIONS_AZURE_USE_CLI"),
            gcp_enable_authenticated_fallback=getenv_flag("MANAGED_PERMISSIONS_GCP_USE_AUTH"),
            gcp_access_token=None,
        )

    @property
    def data_dir(self) -> Path:
        return self.root / "data"

    @property
    def docs_dir(self) -> Path:
        return self.root / "docs"

