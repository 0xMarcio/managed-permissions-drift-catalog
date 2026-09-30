# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: September 30, 2026 · [daily report](docs/daily/2026-09-30.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+2,530` net · `+2` objects · `~20` objects · `-1` object · `+2,541` atoms · `-11` atoms · 5 active days | `+4,579` net · `+14` objects · `~75` objects · `-1` object · `+4,596` atoms · `-11` atoms · 19 active days | AWS managed policies (7d, last changed [September 30, 2026](data/diffs/2026-09-30/aws-managed-policies.json)) |
| Azure | No movement | `~3` objects · 1 active day | Azure built-in roles (30d, last changed [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json)) |
| GCP | `+314` net · `+5` objects · `~67` objects · `-6` objects · `+367` atoms · `-53` atoms · 1 active day | `+1,647` net · `+19` objects · `~320` objects · `-8` objects · `+1,758` atoms · `-111` atoms · 4 active days | GCP predefined roles (7d, last changed [September 30, 2026](data/diffs/2026-09-30/gcp-predefined-roles.json)) |
| GitHub | `+7` net · `+3` objects · `~3` objects · `+3` atoms · 3 active days | `+7` net · `+3` objects · `~13` objects · `+3` atoms · 8 active days | GitHub fine-grained PAT permissions (7d, last changed [September 30, 2026](data/diffs/2026-09-30/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,598` | [September 30, 2026](data/diffs/2026-09-30/aws-managed-policies.json) | `+2,530` net · `+2` objects · `~20` objects · `-1` object · `+2,541` atoms · `-11` atoms · 5 active days | `+4,579` net · `+14` objects · `~75` objects · `-1` object · `+4,596` atoms · `-11` atoms · 19 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-30/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json) | No movement | `~3` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-30/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,386` | [September 30, 2026](data/diffs/2026-09-30/gcp-predefined-roles.json) | `+314` net · `+5` objects · `~67` objects · `-6` objects · `+367` atoms · `-53` atoms · 1 active day | `+1,647` net · `+19` objects · `~320` objects · `-8` objects · `+1,758` atoms · `-111` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-30/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-30/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [September 30, 2026](data/diffs/2026-09-30/github-fgpat-permissions.json) | `+7` net · `+3` objects · `~3` objects · `+3` atoms · 3 active days | `+7` net · `+3` objects · `~13` objects · `+3` atoms · 8 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-30/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-30/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,598` objects.
- Last 7 days: `+2,530` net · `+2` objects · `~20` objects · `-1` object · `+2,541` atoms · `-11` atoms · 5 active days.
- Last 30 days: `+4,579` net · `+14` objects · `~75` objects · `-1` object · `+4,596` atoms · `-11` atoms · 19 active days.
- Recent highlights: September 30, 2026: ~3 changed, +6 atoms (`AmazonECSInfrastructureRolePolicyForVpcLattice` (+3)); September 27, 2026: +1 objects, ~4 changed, -1 removed, +58 atoms, -11 atoms (`AmazonECSInfrastructureRoleForGatewayHostSharedALB` (+48 atoms), `AnthropicReadOnlyAccess` (+4)); September 26, 2026: ~8 changed, +2,083 atoms (`AWSWellArchitectedAgentResourceScanningServiceRolePolicy` (+1,966)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-30/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~3` objects · 1 active day.
- Recent highlights: September 4, 2026: ~3 changed (`Search Index Data Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-30/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,386` objects.
- Last 7 days: `+314` net · `+5` objects · `~67` objects · `-6` objects · `+367` atoms · `-53` atoms · 1 active day.
- Last 30 days: `+1,647` net · `+19` objects · `~320` objects · `-8` objects · `+1,758` atoms · `-111` atoms · 4 active days.
- Recent highlights: September 30, 2026: +5 objects, ~67 changed, -6 removed, +367 atoms, -53 atoms (`Database Insights Service Agent` (+71 atoms), `Security Admin` (+13, -2)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-30/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `+7` net · `+3` objects · `~3` objects · `+3` atoms · 3 active days.
- Last 30 days: `+7` net · `+3` objects · `~13` objects · `+3` atoms · 8 active days.
- Recent highlights: September 30, 2026: +2 objects, ~1 changed, +2 atoms (`External custom properties for repositories` (+1 atoms), `Actions` (+1)); September 29, 2026: ~1 changed (`Issues` (+3)); September 25, 2026: +1 objects, ~1 changed, +1 atoms (`Repository creation` (+1 atoms), `Administration` (+2, -2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-30/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-30/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-30/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
