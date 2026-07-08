# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: July 8, 2026 · [daily report](docs/daily/2026-07-08.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+197` net · `+9` objects · `~15` objects · `+197` atoms · 4 active days | `+965` net · `+20` objects · `~59` objects · `+993` atoms · `-26` atoms · 20 active days | AWS managed policies (7d, last changed [July 8, 2026](data/diffs/2026-07-08/aws-managed-policies.json)) |
| Azure | `+9` net · `+1` object · `~4` objects · `+12` atoms · `-1` atom · 1 active day | `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days | Azure built-in roles (7d, last changed [July 2, 2026](data/diffs/2026-07-02/azure-built-in-roles.json)) |
| GCP | No movement | `+945` net · `+26` objects · `~172` objects · `+954` atoms · `-9` atoms · 4 active days | GCP predefined roles (30d, last changed [July 1, 2026](data/diffs/2026-07-01/gcp-predefined-roles.json)) |
| GitHub | No movement | `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days | GitHub fine-grained PAT permissions (30d, last changed [June 30, 2026](data/diffs/2026-06-30/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,535` | [July 8, 2026](data/diffs/2026-07-08/aws-managed-policies.json) | `+197` net · `+9` objects · `~15` objects · `+197` atoms · 4 active days | `+965` net · `+20` objects · `~59` objects · `+993` atoms · `-26` atoms · 20 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-08/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `502` | [July 2, 2026](data/diffs/2026-07-02/azure-built-in-roles.json) | `+9` net · `+1` object · `~4` objects · `+12` atoms · `-1` atom · 1 active day | `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-08/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,349` | [July 1, 2026](data/diffs/2026-07-01/gcp-predefined-roles.json) | No movement | `+945` net · `+26` objects · `~172` objects · `+954` atoms · `-9` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-08/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-08/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [June 30, 2026](data/diffs/2026-06-30/github-fgpat-permissions.json) | No movement | `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-08/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-08/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,535` objects.
- Last 7 days: `+197` net · `+9` objects · `~15` objects · `+197` atoms · 4 active days.
- Last 30 days: `+965` net · `+20` objects · `~59` objects · `+993` atoms · `-26` atoms · 20 active days.
- Recent highlights: July 8, 2026: +2 objects, ~4 changed, +49 atoms (`DBModVirtualSource` (+39 atoms), `AWSResilienceHubServiceRolePolicy` (+6)); July 4, 2026: +3 objects, ~2 changed, +50 atoms (`AWSElasticBeanstalkEKSImageBuild` (+15 atoms), `AIDevOpsAgentAccessPolicy` (+13)); July 3, 2026: ~1 changed (`AmazonECSInstanceRolePolicyForManagedInstances` (metadata only)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-08/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `502` objects.
- Last 7 days: `+9` net · `+1` object · `~4` objects · `+12` atoms · `-1` atom · 1 active day.
- Last 30 days: `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days.
- Recent highlights: July 2, 2026: +1 objects, ~4 changed, +12 atoms, -1 atoms (`Azure Device Registry Administrator` (+1 atoms), `Container Registry Configuration Reader and Data Access Configuration Reader` (+6)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-08/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,349` objects.
- Last 7 days: No movement.
- Last 30 days: `+945` net · `+26` objects · `~172` objects · `+954` atoms · `-9` atoms · 4 active days.
- Recent highlights: July 1, 2026: +6 objects, ~55 changed, +196 atoms, -1 atoms (`Dataplex Data Domain Admin Beta` (+16 atoms), `Dataplex Administrator` (+14)); June 25, 2026: +9 objects, ~36 changed, +358 atoms (`Appengine Admin` (+30 atoms), `Chronicle SOAR Threat Manager` (+13)); June 23, 2026: +10 objects, ~30 changed, +126 atoms (`Data Studio Managed Storage Service Agent` (+11 atoms), `Dataplex Administrator` (+11)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-08/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: No movement.
- Last 30 days: `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days.
- Recent highlights: June 30, 2026: ~1 changed (`Administration` (+1, -1)); June 26, 2026: +1 objects, +1 atoms (`Code quality` (+1 atoms)); June 24, 2026: ~1 changed (`Administration` (+3)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-08/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-08/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-08/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
