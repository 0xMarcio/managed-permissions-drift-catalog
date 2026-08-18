# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: August 18, 2026 · [daily report](docs/daily/2026-08-18.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+1,533` net · `+16` objects · `~32` objects · `+1,533` atoms · 5 active days | `+2,394` net · `+38` objects · `~76` objects · `+2,400` atoms · 19 active days | AWS managed policies (7d, last changed [August 18, 2026](data/diffs/2026-08-18/aws-managed-policies.json)) |
| Azure | `~4` objects · 1 active day | `~4` objects · 1 active day | Azure built-in roles (7d, last changed [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json)) |
| GCP | `+453` net · `+3` objects · `~34` objects · `+453` atoms · 2 active days | `+968` net · `+8` objects · `~163` objects · `+1,010` atoms · `-42` atoms · 5 active days | GCP predefined roles (7d, last changed [August 18, 2026](data/diffs/2026-08-18/gcp-predefined-roles.json)) |
| GitHub | No movement | `-1` net · `~10` objects · `-1` object · `-1` atom · 6 active days | GitHub GITHUB_TOKEN permissions (30d, last changed [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,579` | [August 18, 2026](data/diffs/2026-08-18/aws-managed-policies.json) | `+1,533` net · `+16` objects · `~32` objects · `+1,533` atoms · 5 active days | `+2,394` net · `+38` objects · `~76` objects · `+2,400` atoms · 19 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-18/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json) | `~4` objects · 1 active day | `~4` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-18/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,370` | [August 18, 2026](data/diffs/2026-08-18/gcp-predefined-roles.json) | `+453` net · `+3` objects · `~34` objects · `+453` atoms · 2 active days | `+968` net · `+8` objects · `~163` objects · `+1,010` atoms · `-42` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-18/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-18/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [August 7, 2026](data/diffs/2026-08-07/github-fgpat-permissions.json) | No movement | `~9` objects · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-18/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [July 31, 2026](data/diffs/2026-07-31/github-token-permissions.json) | No movement | `-1` net · `~1` object · `-1` object · `-1` atom · 2 active days | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-18/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,579` objects.
- Last 7 days: `+1,533` net · `+16` objects · `~32` objects · `+1,533` atoms · 5 active days.
- Last 30 days: `+2,394` net · `+38` objects · `~76` objects · `+2,400` atoms · 19 active days.
- Recent highlights: August 18, 2026: ~1 changed, +5 atoms (`SecurityAudit` (+5)); August 16, 2026: ~5 changed, +23 atoms (`AWSSupplyChainFederationAdminAccess` (+6)); August 15, 2026: ~5 changed, +17 atoms (`AWSManagedSettingsAdminAccess` (+9)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-08-18/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: `~4` objects · 1 active day.
- Last 30 days: `~4` objects · 1 active day.
- Recent highlights: August 12, 2026: ~4 changed (`Logic Apps Standard Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-08-18/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,370` objects.
- Last 7 days: `+453` net · `+3` objects · `~34` objects · `+453` atoms · 2 active days.
- Last 30 days: `+968` net · `+8` objects · `~163` objects · `+1,010` atoms · `-42` atoms · 5 active days.
- Recent highlights: August 18, 2026: ~2 changed (`Cloud Run SSH Read Only Beta` (metadata only)); August 14, 2026: +3 objects, ~32 changed, +453 atoms (`ProdActuation API Admin Beta` (+23 atoms), `App Management Viewer Beta` (+46)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-08-18/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: No movement.
- Last 30 days: `~9` objects · 5 active days.
- Recent highlights: August 7, 2026: ~1 changed (`Administration` (+1)); July 31, 2026: ~3 changed (`Pull requests` (+5)); July 30, 2026: ~1 changed (`Artifact metadata` (+2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-08-18/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `-1` net · `~1` object · `-1` object · `-1` atom · 2 active days.
- Recent highlights: July 31, 2026: -1 removed, -1 atoms (`models` (-1 atoms)); July 21, 2026: ~1 changed (`code-quality` (metadata only)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-08-18/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-08-18/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
