# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: August 25, 2026 · [daily report](docs/daily/2026-08-25.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+411` net · `+4` objects · `~16` objects · `+441` atoms · `-12` atoms · 4 active days | `+2,332` net · `+31` objects · `~72` objects · `+2,368` atoms · `-12` atoms · 17 active days | AWS managed policies (7d, last changed [August 25, 2026](data/diffs/2026-08-25/aws-managed-policies.json)) |
| Azure | No movement | `~4` objects · 1 active day | Azure built-in roles (30d, last changed [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json)) |
| GCP | `+345` net · `+4` objects · `~51` objects · `+345` atoms · 1 active day | `+1,040` net · `+10` objects · `~161` objects · `+1,062` atoms · `-22` atoms · 5 active days | GCP predefined roles (7d, last changed [August 20, 2026](data/diffs/2026-08-20/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `-1` net · `~8` objects · `-1` object · `-1` atom · 5 active days | GitHub fine-grained PAT permissions (7d, last changed [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,583` | [August 25, 2026](data/diffs/2026-08-25/aws-managed-policies.json) | `+411` net · `+4` objects · `~16` objects · `+441` atoms · `-12` atoms · 4 active days | `+2,332` net · `+31` objects · `~72` objects · `+2,368` atoms · `-12` atoms · 17 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-25/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json) | No movement | `~4` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-25/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,374` | [August 20, 2026](data/diffs/2026-08-20/gcp-predefined-roles.json) | `+345` net · `+4` objects · `~51` objects · `+345` atoms · 1 active day | `+1,040` net · `+10` objects · `~161` objects · `+1,062` atoms · `-22` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-25/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-25/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json) | `~1` object · 1 active day | `~8` objects · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-25/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json) | No movement | `-1` net · `-1` object · `-1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-25/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,583` objects.
- Last 7 days: `+411` net · `+4` objects · `~16` objects · `+441` atoms · `-12` atoms · 4 active days.
- Last 30 days: `+2,332` net · `+31` objects · `~72` objects · `+2,368` atoms · `-12` atoms · 17 active days.
- Recent highlights: August 25, 2026: +1 objects, ~4 changed, +16 atoms (`AIDevOpsReleaseManagementVPCPolicy` (+10 atoms), `AWSManagedSettingsReadOnlyAccess` (+2)); August 22, 2026: ~3 changed, +15 atoms (`AWSAgentRegistryServiceRolePolicy` (+14)); August 21, 2026: ~3 changed, +202 atoms, -10 atoms (`AWSSupportServiceRolePolicy` (+148)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-25/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~4` objects · 1 active day.
- Recent highlights: August 12, 2026: ~4 changed (`Logic Apps Standard Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-25/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,374` objects.
- Last 7 days: `+345` net · `+4` objects · `~51` objects · `+345` atoms · 1 active day.
- Last 30 days: `+1,040` net · `+10` objects · `~161` objects · `+1,062` atoms · `-22` atoms · 5 active days.
- Recent highlights: August 20, 2026: +4 objects, ~51 changed, +345 atoms (`Cloud FTP Admin` (+20 atoms), `Security Admin` (+16)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-25/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `~8` objects · 5 active days.
- Recent highlights: August 22, 2026: ~1 changed (`Metadata` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-25/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `-1` net · `-1` object · `-1` atom · 1 active day.
- Recent highlights: July 31, 2026: -1 removed, -1 atoms (`models` (-1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-25/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-25/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
