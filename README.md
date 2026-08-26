# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: August 26, 2026 · [daily report](docs/daily/2026-08-26.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+428` net · `+4` objects · `~21` objects · `+458` atoms · `-12` atoms · 5 active days | `+2,349` net · `+31` objects · `~77` objects · `+2,385` atoms · `-12` atoms · 18 active days | AWS managed policies (7d, last changed [August 26, 2026](data/diffs/2026-08-26/aws-managed-policies.json)) |
| Azure | No movement | `~4` objects · 1 active day | Azure built-in roles (30d, last changed [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json)) |
| GCP | `+426` net · `+5` objects · `~100` objects · `+435` atoms · `-9` atoms · 2 active days | `+1,121` net · `+11` objects · `~210` objects · `+1,152` atoms · `-31` atoms · 6 active days | GCP predefined roles (7d, last changed [August 26, 2026](data/diffs/2026-08-26/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `-1` net · `~8` objects · `-1` object · `-1` atom · 5 active days | GitHub fine-grained PAT permissions (7d, last changed [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,583` | [August 26, 2026](data/diffs/2026-08-26/aws-managed-policies.json) | `+428` net · `+4` objects · `~21` objects · `+458` atoms · `-12` atoms · 5 active days | `+2,349` net · `+31` objects · `~77` objects · `+2,385` atoms · `-12` atoms · 18 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-26/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json) | No movement | `~4` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-26/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,375` | [August 26, 2026](data/diffs/2026-08-26/gcp-predefined-roles.json) | `+426` net · `+5` objects · `~100` objects · `+435` atoms · `-9` atoms · 2 active days | `+1,121` net · `+11` objects · `~210` objects · `+1,152` atoms · `-31` atoms · 6 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-26/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-26/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json) | `~1` object · 1 active day | `~8` objects · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-26/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json) | No movement | `-1` net · `-1` object · `-1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-26/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,583` objects.
- Last 7 days: `+428` net · `+4` objects · `~21` objects · `+458` atoms · `-12` atoms · 5 active days.
- Last 30 days: `+2,349` net · `+31` objects · `~77` objects · `+2,385` atoms · `-12` atoms · 18 active days.
- Recent highlights: August 26, 2026: ~5 changed, +17 atoms (`AWSSupportPlansFullAccess` (+10)); August 25, 2026: +1 objects, ~4 changed, +16 atoms (`AIDevOpsReleaseManagementVPCPolicy` (+10 atoms), `AWSManagedSettingsReadOnlyAccess` (+2)); August 22, 2026: ~3 changed, +15 atoms (`AWSAgentRegistryServiceRolePolicy` (+14)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-26/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~4` objects · 1 active day.
- Recent highlights: August 12, 2026: ~4 changed (`Logic Apps Standard Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-26/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,375` objects.
- Last 7 days: `+426` net · `+5` objects · `~100` objects · `+435` atoms · `-9` atoms · 2 active days.
- Last 30 days: `+1,121` net · `+11` objects · `~210` objects · `+1,152` atoms · `-31` atoms · 6 active days.
- Recent highlights: August 26, 2026: +1 objects, ~49 changed, +90 atoms, -9 atoms (`Analytics Hub Service Agent` (+3 atoms), `Chronicle Service Agent` (+10)); August 20, 2026: +4 objects, ~51 changed, +345 atoms (`Cloud FTP Admin` (+20 atoms), `Security Admin` (+16)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-26/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `~8` objects · 5 active days.
- Recent highlights: August 22, 2026: ~1 changed (`Metadata` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-26/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `-1` net · `-1` object · `-1` atom · 1 active day.
- Recent highlights: July 31, 2026: -1 removed, -1 atoms (`models` (-1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-26/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-26/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
