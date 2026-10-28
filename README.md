# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: October 28, 2026 · [daily report](docs/daily/2026-10-28.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+289` net · `+2` objects · `~26` objects · `+300` atoms · `-11` atoms · 5 active days | `+3,726` net · `+11` objects · `~89` objects · `+3,746` atoms · `-12` atoms · 24 active days | AWS managed policies (7d, last changed [October 28, 2026](data/diffs/2026-10-28/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | No movement | `+3,532` net · `+24` objects · `~607` objects · `-7` objects · `+3,644` atoms · `-112` atoms · 6 active days | GCP predefined roles (30d, last changed [October 21, 2026](data/diffs/2026-10-21/gcp-predefined-roles.json)) |
| GitHub | `~2` objects · 1 active day | `+7` net · `+3` objects · `~6` objects · `+3` atoms · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [October 28, 2026](data/diffs/2026-10-28/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,609` | [October 28, 2026](data/diffs/2026-10-28/aws-managed-policies.json) | `+289` net · `+2` objects · `~26` objects · `+300` atoms · `-11` atoms · 5 active days | `+3,726` net · `+11` objects · `~89` objects · `+3,746` atoms · `-12` atoms · 24 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-28/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-28/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,404` | [October 21, 2026](data/diffs/2026-10-21/gcp-predefined-roles.json) | No movement | `+3,532` net · `+24` objects · `~607` objects · `-7` objects · `+3,644` atoms · `-112` atoms · 6 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-28/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-28/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 28, 2026](data/diffs/2026-10-28/github-fgpat-permissions.json) | `~2` objects · 1 active day | `+5` net · `+2` objects · `~6` objects · `+2` atoms · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-28/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | No movement | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-28/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,609` objects.
- Last 7 days: `+289` net · `+2` objects · `~26` objects · `+300` atoms · `-11` atoms · 5 active days.
- Last 30 days: `+3,726` net · `+11` objects · `~89` objects · `+3,746` atoms · `-12` atoms · 24 active days.
- Recent highlights: October 28, 2026: +1 objects, ~16 changed, +211 atoms, -11 atoms (`AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy` (+10 atoms), `AWSSupportServiceRolePolicy` (+152, -11)); October 26, 2026: ~1 changed, +1 atoms (`AWSApplicationMigrationFSxProxyPolicy` (+1)); October 24, 2026: ~7 changed, +18 atoms (`AWSTransformInfrastructureExecutorAccessBatch` (+4)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-28/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-28/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,404` objects.
- Last 7 days: No movement.
- Last 30 days: `+3,532` net · `+24` objects · `~607` objects · `-7` objects · `+3,644` atoms · `-112` atoms · 6 active days.
- Recent highlights: October 21, 2026: +4 objects, ~252 changed, +1,151 atoms, -8 atoms (`Folder level Compute VM extension policies admin Beta` (+31 atoms), `Cloud Dataplex Service Agent` (+44, -8)); October 17, 2026: ~5 changed (`Advisory Support Editor` (metadata only)); October 15, 2026: +12 objects, ~92 changed, +1,336 atoms, -23 atoms (`Wiz Cloud Inventory Viewer` (+350 atoms), `Chronicle API Restricted Data Access Viewer Beta` (+160)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-28/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `~2` objects · 1 active day.
- Last 30 days: `+5` net · `+2` objects · `~6` objects · `+2` atoms · 5 active days.
- Recent highlights: October 28, 2026: ~2 changed (`Issues` (+5)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-28/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-28/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-28/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
