# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: August 10, 2026 · [daily report](docs/daily/2026-08-10.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+118` net · `+4` objects · `~9` objects · `+118` atoms · 2 active days | `+2,090` net · `+27` objects · `~58` objects · `+2,116` atoms · `-2` atoms · 19 active days | AWS managed policies (7d, last changed [August 5, 2026](data/diffs/2026-08-05/aws-managed-policies.json)) |
| Azure | No movement | `+98` net · `+2` objects · `+110` atoms · 1 active day | Azure built-in roles (30d, last changed [July 15, 2026](data/diffs/2026-07-15/azure-built-in-roles.json)) |
| GCP | `+135` net · `+1` object · `~38` objects · `+135` atoms · 1 active day | `+624` net · `+5` objects · `~170` objects · `+726` atoms · `-102` atoms · 4 active days | GCP predefined roles (7d, last changed [August 5, 2026](data/diffs/2026-08-05/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `-1` net · `~13` objects · `-1` object · `-1` atom · 8 active days | GitHub fine-grained PAT permissions (7d, last changed [August 7, 2026](data/diffs/2026-08-07/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,563` | [August 5, 2026](data/diffs/2026-08-05/aws-managed-policies.json) | `+118` net · `+4` objects · `~9` objects · `+118` atoms · 2 active days | `+2,090` net · `+27` objects · `~58` objects · `+2,116` atoms · `-2` atoms · 19 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-10/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [July 15, 2026](data/diffs/2026-07-15/azure-built-in-roles.json) | No movement | `+98` net · `+2` objects · `+110` atoms · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-10/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,367` | [August 5, 2026](data/diffs/2026-08-05/gcp-predefined-roles.json) | `+135` net · `+1` object · `~38` objects · `+135` atoms · 1 active day | `+624` net · `+5` objects · `~170` objects · `+726` atoms · `-102` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-10/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-10/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [August 7, 2026](data/diffs/2026-08-07/github-fgpat-permissions.json) | `~1` object · 1 active day | `~12` objects · 7 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-10/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json) | No movement | `-1` net · `~1` object · `-1` object · `-1` atom · 2 active days | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-10/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,563` objects.
- Last 7 days: `+118` net · `+4` objects · `~9` objects · `+118` atoms · 2 active days.
- Last 30 days: `+2,090` net · `+27` objects · `~58` objects · `+2,116` atoms · `-2` atoms · 19 active days.
- Recent highlights: August 5, 2026: ~8 changed, +103 atoms (`AWSElasticBeanstalkServiceRolePolicy` (+84)); August 4, 2026: +4 objects, ~1 changed, +15 atoms (`AmazonBedrockExternalWebSearchFullAccess` (+3 atoms), `AWSApplicationMigrationFullAccess` (+5)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-10/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `+98` net · `+2` objects · `+110` atoms · 1 active day.
- Recent highlights: July 15, 2026: +2 objects, +110 atoms (`Azure Local Migrate Owner` (+64 atoms)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-10/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,367` objects.
- Last 7 days: `+135` net · `+1` object · `~38` objects · `+135` atoms · 1 active day.
- Last 30 days: `+624` net · `+5` objects · `~170` objects · `+726` atoms · `-102` atoms · 4 active days.
- Recent highlights: August 5, 2026: +1 objects, ~38 changed, +135 atoms (`Agent Registry User Beta` (+29 atoms), `Agent Registry API Admin Beta` (+12)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-10/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `~12` objects · 7 active days.
- Recent highlights: August 7, 2026: ~1 changed (`Administration` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-10/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `-1` net · `~1` object · `-1` object · `-1` atom · 2 active days.
- Recent highlights: July 31, 2026: -1 removed, -1 atoms (`models` (-1 atoms)); July 21, 2026: ~1 changed (`code-quality` (metadata only)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-10/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-10/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
