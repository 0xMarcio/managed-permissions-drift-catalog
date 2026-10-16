# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: October 16, 2026 · [daily report](docs/daily/2026-10-16.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+161` net · `+3` objects · `~25` objects · `+161` atoms · 7 active days | `+5,004` net · `+15` objects · `~78` objects · `-1` object · `+5,030` atoms · `-12` atoms · 24 active days | AWS managed policies (7d, last changed [October 16, 2026](data/diffs/2026-10-16/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | `+1,313` net · `+12` objects · `~93` objects · `+1,336` atoms · `-23` atoms · 2 active days | `+2,654` net · `+26` objects · `~393` objects · `-7` objects · `+2,758` atoms · `-104` atoms · 5 active days | GCP predefined roles (7d, last changed [October 15, 2026](data/diffs/2026-10-15/gcp-predefined-roles.json)) |
| GitHub | `+2` net · `+1` object · `+1` atom · 1 active day | `+9` net · `+4` objects · `~7` objects · `+4` atoms · 7 active days | GitHub GITHUB_TOKEN permissions (7d, last changed [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,604` | [October 16, 2026](data/diffs/2026-10-16/aws-managed-policies.json) | `+161` net · `+3` objects · `~25` objects · `+161` atoms · 7 active days | `+5,004` net · `+15` objects · `~78` objects · `-1` object · `+5,030` atoms · `-12` atoms · 24 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-16/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-16/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,400` | [October 15, 2026](data/diffs/2026-10-15/gcp-predefined-roles.json) | `+1,313` net · `+12` objects · `~93` objects · `+1,336` atoms · `-23` atoms · 2 active days | `+2,654` net · `+26` objects · `~393` objects · `-7` objects · `+2,758` atoms · `-104` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-16/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-16/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 9, 2026](data/diffs/2026-10-09/github-fgpat-permissions.json) | No movement | `+7` net · `+3` objects · `~7` objects · `+3` atoms · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-16/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | `+2` net · `+1` object · `+1` atom · 1 active day | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-16/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,604` objects.
- Last 7 days: `+161` net · `+3` objects · `~25` objects · `+161` atoms · 7 active days.
- Last 30 days: `+5,004` net · `+15` objects · `~78` objects · `-1` object · `+5,030` atoms · `-12` atoms · 24 active days.
- Recent highlights: October 16, 2026: ~8 changed, +58 atoms (`ViewOnlyAccess` (+14)); October 15, 2026: +1 objects, ~2 changed, +14 atoms (`SageMakerStudioDataAppsAccessRolePolicy` (+11 atoms), `AIDevOpsConstellationAccessPolicy` (+2)); October 14, 2026: +2 objects, ~1 changed, +48 atoms (`AmazonSageMakerTrainingSessionAccess` (+26 atoms), `AWSElasticLoadBalancingClassicServiceRolePolicy` (+1)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-16/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-16/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,400` objects.
- Last 7 days: `+1,313` net · `+12` objects · `~93` objects · `+1,336` atoms · `-23` atoms · 2 active days.
- Last 30 days: `+2,654` net · `+26` objects · `~393` objects · `-7` objects · `+2,758` atoms · `-104` atoms · 5 active days.
- Recent highlights: October 15, 2026: +12 objects, ~92 changed, +1,336 atoms, -23 atoms (`Wiz Cloud Inventory Viewer` (+350 atoms), `Chronicle API Restricted Data Access Viewer Beta` (+160)); October 13, 2026: ~1 changed (`Storage Object User` (metadata only)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-16/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: No movement.
- Last 30 days: `+7` net · `+3` objects · `~7` objects · `+3` atoms · 6 active days.
- Recent highlights: October 9, 2026: ~1 changed (`Repository creation` (+1)); October 6, 2026: ~1 changed (`Pull requests` (+1)); September 30, 2026: +2 objects, ~1 changed, +2 atoms (`External custom properties for repositories` (+1 atoms), `Actions` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-16/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-16/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-16/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
