# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: September 6, 2026 · [daily report](docs/daily/2026-09-06.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+466` net · `~20` objects · `+466` atoms · 4 active days | `+2,846` net · `+22` objects · `~84` objects · `+2,876` atoms · `-12` atoms · 18 active days | AWS managed policies (7d, last changed [September 5, 2026](data/diffs/2026-09-05/aws-managed-policies.json)) |
| Azure | `~3` objects · 1 active day | `~7` objects · 2 active days | Azure built-in roles (7d, last changed [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json)) |
| GCP | `+298` net · `+1` object · `~82` objects · `-2` objects · `+350` atoms · `-52` atoms · 1 active day | `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days | GCP predefined roles (7d, last changed [September 3, 2026](data/diffs/2026-09-03/gcp-predefined-roles.json)) |
| GitHub | `~3` objects · 2 active days | `~4` objects · 3 active days | GitHub fine-grained PAT permissions (7d, last changed [September 5, 2026](data/diffs/2026-09-05/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,585` | [September 5, 2026](data/diffs/2026-09-05/aws-managed-policies.json) | `+466` net · `~20` objects · `+466` atoms · 4 active days | `+2,846` net · `+22` objects · `~84` objects · `+2,876` atoms · `-12` atoms · 18 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-06/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json) | `~3` objects · 1 active day | `~7` objects · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-06/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,374` | [September 3, 2026](data/diffs/2026-09-03/gcp-predefined-roles.json) | `+298` net · `+1` object · `~82` objects · `-2` objects · `+350` atoms · `-52` atoms · 1 active day | `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-06/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-06/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [September 5, 2026](data/diffs/2026-09-05/github-fgpat-permissions.json) | `~3` objects · 2 active days | `~4` objects · 3 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-06/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-06/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,585` objects.
- Last 7 days: `+466` net · `~20` objects · `+466` atoms · 4 active days.
- Last 30 days: `+2,846` net · `+22` objects · `~84` objects · `+2,876` atoms · `-12` atoms · 18 active days.
- Recent highlights: September 5, 2026: ~6 changed, +401 atoms (`AWSResourceExplorerServiceRolePolicy` (+393)); September 4, 2026: ~4 changed, +4 atoms (`AWSTransformInfrastructureExecutorAccessBatch` (+1)); September 3, 2026: ~2 changed, +2 atoms (`AmazonECS_FullAccess` (+2)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-06/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: `~3` objects · 1 active day.
- Last 30 days: `~7` objects · 2 active days.
- Recent highlights: September 4, 2026: ~3 changed (`Search Index Data Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-06/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,374` objects.
- Last 7 days: `+298` net · `+1` object · `~82` objects · `-2` objects · `+350` atoms · `-52` atoms · 1 active day.
- Last 30 days: `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days.
- Recent highlights: September 3, 2026: +1 objects, ~82 changed, -2 removed, +350 atoms, -52 atoms (`App Topology Admin Beta` (+16 atoms), `Discovery Engine Admin` (+28)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-06/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~3` objects · 2 active days.
- Last 30 days: `~4` objects · 3 active days.
- Recent highlights: September 5, 2026: ~1 changed (`Metadata` (+1)); September 4, 2026: ~2 changed (`Administration` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-06/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-06/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-06/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
