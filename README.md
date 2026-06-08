# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: June 8, 2026 · [daily report](docs/daily/2026-06-08.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+337` net · `+9` objects · `~21` objects · `+380` atoms · `-7` atoms · 3 active days | `+466` net · `+14` objects · `~64` objects · `+738` atoms · `-188` atoms · 19 active days | AWS managed policies (7d, last changed [June 7, 2026](data/diffs/2026-06-07/aws-managed-policies.json)) |
| Azure | `-14` net · `~10` objects · `+22` atoms · `-4` atoms · 1 active day | `+4` net · `+3` objects · `~19` objects · `+44` atoms · `-4` atoms · 5 active days | Azure built-in roles (7d, last changed [June 3, 2026](data/diffs/2026-06-03/azure-built-in-roles.json)) |
| GCP | `+235` net · `+11` objects · `~26` objects · `+235` atoms · 1 active day | `+1,867` net · `+40` objects · `~319` objects · `-1` object · `+1,929` atoms · `-62` atoms · 5 active days | GCP predefined roles (7d, last changed [June 4, 2026](data/diffs/2026-06-04/gcp-predefined-roles.json)) |
| GitHub | `~4` objects · 2 active days | `+16` net · `+6` objects · `~9` objects · `+11` atoms · 5 active days | GitHub fine-grained PAT permissions (7d, last changed [June 4, 2026](data/diffs/2026-06-04/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,515` | [June 7, 2026](data/diffs/2026-06-07/aws-managed-policies.json) | `+337` net · `+9` objects · `~21` objects · `+380` atoms · `-7` atoms · 3 active days | `+466` net · `+14` objects · `~64` objects · `+738` atoms · `-188` atoms · 19 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-08/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `501` | [June 3, 2026](data/diffs/2026-06-03/azure-built-in-roles.json) | `-14` net · `~10` objects · `+22` atoms · `-4` atoms · 1 active day | `+4` net · `+3` objects · `~19` objects · `+44` atoms · `-4` atoms · 5 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-08/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,323` | [June 4, 2026](data/diffs/2026-06-04/gcp-predefined-roles.json) | `+235` net · `+11` objects · `~26` objects · `+235` atoms · 1 active day | `+1,867` net · `+40` objects · `~319` objects · `-1` object · `+1,929` atoms · `-62` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-08/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-08/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `72` | [June 4, 2026](data/diffs/2026-06-04/github-fgpat-permissions.json) | `~4` objects · 2 active days | `+13` net · `+5` objects · `~9` objects · `+9` atoms · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-08/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [May 12, 2026](data/diffs/2026-05-12/github-token-permissions.json) | No movement | `+3` net · `+1` object · `+2` atoms · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-08/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,515` objects.
- Last 7 days: `+337` net · `+9` objects · `~21` objects · `+380` atoms · `-7` atoms · 3 active days.
- Last 30 days: `+466` net · `+14` objects · `~64` objects · `+738` atoms · `-188` atoms · 19 active days.
- Recent highlights: June 7, 2026: ~4 changed, +47 atoms (`AIDevOpsAgentFullAccess` (+19)); June 6, 2026: +3 objects, ~8 changed, +219 atoms, -7 atoms (`FinOpsAgentAgentPolicy` (+81 atoms), `SageMakerStudioAdminIAMDefaultExecutionPolicy` (+11)); June 4, 2026: +6 objects, ~9 changed, +114 atoms (`AmazonSageMakerJobFullAccess` (+42 atoms), `AWSQuickSetupManagedInstanceProfileExecutionPolicy` (+5)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-08/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `501` objects.
- Last 7 days: `-14` net · `~10` objects · `+22` atoms · `-4` atoms · 1 active day.
- Last 30 days: `+4` net · `+3` objects · `~19` objects · `+44` atoms · `-4` atoms · 5 active days.
- Recent highlights: June 3, 2026: ~10 changed, +22 atoms, -4 atoms (`Cosmos DB Operator` (+16)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-08/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,323` objects.
- Last 7 days: `+235` net · `+11` objects · `~26` objects · `+235` atoms · 1 active day.
- Last 30 days: `+1,867` net · `+40` objects · `~319` objects · `-1` object · `+1,929` atoms · `-62` atoms · 5 active days.
- Recent highlights: June 4, 2026: +11 objects, ~26 changed, +235 atoms (`Connectors Editor` (+73 atoms), `Vertex AI Service Agent` (+9)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-08/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `72` objects.
- Last 7 days: `~4` objects · 2 active days.
- Last 30 days: `+13` net · `+5` objects · `~9` objects · `+9` atoms · 5 active days.
- Recent highlights: June 4, 2026: ~1 changed (`Administration` (+1)); June 3, 2026: ~3 changed (`Administration` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-08/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+3` net · `+1` object · `+2` atoms · 1 active day.
- Recent highlights: May 12, 2026: +1 objects, +2 atoms (`code-quality` (+2 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-08/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-08/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
