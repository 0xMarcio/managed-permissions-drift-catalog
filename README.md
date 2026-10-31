# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: October 31, 2026 · [daily report](docs/daily/2026-10-31.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+1,097` net · `+5` objects · `~45` objects · `+1,109` atoms · `-12` atoms · 5 active days | `+4,615` net · `+14` objects · `~114` objects · `+4,636` atoms · `-13` atoms · 25 active days | AWS managed policies (7d, last changed [October 31, 2026](data/diffs/2026-10-31/aws-managed-policies.json)) |
| Azure | `+2` net · `~1` object · `+2` atoms · 1 active day | `+2` net · `~1` object · `+2` atoms · 1 active day | Azure built-in roles (7d, last changed [October 30, 2026](data/diffs/2026-10-30/azure-built-in-roles.json)) |
| GCP | `+892` net · `+7` objects · `~71` objects · `+906` atoms · `-14` atoms · 1 active day | `+4,110` net · `+26` objects · `~611` objects · `-1` object · `+4,183` atoms · `-73` atoms · 6 active days | GCP predefined roles (7d, last changed [October 29, 2026](data/diffs/2026-10-29/gcp-predefined-roles.json)) |
| GitHub | `~3` objects · 2 active days | `+2` net · `+1` object · `~5` objects · `+1` atom · 5 active days | GitHub fine-grained PAT permissions (7d, last changed [October 29, 2026](data/diffs/2026-10-29/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,613` | [October 31, 2026](data/diffs/2026-10-31/aws-managed-policies.json) | `+1,097` net · `+5` objects · `~45` objects · `+1,109` atoms · `-12` atoms · 5 active days | `+4,615` net · `+14` objects · `~114` objects · `+4,636` atoms · `-13` atoms · 25 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-31/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [October 30, 2026](data/diffs/2026-10-30/azure-built-in-roles.json) | `+2` net · `~1` object · `+2` atoms · 1 active day | `+2` net · `~1` object · `+2` atoms · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-31/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,411` | [October 29, 2026](data/diffs/2026-10-29/gcp-predefined-roles.json) | `+892` net · `+7` objects · `~71` objects · `+906` atoms · `-14` atoms · 1 active day | `+4,110` net · `+26` objects · `~611` objects · `-1` object · `+4,183` atoms · `-73` atoms · 6 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-31/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-31/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 29, 2026](data/diffs/2026-10-29/github-fgpat-permissions.json) | `~3` objects · 2 active days | `~5` objects · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-31/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | No movement | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-31/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,613` objects.
- Last 7 days: `+1,097` net · `+5` objects · `~45` objects · `+1,109` atoms · `-12` atoms · 5 active days.
- Last 30 days: `+4,615` net · `+14` objects · `~114` objects · `+4,636` atoms · `-13` atoms · 25 active days.
- Recent highlights: October 31, 2026: +1 objects, ~12 changed, +235 atoms (`FinOpsAgentIdentityReaderPolicy` (+3 atoms), `ViewOnlyAccess` (+87)); October 30, 2026: +1 objects, ~8 changed, +639 atoms (`TagsHealthServiceRolePolicy` (+1 atoms), `AWSResourceExplorerServiceRolePolicy` (+408)); October 29, 2026: +2 objects, ~8 changed, +23 atoms, -1 atoms (`AWSXRayAPIKeyAccess` (+2 atoms), `AWSPartnerCentralOpportunityManagement` (+4)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-31/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: `+2` net · `~1` object · `+2` atoms · 1 active day.
- Last 30 days: `+2` net · `~1` object · `+2` atoms · 1 active day.
- Recent highlights: October 30, 2026: ~1 changed, +2 atoms (`FHIR Data Bulk Operator` (+2)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-31/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,411` objects.
- Last 7 days: `+892` net · `+7` objects · `~71` objects · `+906` atoms · `-14` atoms · 1 active day.
- Last 30 days: `+4,110` net · `+26` objects · `~611` objects · `-1` object · `+4,183` atoms · `-73` atoms · 6 active days.
- Recent highlights: October 29, 2026: +7 objects, ~71 changed, +906 atoms, -14 atoms (`Cloud Functions Service Agent` (+265 atoms), `Wiz Cloud Inventory Viewer` (+259)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-31/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `~3` objects · 2 active days.
- Last 30 days: `~5` objects · 4 active days.
- Recent highlights: October 29, 2026: ~1 changed (`Repository security advisories` (+4)); October 28, 2026: ~2 changed (`Issues` (+5)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-31/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-31/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-31/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
