# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: September 19, 2026 · [daily report](docs/daily/2026-09-19.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+729` net · `+1` object · `~7` objects · `+729` atoms · 4 active days | `+2,039` net · `+9` objects · `~77` objects · `+2,067` atoms · `-10` atoms · 20 active days | AWS managed policies (7d, last changed [September 19, 2026](data/diffs/2026-09-19/aws-managed-policies.json)) |
| Azure | No movement | `~3` objects · 1 active day | Azure built-in roles (30d, last changed [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json)) |
| GCP | `+770` net · `+7` objects · `~128` objects · `+776` atoms · `-6` atoms · 1 active day | `+1,149` net · `+9` objects · `~259` objects · `-2` objects · `+1,216` atoms · `-67` atoms · 3 active days | GCP predefined roles (7d, last changed [September 16, 2026](data/diffs/2026-09-16/gcp-predefined-roles.json)) |
| GitHub | `~2` objects · 1 active day | `~11` objects · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [September 17, 2026](data/diffs/2026-09-17/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,591` | [September 19, 2026](data/diffs/2026-09-19/aws-managed-policies.json) | `+729` net · `+1` object · `~7` objects · `+729` atoms · 4 active days | `+2,039` net · `+9` objects · `~77` objects · `+2,067` atoms · `-10` atoms · 20 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-19/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json) | No movement | `~3` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-19/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,381` | [September 16, 2026](data/diffs/2026-09-16/gcp-predefined-roles.json) | `+770` net · `+7` objects · `~128` objects · `+776` atoms · `-6` atoms · 1 active day | `+1,149` net · `+9` objects · `~259` objects · `-2` objects · `+1,216` atoms · `-67` atoms · 3 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-19/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-19/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [September 17, 2026](data/diffs/2026-09-17/github-fgpat-permissions.json) | `~2` objects · 1 active day | `~11` objects · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-19/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-19/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,591` objects.
- Last 7 days: `+729` net · `+1` object · `~7` objects · `+729` atoms · 4 active days.
- Last 30 days: `+2,039` net · `+9` objects · `~77` objects · `+2,067` atoms · `-10` atoms · 20 active days.
- Recent highlights: September 19, 2026: ~1 changed, +1 atoms (`ROSAKubeControllerPolicy` (+1)); September 17, 2026: +1 objects, ~2 changed, +18 atoms (`AWSWellArchitectedAgentOrganizationsServiceRolePolicy` (+11 atoms), `ReadOnlyAccess` (+7)); September 16, 2026: ~3 changed, +708 atoms (`AWSResourceExplorerServiceRolePolicy` (+706)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-19/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~3` objects · 1 active day.
- Recent highlights: September 4, 2026: ~3 changed (`Search Index Data Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-19/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,381` objects.
- Last 7 days: `+770` net · `+7` objects · `~128` objects · `+776` atoms · `-6` atoms · 1 active day.
- Last 30 days: `+1,149` net · `+9` objects · `~259` objects · `-2` objects · `+1,216` atoms · `-67` atoms · 3 active days.
- Recent highlights: September 16, 2026: +7 objects, ~128 changed, +776 atoms, -6 atoms (`Resource Manager Editor` (+41 atoms), `DLP Organization Data Profiles Driver` (+35)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-19/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~2` objects · 1 active day.
- Last 30 days: `~11` objects · 6 active days.
- Recent highlights: September 17, 2026: ~2 changed (`Administration` (+5)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-19/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-19/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-19/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
