from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from ..config import (
    AWS_MANAGED_POLICIES,
    AZURE_BUILT_IN_ROLES,
    GCP_PREDEFINED_ROLES,
    GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS,
    GITHUB_FGPAT_PERMISSIONS,
    GITHUB_TOKEN_PERMISSIONS,
)


@dataclass(frozen=True, slots=True)
class SourceAdapter:
    dataset: str
    platform: str
    fetch: Callable
    normalize: Callable


def build_registry() -> dict[str, SourceAdapter]:
    from . import aws, azure, gcp, github

    return {
        AWS_MANAGED_POLICIES: SourceAdapter(
            dataset=AWS_MANAGED_POLICIES,
            platform="aws",
            fetch=aws.fetch,
            normalize=aws.normalize,
        ),
        AZURE_BUILT_IN_ROLES: SourceAdapter(
            dataset=AZURE_BUILT_IN_ROLES,
            platform="azure",
            fetch=azure.fetch,
            normalize=azure.normalize,
        ),
        GCP_PREDEFINED_ROLES: SourceAdapter(
            dataset=GCP_PREDEFINED_ROLES,
            platform="gcp",
            fetch=gcp.fetch,
            normalize=gcp.normalize,
        ),
        GITHUB_FGPAT_PERMISSIONS: SourceAdapter(
            dataset=GITHUB_FGPAT_PERMISSIONS,
            platform="github",
            fetch=github.fetch_fgpat,
            normalize=github.normalize_fgpat,
        ),
        GITHUB_TOKEN_PERMISSIONS: SourceAdapter(
            dataset=GITHUB_TOKEN_PERMISSIONS,
            platform="github",
            fetch=github.fetch_token_permissions,
            normalize=github.normalize_token_permissions,
        ),
        GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS: SourceAdapter(
            dataset=GITHUB_ACTIONS_DEFAULT_WORKFLOW_SETTINGS,
            platform="github",
            fetch=github.fetch_actions_settings,
            normalize=github.normalize_actions_settings,
        ),
    }


REGISTRY = build_registry()

