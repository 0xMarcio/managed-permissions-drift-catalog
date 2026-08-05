# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: August 5, 2026 · [daily report](docs/daily/2026-08-05.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+351` net · `+10` objects · `~20` objects · `+357` atoms · 6 active days | `+2,273` net · `+30` objects · `~74` objects · `+2,299` atoms · `-2` atoms · 23 active days | AWS managed policies (7d, last changed [August 5, 2026](data/diffs/2026-08-05/aws-managed-policies.json)) |
| Azure | No movement | `+98` net · `+2` objects · `+110` atoms · 1 active day | Azure built-in roles (30d, last changed [July 15, 2026](data/diffs/2026-07-15/azure-built-in-roles.json)) |
| GCP | `+135` net · `+1` object · `~38` objects · `+135` atoms · 1 active day | `+2,299` net · `+18` objects · `~239` objects · `+2,406` atoms · `-107` atoms · 5 active days | GCP predefined roles (7d, last changed [August 5, 2026](data/diffs/2026-08-05/gcp-predefined-roles.json)) |
| GitHub | `-1` net · `~4` objects · `-1` object · `-1` atom · 2 active days | `-1` net · `~13` objects · `-1` object · `-1` atom · 8 active days | GitHub GITHUB_TOKEN permissions (7d, last changed [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,563` | [August 5, 2026](data/diffs/2026-08-05/aws-managed-policies.json) | `+351` net · `+10` objects · `~20` objects · `+357` atoms · 6 active days | `+2,273` net · `+30` objects · `~74` objects · `+2,299` atoms · `-2` atoms · 23 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-05/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [July 15, 2026](data/diffs/2026-07-15/azure-built-in-roles.json) | No movement | `+98` net · `+2` objects · `+110` atoms · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-05/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,367` | [August 5, 2026](data/diffs/2026-08-05/gcp-predefined-roles.json) | `+135` net · `+1` object · `~38` objects · `+135` atoms · 1 active day | `+2,299` net · `+18` objects · `~239` objects · `+2,406` atoms · `-107` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-05/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-05/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [July 31, 2026](data/diffs/2026-07-31/github-fgpat-permissions.json) | `~4` objects · 2 active days | `~12` objects · 7 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-05/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json) | `-1` net · `-1` object · `-1` atom · 1 active day | `-1` net · `~1` object · `-1` object · `-1` atom · 2 active days | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-05/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,563` objects.
- Last 7 days: `+351` net · `+10` objects · `~20` objects · `+357` atoms · 6 active days.
- Last 30 days: `+2,273` net · `+30` objects · `~74` objects · `+2,299` atoms · `-2` atoms · 23 active days.
- Recent highlights: August 5, 2026: ~8 changed, +103 atoms (`AWSElasticBeanstalkServiceRolePolicy` (+84)); August 4, 2026: +4 objects, ~1 changed, +15 atoms (`AmazonBedrockExternalWebSearchFullAccess` (+3 atoms), `AWSApplicationMigrationFullAccess` (+5)); August 2, 2026: +2 objects, ~1 changed, +113 atoms (`AWSResilienceHubResilienceTestingPolicy` (+13 atoms), `AWSResourceExplorerServiceRolePolicy` (+90)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-05/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `+98` net · `+2` objects · `+110` atoms · 1 active day.
- Recent highlights: July 15, 2026: +2 objects, +110 atoms (`Azure Local Migrate Owner` (+64 atoms)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-05/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,367` objects.
- Last 7 days: `+135` net · `+1` object · `~38` objects · `+135` atoms · 1 active day.
- Last 30 days: `+2,299` net · `+18` objects · `~239` objects · `+2,406` atoms · `-107` atoms · 5 active days.
- Recent highlights: August 5, 2026: +1 objects, ~38 changed, +135 atoms (`Agent Registry User Beta` (+29 atoms), `Agent Registry API Admin Beta` (+12)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-05/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~4` objects · 2 active days.
- Last 30 days: `~12` objects · 7 active days.
- Recent highlights: July 31, 2026: ~3 changed (`Pull requests` (+5)); July 30, 2026: ~1 changed (`Artifact metadata` (+2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-05/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: `-1` net · `-1` object · `-1` atom · 1 active day.
- Last 30 days: `-1` net · `~1` object · `-1` object · `-1` atom · 2 active days.
- Recent highlights: July 31, 2026: -1 removed, -1 atoms (`models` (-1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-05/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-05/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
