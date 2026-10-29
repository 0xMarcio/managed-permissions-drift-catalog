# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: October 29, 2026 · [daily report](docs/daily/2026-10-29.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+242` net · `+3` objects · `~33` objects · `+254` atoms · `-12` atoms · 5 active days | `+3,748` net · `+13` objects · `~97` objects · `+3,769` atoms · `-13` atoms · 25 active days | AWS managed policies (7d, last changed [October 29, 2026](data/diffs/2026-10-29/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | `+892` net · `+7` objects · `~71` objects · `+906` atoms · `-14` atoms · 1 active day | `+4,424` net · `+31` objects · `~678` objects · `-7` objects · `+4,550` atoms · `-126` atoms · 7 active days | GCP predefined roles (7d, last changed [October 29, 2026](data/diffs/2026-10-29/gcp-predefined-roles.json)) |
| GitHub | `~3` objects · 2 active days | `+7` net · `+3` objects · `~6` objects · `+3` atoms · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [October 29, 2026](data/diffs/2026-10-29/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,611` | [October 29, 2026](data/diffs/2026-10-29/aws-managed-policies.json) | `+242` net · `+3` objects · `~33` objects · `+254` atoms · `-12` atoms · 5 active days | `+3,748` net · `+13` objects · `~97` objects · `+3,769` atoms · `-13` atoms · 25 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-29/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-29/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,411` | [October 29, 2026](data/diffs/2026-10-29/gcp-predefined-roles.json) | `+892` net · `+7` objects · `~71` objects · `+906` atoms · `-14` atoms · 1 active day | `+4,424` net · `+31` objects · `~678` objects · `-7` objects · `+4,550` atoms · `-126` atoms · 7 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-29/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-29/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 29, 2026](data/diffs/2026-10-29/github-fgpat-permissions.json) | `~3` objects · 2 active days | `+5` net · `+2` objects · `~6` objects · `+2` atoms · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-29/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | No movement | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-29/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,611` objects.
- Last 7 days: `+242` net · `+3` objects · `~33` objects · `+254` atoms · `-12` atoms · 5 active days.
- Last 30 days: `+3,748` net · `+13` objects · `~97` objects · `+3,769` atoms · `-13` atoms · 25 active days.
- Recent highlights: October 29, 2026: +2 objects, ~8 changed, +23 atoms, -1 atoms (`AWSXRayAPIKeyAccess` (+2 atoms), `AWSPartnerCentralOpportunityManagement` (+4)); October 28, 2026: +1 objects, ~16 changed, +211 atoms, -11 atoms (`AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy` (+10 atoms), `AWSSupportServiceRolePolicy` (+152, -11)); October 26, 2026: ~1 changed, +1 atoms (`AWSApplicationMigrationFSxProxyPolicy` (+1)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-29/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-29/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,411` objects.
- Last 7 days: `+892` net · `+7` objects · `~71` objects · `+906` atoms · `-14` atoms · 1 active day.
- Last 30 days: `+4,424` net · `+31` objects · `~678` objects · `-7` objects · `+4,550` atoms · `-126` atoms · 7 active days.
- Recent highlights: October 29, 2026: +7 objects, ~71 changed, +906 atoms, -14 atoms (`Cloud Functions Service Agent` (+265 atoms), `Wiz Cloud Inventory Viewer` (+259)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-29/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `~3` objects · 2 active days.
- Last 30 days: `+5` net · `+2` objects · `~6` objects · `+2` atoms · 5 active days.
- Recent highlights: October 29, 2026: ~1 changed (`Repository security advisories` (+4)); October 28, 2026: ~2 changed (`Issues` (+5)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-29/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-29/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-29/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
