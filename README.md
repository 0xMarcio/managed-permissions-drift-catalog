# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: June 27, 2026 · [daily report](docs/daily/2026-06-27.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+312` net · `+5` objects · `~7` objects · `+317` atoms · `-5` atoms · 6 active days | `+925` net · `+19` objects · `~55` objects · `+1,056` atoms · `-75` atoms · 19 active days | AWS managed policies (7d, last changed [June 27, 2026](data/diffs/2026-06-27/aws-managed-policies.json)) |
| Azure | `+4` net · `~5` objects · `+6` atoms · `-2` atoms · 1 active day | `-10` net · `+1` object · `~15` objects · `+32` atoms · `-6` atoms · 3 active days | Azure built-in roles (7d, last changed [June 21, 2026](data/diffs/2026-06-21/azure-built-in-roles.json)) |
| GCP | `+484` net · `+19` objects · `~66` objects · `+484` atoms · 2 active days | `+985` net · `+31` objects · `~143` objects · `+993` atoms · `-8` atoms · 4 active days | GCP predefined roles (7d, last changed [June 25, 2026](data/diffs/2026-06-25/gcp-predefined-roles.json)) |
| GitHub | `+1` net · `+1` object · `~1` object · `+1` atom · 2 active days | `+1` net · `+1` object · `~10` objects · `+1` atom · 5 active days | GitHub fine-grained PAT permissions (7d, last changed [June 26, 2026](data/diffs/2026-06-26/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,524` | [June 27, 2026](data/diffs/2026-06-27/aws-managed-policies.json) | `+312` net · `+5` objects · `~7` objects · `+317` atoms · `-5` atoms · 6 active days | `+925` net · `+19` objects · `~55` objects · `+1,056` atoms · `-75` atoms · 19 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-27/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `501` | [June 21, 2026](data/diffs/2026-06-21/azure-built-in-roles.json) | `+4` net · `~5` objects · `+6` atoms · `-2` atoms · 1 active day | `-10` net · `+1` object · `~15` objects · `+32` atoms · `-6` atoms · 3 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-27/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,343` | [June 25, 2026](data/diffs/2026-06-25/gcp-predefined-roles.json) | `+484` net · `+19` objects · `~66` objects · `+484` atoms · 2 active days | `+985` net · `+31` objects · `~143` objects · `+993` atoms · `-8` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-27/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-27/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [June 26, 2026](data/diffs/2026-06-26/github-fgpat-permissions.json) | `+1` net · `+1` object · `~1` object · `+1` atom · 2 active days | `+1` net · `+1` object · `~10` objects · `+1` atom · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-27/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-27/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,524` objects.
- Last 7 days: `+312` net · `+5` objects · `~7` objects · `+317` atoms · `-5` atoms · 6 active days.
- Last 30 days: `+925` net · `+19` objects · `~55` objects · `+1,056` atoms · `-75` atoms · 19 active days.
- Recent highlights: June 27, 2026: +1 objects, +36 atoms (`AmazonInspector2ThirdPartyServiceRolePolicy` (+36 atoms)); June 26, 2026: ~1 changed, +2 atoms (`AWSObservabilityAdminTelemetryEnablementServiceRolePolicy` (+2)); June 25, 2026: +1 objects, ~1 changed, +24 atoms, -5 atoms (`AIDevOpsAgentActionsPolicy` (+10 atoms), `AIDevOpsAgentAccessPolicy` (+14, -5)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-27/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `501` objects.
- Last 7 days: `+4` net · `~5` objects · `+6` atoms · `-2` atoms · 1 active day.
- Last 30 days: `-10` net · `+1` object · `~15` objects · `+32` atoms · `-6` atoms · 3 active days.
- Recent highlights: June 21, 2026: ~5 changed, +6 atoms, -2 atoms (`Foundry Owner` (+2)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-27/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,343` objects.
- Last 7 days: `+484` net · `+19` objects · `~66` objects · `+484` atoms · 2 active days.
- Last 30 days: `+985` net · `+31` objects · `~143` objects · `+993` atoms · `-8` atoms · 4 active days.
- Recent highlights: June 25, 2026: +9 objects, ~36 changed, +358 atoms (`Appengine Admin` (+30 atoms), `Chronicle SOAR Threat Manager` (+13)); June 23, 2026: +10 objects, ~30 changed, +126 atoms (`Data Studio Managed Storage Service Agent` (+11 atoms), `Dataplex Administrator` (+11)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-27/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `+1` net · `+1` object · `~1` object · `+1` atom · 2 active days.
- Last 30 days: `+1` net · `+1` object · `~10` objects · `+1` atom · 5 active days.
- Recent highlights: June 26, 2026: +1 objects, +1 atoms (`Code quality` (+1 atoms)); June 24, 2026: ~1 changed (`Administration` (+3)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-27/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-27/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-27/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
