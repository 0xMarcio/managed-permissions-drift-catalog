# managed-permissions-drift-catalog

Tracks documented permission drift in AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Supported datasets

- `aws-managed-policies`
- `azure-built-in-roles`
- `gcp-predefined-roles`
- `github-fgpat-permissions`
- `github-token-permissions`
- `github-actions-default-workflow-settings`

Last successful run: `2026-04-17T20:32:18Z`
Latest summary: **AWS became more privileged today** on `2026-04-17`.

## Local usage

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python -m managed_permissions_drift_catalog.cli update
```

Other commands:

```bash
python -m managed_permissions_drift_catalog.cli fetch --dataset aws-managed-policies
python -m managed_permissions_drift_catalog.cli normalize --dataset aws-managed-policies
python -m managed_permissions_drift_catalog.cli diff
python -m managed_permissions_drift_catalog.cli render
python -m managed_permissions_drift_catalog.cli query --permission s3:GetObject
python -m managed_permissions_drift_catalog.cli validate
```

## Reverse-index queries

Query by concrete permission and the CLI will return exact matches plus wildcard-bearing objects that match the query.

Examples:

```bash
python -m managed_permissions_drift_catalog.cli query --permission s3:GetObject
python -m managed_permissions_drift_catalog.cli query --permission Microsoft.Authorization/*/Delete
python -m managed_permissions_drift_catalog.cli query --permission contents:write
```

## Caveats

- Privilege scoring is a documented heuristic, not a proof of effective runtime access.
- AWS wildcard actions are not expanded, and conditions/resource scope are only preserved as metadata.
- Source fetch failures leave the existing platform snapshot in place and are reported as stale-source warnings.

## Repository outputs

- `data/latest/` stores latest normalized snapshots.
- `data/snapshots/` stores daily gzipped historical snapshots.
- `data/diffs/` stores per-day JSON diffs.
- `data/reverse-index/` stores atom reverse indexes.
- `data/summaries/` stores daily privilege-drift summaries.
- `docs/` stores browseable Markdown reports.
