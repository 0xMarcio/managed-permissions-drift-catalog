# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: July 4, 2026 · [daily report](docs/daily/2026-07-04.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+281` net · `+9` objects · `~28` objects · `+304` atoms · `-21` atoms · 6 active days | `+1,143` net · `+21` objects · `~67` objects · `+1,210` atoms · `-33` atoms · 21 active days | AWS managed policies (7d, last changed [July 4, 2026](data/diffs/2026-07-04/aws-managed-policies.json)) |
| Azure | `+9` net · `+1` object · `~4` objects · `+12` atoms · `-1` atom · 1 active day | `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days | Azure built-in roles (7d, last changed [July 2, 2026](data/diffs/2026-07-02/azure-built-in-roles.json)) |
| GCP | `+195` net · `+6` objects · `~55` objects · `+196` atoms · `-1` atom · 1 active day | `+945` net · `+26` objects · `~172` objects · `+954` atoms · `-9` atoms · 4 active days | GCP predefined roles (7d, last changed [July 1, 2026](data/diffs/2026-07-01/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days | GitHub fine-grained PAT permissions (7d, last changed [June 30, 2026](data/diffs/2026-06-30/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,533` | [July 4, 2026](data/diffs/2026-07-04/aws-managed-policies.json) | `+281` net · `+9` objects · `~28` objects · `+304` atoms · `-21` atoms · 6 active days | `+1,143` net · `+21` objects · `~67` objects · `+1,210` atoms · `-33` atoms · 21 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-04/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `502` | [July 2, 2026](data/diffs/2026-07-02/azure-built-in-roles.json) | `+9` net · `+1` object · `~4` objects · `+12` atoms · `-1` atom · 1 active day | `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-04/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,349` | [July 1, 2026](data/diffs/2026-07-01/gcp-predefined-roles.json) | `+195` net · `+6` objects · `~55` objects · `+196` atoms · `-1` atom · 1 active day | `+945` net · `+26` objects · `~172` objects · `+954` atoms · `-9` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-04/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-04/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [June 30, 2026](data/diffs/2026-06-30/github-fgpat-permissions.json) | `~1` object · 1 active day | `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-04/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-04/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,533` objects.
- Last 7 days: `+281` net · `+9` objects · `~28` objects · `+304` atoms · `-21` atoms · 6 active days.
- Last 30 days: `+1,143` net · `+21` objects · `~67` objects · `+1,210` atoms · `-33` atoms · 21 active days.
- Recent highlights: July 4, 2026: +3 objects, ~2 changed, +50 atoms (`AWSElasticBeanstalkEKSImageBuild` (+15 atoms), `AIDevOpsAgentAccessPolicy` (+13)); July 3, 2026: ~1 changed (`AmazonECSInstanceRolePolicyForManagedInstances` (metadata only)); July 2, 2026: +4 objects, ~8 changed, +98 atoms (`AWSPartnerCentralRevenueAttributionManagement` (+29 atoms), `AWSResourceExplorerServiceRolePolicy` (+29)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-04/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `502` objects.
- Last 7 days: `+9` net · `+1` object · `~4` objects · `+12` atoms · `-1` atom · 1 active day.
- Last 30 days: `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days.
- Recent highlights: July 2, 2026: +1 objects, ~4 changed, +12 atoms, -1 atoms (`Azure Device Registry Administrator` (+1 atoms), `Container Registry Configuration Reader and Data Access Configuration Reader` (+6)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-04/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,349` objects.
- Last 7 days: `+195` net · `+6` objects · `~55` objects · `+196` atoms · `-1` atom · 1 active day.
- Last 30 days: `+945` net · `+26` objects · `~172` objects · `+954` atoms · `-9` atoms · 4 active days.
- Recent highlights: July 1, 2026: +6 objects, ~55 changed, +196 atoms, -1 atoms (`Dataplex Data Domain Admin Beta` (+16 atoms), `Dataplex Administrator` (+14)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-04/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days.
- Recent highlights: June 30, 2026: ~1 changed (`Administration` (+1, -1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-04/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-04/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-04/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
