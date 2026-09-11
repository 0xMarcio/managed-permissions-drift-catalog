# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: September 11, 2026 · [daily report](docs/daily/2026-09-11.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+574` net · `+5` objects · `~22` objects · `+574` atoms · 4 active days | `+3,019` net · `+27` objects · `~100` objects · `+3,049` atoms · `-12` atoms · 21 active days | AWS managed policies (7d, last changed [September 11, 2026](data/diffs/2026-09-11/aws-managed-policies.json)) |
| Azure | No movement | `~3` objects · 1 active day | Azure built-in roles (30d, last changed [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json)) |
| GCP | No movement | `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days | GCP predefined roles (30d, last changed [September 3, 2026](data/diffs/2026-09-03/gcp-predefined-roles.json)) |
| GitHub | `~4` objects · 2 active days | `~7` objects · 4 active days | GitHub fine-grained PAT permissions (7d, last changed [September 11, 2026](data/diffs/2026-09-11/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,590` | [September 11, 2026](data/diffs/2026-09-11/aws-managed-policies.json) | `+574` net · `+5` objects · `~22` objects · `+574` atoms · 4 active days | `+3,019` net · `+27` objects · `~100` objects · `+3,049` atoms · `-12` atoms · 21 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-11/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json) | No movement | `~3` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-11/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,374` | [September 3, 2026](data/diffs/2026-09-03/gcp-predefined-roles.json) | No movement | `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-11/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-11/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [September 11, 2026](data/diffs/2026-09-11/github-fgpat-permissions.json) | `~4` objects · 2 active days | `~7` objects · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-11/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-11/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,590` objects.
- Last 7 days: `+574` net · `+5` objects · `~22` objects · `+574` atoms · 4 active days.
- Last 30 days: `+3,019` net · `+27` objects · `~100` objects · `+3,049` atoms · `-12` atoms · 21 active days.
- Recent highlights: September 11, 2026: +1 objects, ~5 changed, +11 atoms (`AmazonSageMakerHyperPodInferenceGatewayAccess` (+5 atoms), `AWSResourceExplorerServiceRolePolicy` (+2)); September 10, 2026: ~1 changed, +2 atoms (`AWSElasticDisasterRecoveryStagingAccountPolicy_v2` (+2)); September 9, 2026: +4 objects, ~10 changed, +160 atoms (`AmazonODBExascaleVmClusterAdmin` (+35 atoms), `AmazonODBFullAccess` (+20)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-11/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~3` objects · 1 active day.
- Recent highlights: September 4, 2026: ~3 changed (`Search Index Data Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-11/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,374` objects.
- Last 7 days: No movement.
- Last 30 days: `+1,177` net · `+9` objects · `~216` objects · `-2` objects · `+1,238` atoms · `-61` atoms · 5 active days.
- Recent highlights: September 3, 2026: +1 objects, ~82 changed, -2 removed, +350 atoms, -52 atoms (`App Topology Admin Beta` (+16 atoms), `Discovery Engine Admin` (+28)); August 26, 2026: +1 objects, ~49 changed, +90 atoms, -9 atoms (`Analytics Hub Service Agent` (+3 atoms), `Chronicle Service Agent` (+10)); August 20, 2026: +4 objects, ~51 changed, +345 atoms (`Cloud FTP Admin` (+20 atoms), `Security Admin` (+16)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-11/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~4` objects · 2 active days.
- Last 30 days: `~7` objects · 4 active days.
- Recent highlights: September 11, 2026: ~3 changed (`Administration` (+2)); September 5, 2026: ~1 changed (`Metadata` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-11/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-11/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-11/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
