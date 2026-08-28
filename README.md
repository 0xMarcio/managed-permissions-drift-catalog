# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: August 28, 2026 · [daily report](docs/daily/2026-08-28.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+444` net · `+3` objects · `~16` objects · `+444` atoms · 5 active days | `+2,708` net · `+32` objects · `~77` objects · `+2,744` atoms · `-12` atoms · 18 active days | AWS managed policies (7d, last changed [August 28, 2026](data/diffs/2026-08-28/aws-managed-policies.json)) |
| Azure | No movement | `~4` objects · 1 active day | Azure built-in roles (30d, last changed [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json)) |
| GCP | `+81` net · `+1` object · `~49` objects · `+90` atoms · `-9` atoms · 1 active day | `+1,014` net · `+9` objects · `~172` objects · `+1,023` atoms · `-9` atoms · 5 active days | GCP predefined roles (7d, last changed [August 26, 2026](data/diffs/2026-08-26/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `-1` net · `~6` objects · `-1` object · `-1` atom · 4 active days | GitHub fine-grained PAT permissions (7d, last changed [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,585` | [August 28, 2026](data/diffs/2026-08-28/aws-managed-policies.json) | `+444` net · `+3` objects · `~16` objects · `+444` atoms · 5 active days | `+2,708` net · `+32` objects · `~77` objects · `+2,744` atoms · `-12` atoms · 18 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-28/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json) | No movement | `~4` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-28/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,375` | [August 26, 2026](data/diffs/2026-08-26/gcp-predefined-roles.json) | `+81` net · `+1` object · `~49` objects · `+90` atoms · `-9` atoms · 1 active day | `+1,014` net · `+9` objects · `~172` objects · `+1,023` atoms · `-9` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-28/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-28/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json) | `~1` object · 1 active day | `~6` objects · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-28/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json) | No movement | `-1` net · `-1` object · `-1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-28/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,585` objects.
- Last 7 days: `+444` net · `+3` objects · `~16` objects · `+444` atoms · 5 active days.
- Last 30 days: `+2,708` net · `+32` objects · `~77` objects · `+2,744` atoms · `-12` atoms · 18 active days.
- Recent highlights: August 28, 2026: +2 objects, ~1 changed, +392 atoms (`AssuranceServiceRolePolicy` (+388 atoms), `SageMakerStudioAdminIAMConsolePolicy` (+2)); August 27, 2026: ~3 changed, +4 atoms (`SecretsManagerReadWrite` (+2)); August 26, 2026: ~5 changed, +17 atoms (`AWSSupportPlansFullAccess` (+10)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-28/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~4` objects · 1 active day.
- Recent highlights: August 12, 2026: ~4 changed (`Logic Apps Standard Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-28/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,375` objects.
- Last 7 days: `+81` net · `+1` object · `~49` objects · `+90` atoms · `-9` atoms · 1 active day.
- Last 30 days: `+1,014` net · `+9` objects · `~172` objects · `+1,023` atoms · `-9` atoms · 5 active days.
- Recent highlights: August 26, 2026: +1 objects, ~49 changed, +90 atoms, -9 atoms (`Analytics Hub Service Agent` (+3 atoms), `Chronicle Service Agent` (+10)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-28/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `~6` objects · 4 active days.
- Recent highlights: August 22, 2026: ~1 changed (`Metadata` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-28/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `-1` net · `-1` object · `-1` atom · 1 active day.
- Recent highlights: July 31, 2026: -1 removed, -1 atoms (`models` (-1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-28/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-28/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
