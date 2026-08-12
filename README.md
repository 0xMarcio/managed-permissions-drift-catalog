# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: August 12, 2026 · [daily report](docs/daily/2026-08-12.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | No movement | `+2,088` net · `+27` objects · `~56` objects · `+2,114` atoms · `-2` atoms · 18 active days | AWS managed policies (30d, last changed [August 5, 2026](data/diffs/2026-08-05/aws-managed-policies.json)) |
| Azure | `~4` objects · 1 active day | `+98` net · `+2` objects · `~4` objects · `+110` atoms · 2 active days | Azure built-in roles (7d, last changed [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json)) |
| GCP | No movement | `+624` net · `+5` objects · `~170` objects · `+726` atoms · `-102` atoms · 4 active days | GCP predefined roles (30d, last changed [August 5, 2026](data/diffs/2026-08-05/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `-1` net · `~13` objects · `-1` object · `-1` atom · 8 active days | GitHub fine-grained PAT permissions (7d, last changed [August 7, 2026](data/diffs/2026-08-07/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,563` | [August 5, 2026](data/diffs/2026-08-05/aws-managed-policies.json) | No movement | `+2,088` net · `+27` objects · `~56` objects · `+2,114` atoms · `-2` atoms · 18 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-12/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json) | `~4` objects · 1 active day | `+98` net · `+2` objects · `~4` objects · `+110` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-12/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,367` | [August 5, 2026](data/diffs/2026-08-05/gcp-predefined-roles.json) | No movement | `+624` net · `+5` objects · `~170` objects · `+726` atoms · `-102` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-12/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-12/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [August 7, 2026](data/diffs/2026-08-07/github-fgpat-permissions.json) | `~1` object · 1 active day | `~12` objects · 7 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-12/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json) | No movement | `-1` net · `~1` object · `-1` object · `-1` atom · 2 active days | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-12/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,563` objects.
- Last 7 days: No movement.
- Last 30 days: `+2,088` net · `+27` objects · `~56` objects · `+2,114` atoms · `-2` atoms · 18 active days.
- Recent highlights: August 5, 2026: ~8 changed, +103 atoms (`AWSElasticBeanstalkServiceRolePolicy` (+84)); August 4, 2026: +4 objects, ~1 changed, +15 atoms (`AmazonBedrockExternalWebSearchFullAccess` (+3 atoms), `AWSApplicationMigrationFullAccess` (+5)); August 2, 2026: +2 objects, ~1 changed, +113 atoms (`AWSResilienceHubResilienceTestingPolicy` (+13 atoms), `AWSResourceExplorerServiceRolePolicy` (+90)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-12/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: `~4` objects · 1 active day.
- Last 30 days: `+98` net · `+2` objects · `~4` objects · `+110` atoms · 2 active days.
- Recent highlights: August 12, 2026: ~4 changed (`Logic Apps Standard Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-12/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,367` objects.
- Last 7 days: No movement.
- Last 30 days: `+624` net · `+5` objects · `~170` objects · `+726` atoms · `-102` atoms · 4 active days.
- Recent highlights: August 5, 2026: +1 objects, ~38 changed, +135 atoms (`Agent Registry User Beta` (+29 atoms), `Agent Registry API Admin Beta` (+12)); July 29, 2026: +2 objects, ~38 changed, +129 atoms, -22 atoms (`AI Platform Editor` (+37 atoms), `Cloud Composer API Service Agent` (+6)); July 22, 2026: +2 objects, ~53 changed, +293 atoms, -20 atoms (`FlowService Service Agent` (+4 atoms), `DLP Organization Data Profiles Driver` (+24, -4)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-12/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `~12` objects · 7 active days.
- Recent highlights: August 7, 2026: ~1 changed (`Administration` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-12/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `-1` net · `~1` object · `-1` object · `-1` atom · 2 active days.
- Recent highlights: July 31, 2026: -1 removed, -1 atoms (`models` (-1 atoms)); July 21, 2026: ~1 changed (`code-quality` (metadata only)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-12/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-12/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
