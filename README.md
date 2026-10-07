# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: October 7, 2026 · [daily report](docs/daily/2026-10-07.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+1,318` net · `+3` objects · `~18` objects · `+1,318` atoms · 6 active days | `+5,431` net · `+17` objects · `~73` objects · `-1` object · `+5,448` atoms · `-11` atoms · 21 active days | AWS managed policies (7d, last changed [October 7, 2026](data/diffs/2026-10-07/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | No movement | `+1,349` net · `+18` objects · `~238` objects · `-6` objects · `+1,408` atoms · `-59` atoms · 3 active days | GCP predefined roles (30d, last changed [September 30, 2026](data/diffs/2026-09-30/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `+7` net · `+3` objects · `~11` objects · `+3` atoms · 7 active days | GitHub fine-grained PAT permissions (7d, last changed [October 6, 2026](data/diffs/2026-10-06/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,601` | [October 7, 2026](data/diffs/2026-10-07/aws-managed-policies.json) | `+1,318` net · `+3` objects · `~18` objects · `+1,318` atoms · 6 active days | `+5,431` net · `+17` objects · `~73` objects · `-1` object · `+5,448` atoms · `-11` atoms · 21 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-07/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-07/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,386` | [September 30, 2026](data/diffs/2026-09-30/gcp-predefined-roles.json) | No movement | `+1,349` net · `+18` objects · `~238` objects · `-6` objects · `+1,408` atoms · `-59` atoms · 3 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-07/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-07/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 6, 2026](data/diffs/2026-10-06/github-fgpat-permissions.json) | `~1` object · 1 active day | `+7` net · `+3` objects · `~11` objects · `+3` atoms · 7 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-07/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-07/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,601` objects.
- Last 7 days: `+1,318` net · `+3` objects · `~18` objects · `+1,318` atoms · 6 active days.
- Last 30 days: `+5,431` net · `+17` objects · `~73` objects · `-1` object · `+5,448` atoms · `-11` atoms · 21 active days.
- Recent highlights: October 7, 2026: ~2 changed, +3 atoms (`AWSObservabilityAdminTelemetryEnablementServiceRolePolicy` (+3)); October 6, 2026: +1 objects, +6 atoms (`AWSSecurityAgentContinuousPentestPolicy` (+6 atoms)); October 4, 2026: ~3 changed, +8 atoms (`FinOpsAgentAgentPolicy` (+4)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-07/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-07/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,386` objects.
- Last 7 days: No movement.
- Last 30 days: `+1,349` net · `+18` objects · `~238` objects · `-6` objects · `+1,408` atoms · `-59` atoms · 3 active days.
- Recent highlights: September 30, 2026: +5 objects, ~67 changed, -6 removed, +367 atoms, -53 atoms (`Database Insights Service Agent` (+71 atoms), `Security Admin` (+13, -2)); September 23, 2026: +6 objects, ~43 changed, +265 atoms (`Universal Ledger Admin Beta` (+6 atoms), `SaaS Service Management Service Agent` (+23)); September 16, 2026: +7 objects, ~128 changed, +776 atoms, -6 atoms (`Resource Manager Editor` (+41 atoms), `DLP Organization Data Profiles Driver` (+35)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-07/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `+7` net · `+3` objects · `~11` objects · `+3` atoms · 7 active days.
- Recent highlights: October 6, 2026: ~1 changed (`Pull requests` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-07/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-07/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-07/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
