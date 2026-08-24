# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: August 24, 2026 · [daily report](docs/daily/2026-08-24.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+400` net · `+3` objects · `~13` objects · `+430` atoms · `-12` atoms · 4 active days | `+2,351` net · `+31` objects · `~70` objects · `+2,387` atoms · `-12` atoms · 17 active days | AWS managed policies (7d, last changed [August 22, 2026](data/diffs/2026-08-22/aws-managed-policies.json)) |
| Azure | No movement | `~4` objects · 1 active day | Azure built-in roles (30d, last changed [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json)) |
| GCP | `+345` net · `+4` objects · `~53` objects · `+345` atoms · 2 active days | `+1,040` net · `+10` objects · `~161` objects · `+1,062` atoms · `-22` atoms · 5 active days | GCP predefined roles (7d, last changed [August 20, 2026](data/diffs/2026-08-20/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `-1` net · `~8` objects · `-1` object · `-1` atom · 5 active days | GitHub fine-grained PAT permissions (7d, last changed [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,582` | [August 22, 2026](data/diffs/2026-08-22/aws-managed-policies.json) | `+400` net · `+3` objects · `~13` objects · `+430` atoms · `-12` atoms · 4 active days | `+2,351` net · `+31` objects · `~70` objects · `+2,387` atoms · `-12` atoms · 17 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-24/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json) | No movement | `~4` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-24/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,374` | [August 20, 2026](data/diffs/2026-08-20/gcp-predefined-roles.json) | `+345` net · `+4` objects · `~53` objects · `+345` atoms · 2 active days | `+1,040` net · `+10` objects · `~161` objects · `+1,062` atoms · `-22` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-24/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-24/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json) | `~1` object · 1 active day | `~8` objects · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-24/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json) | No movement | `-1` net · `-1` object · `-1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-24/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,582` objects.
- Last 7 days: `+400` net · `+3` objects · `~13` objects · `+430` atoms · `-12` atoms · 4 active days.
- Last 30 days: `+2,351` net · `+31` objects · `~70` objects · `+2,387` atoms · `-12` atoms · 17 active days.
- Recent highlights: August 22, 2026: ~3 changed, +15 atoms (`AWSAgentRegistryServiceRolePolicy` (+14)); August 21, 2026: ~3 changed, +202 atoms, -10 atoms (`AWSSupportServiceRolePolicy` (+148)); August 20, 2026: +3 objects, ~6 changed, +208 atoms, -2 atoms (`NetworkSecurityManagerServiceRolePolicy` (+87 atoms), `AmazonLaunchWizardFullAccessV2` (+62, -2)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-24/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~4` objects · 1 active day.
- Recent highlights: August 12, 2026: ~4 changed (`Logic Apps Standard Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-24/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,374` objects.
- Last 7 days: `+345` net · `+4` objects · `~53` objects · `+345` atoms · 2 active days.
- Last 30 days: `+1,040` net · `+10` objects · `~161` objects · `+1,062` atoms · `-22` atoms · 5 active days.
- Recent highlights: August 20, 2026: +4 objects, ~51 changed, +345 atoms (`Cloud FTP Admin` (+20 atoms), `Security Admin` (+16)); August 18, 2026: ~2 changed (`Cloud Run SSH Read Only Beta` (metadata only)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-24/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `~8` objects · 5 active days.
- Recent highlights: August 22, 2026: ~1 changed (`Metadata` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-24/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `-1` net · `-1` object · `-1` atom · 1 active day.
- Recent highlights: July 31, 2026: -1 removed, -1 atoms (`models` (-1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-24/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-24/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
