# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: September 10, 2026 · [daily report](docs/daily/2026-09-10.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+567` net · `+4` objects · `~21` objects · `+567` atoms · 4 active days | `+3,008` net · `+26` objects · `~95` objects · `+3,038` atoms · `-12` atoms · 20 active days | AWS managed policies (7d, last changed [September 10, 2026](data/diffs/2026-09-10/aws-managed-policies.json)) |
| Azure | `~3` objects · 1 active day | `~7` objects · 2 active days | Azure built-in roles (7d, last changed [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json)) |
| GCP | No movement | `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days | GCP predefined roles (30d, last changed [September 3, 2026](data/diffs/2026-09-03/gcp-predefined-roles.json)) |
| GitHub | `~3` objects · 2 active days | `~4` objects · 3 active days | GitHub fine-grained PAT permissions (7d, last changed [September 5, 2026](data/diffs/2026-09-05/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,589` | [September 10, 2026](data/diffs/2026-09-10/aws-managed-policies.json) | `+567` net · `+4` objects · `~21` objects · `+567` atoms · 4 active days | `+3,008` net · `+26` objects · `~95` objects · `+3,038` atoms · `-12` atoms · 20 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-10/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json) | `~3` objects · 1 active day | `~7` objects · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-10/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,374` | [September 3, 2026](data/diffs/2026-09-03/gcp-predefined-roles.json) | No movement | `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-10/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-10/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [September 5, 2026](data/diffs/2026-09-05/github-fgpat-permissions.json) | `~3` objects · 2 active days | `~4` objects · 3 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-10/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-10/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,589` objects.
- Last 7 days: `+567` net · `+4` objects · `~21` objects · `+567` atoms · 4 active days.
- Last 30 days: `+3,008` net · `+26` objects · `~95` objects · `+3,038` atoms · `-12` atoms · 20 active days.
- Recent highlights: September 10, 2026: ~1 changed, +2 atoms (`AWSElasticDisasterRecoveryStagingAccountPolicy_v2` (+2)); September 9, 2026: +4 objects, ~10 changed, +160 atoms (`AmazonODBExascaleVmClusterAdmin` (+35 atoms), `AmazonODBFullAccess` (+20)); September 5, 2026: ~6 changed, +401 atoms (`AWSResourceExplorerServiceRolePolicy` (+393)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-10/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: `~3` objects · 1 active day.
- Last 30 days: `~7` objects · 2 active days.
- Recent highlights: September 4, 2026: ~3 changed (`Search Index Data Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-10/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,374` objects.
- Last 7 days: No movement.
- Last 30 days: `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days.
- Recent highlights: September 3, 2026: +1 objects, ~82 changed, -2 removed, +350 atoms, -52 atoms (`App Topology Admin Beta` (+16 atoms), `Discovery Engine Admin` (+28)); August 26, 2026: +1 objects, ~49 changed, +90 atoms, -9 atoms (`Analytics Hub Service Agent` (+3 atoms), `Chronicle Service Agent` (+10)); August 20, 2026: +4 objects, ~51 changed, +345 atoms (`Cloud FTP Admin` (+20 atoms), `Security Admin` (+16)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-10/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~3` objects · 2 active days.
- Last 30 days: `~4` objects · 3 active days.
- Recent highlights: September 5, 2026: ~1 changed (`Metadata` (+1)); September 4, 2026: ~2 changed (`Administration` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-10/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-10/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-10/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
