# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: November 17, 2026 · [daily report](docs/daily/2026-11-17.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+1,188` net · `+7` objects · `~54` objects · `+1,280` atoms · `-40` atoms · 5 active days | `+3,977` net · `+20` objects · `~145` objects · `+4,507` atoms · `-56` atoms · 20 active days | AWS managed policies (7d, last changed [November 15, 2026](data/diffs/2026-11-15/aws-managed-policies.json)) |
| Azure | No movement | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | Azure built-in roles (30d, last changed [November 4, 2026](data/diffs/2026-11-04/azure-built-in-roles.json)) |
| GCP | No movement | `+2,930` net · `+11` objects · `~440` objects · `+2,963` atoms · `-33` atoms · 3 active days | GCP predefined roles (30d, last changed [November 4, 2026](data/diffs/2026-11-04/gcp-predefined-roles.json)) |
| GitHub | `+6` net · `+2` objects · `+4` atoms · 1 active day | `+6` net · `+2` objects · `~7` objects · `+4` atoms · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [November 12, 2026](data/diffs/2026-11-12/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,625` | [November 15, 2026](data/diffs/2026-11-15/aws-managed-policies.json) | `+1,188` net · `+7` objects · `~54` objects · `+1,280` atoms · `-40` atoms · 5 active days | `+3,977` net · `+20` objects · `~145` objects · `+4,507` atoms · `-56` atoms · 20 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-17/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `506` | [November 4, 2026](data/diffs/2026-11-04/azure-built-in-roles.json) | No movement | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-17/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,411` | [November 4, 2026](data/diffs/2026-11-04/gcp-predefined-roles.json) | No movement | `+2,930` net · `+11` objects · `~440` objects · `+2,963` atoms · `-33` atoms · 3 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-17/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-17/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `78` | [November 12, 2026](data/diffs/2026-11-12/github-fgpat-permissions.json) | `+6` net · `+2` objects · `+4` atoms · 1 active day | `+6` net · `+2` objects · `~7` objects · `+4` atoms · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-17/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-17/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,625` objects.
- Last 7 days: `+1,188` net · `+7` objects · `~54` objects · `+1,280` atoms · `-40` atoms · 5 active days.
- Last 30 days: `+3,977` net · `+20` objects · `~145` objects · `+4,507` atoms · `-56` atoms · 20 active days.
- Recent highlights: November 15, 2026: +1 objects, ~21 changed, +275 atoms, -14 atoms (`ContinuumThreatsServiceRolePolicy` (+8 atoms), `SageMakerStudioAdminIAMDefaultExecutionPolicy` (+49, -4)); November 14, 2026: +1 objects, ~10 changed, +802 atoms, -3 atoms (`AWSMarketplaceAgenticCommerceServiceRolePolicy` (+13 atoms), `ViewOnlyAccess` (+265)); November 13, 2026: +2 objects, ~4 changed, +57 atoms (`AWSNetworkFirewallIGWServiceRolePolicy` (+15 atoms), `AWSTransformServerMigrationAgentPolicy` (+17)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-17/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `506` objects.
- Last 7 days: No movement.
- Last 30 days: `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days.
- Recent highlights: November 4, 2026: +2 objects, ~4 changed, +8 atoms (`Foundry Project Runtime User` (+3 atoms), `Foundry Account Owner` (+1)); October 30, 2026: ~1 changed, +2 atoms (`FHIR Data Bulk Operator` (+2)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-17/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,411` objects.
- Last 7 days: No movement.
- Last 30 days: `+2,930` net · `+11` objects · `~440` objects · `+2,963` atoms · `-33` atoms · 3 active days.
- Recent highlights: November 4, 2026: ~117 changed, +906 atoms, -11 atoms (`DLP Organization Data Profiles Driver` (+63)); October 29, 2026: +7 objects, ~71 changed, +906 atoms, -14 atoms (`Cloud Functions Service Agent` (+265 atoms), `Wiz Cloud Inventory Viewer` (+259)); October 21, 2026: +4 objects, ~252 changed, +1,151 atoms, -8 atoms (`Folder level Compute VM extension policies admin Beta` (+31 atoms), `Cloud Dataplex Service Agent` (+44, -8)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-17/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `78` objects.
- Last 7 days: `+6` net · `+2` objects · `+4` atoms · 1 active day.
- Last 30 days: `+6` net · `+2` objects · `~7` objects · `+4` atoms · 6 active days.
- Recent highlights: November 12, 2026: +2 objects, +4 atoms (`Issue Fields` (+2 atoms)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-17/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-17/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-17/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
