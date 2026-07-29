# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: July 29, 2026 · [daily report](docs/daily/2026-07-29.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+363` net · `+6` objects · `~19` objects · `+363` atoms · 6 active days | `+2,154` net · `+29` objects · `~75` objects · `+2,195` atoms · `-23` atoms · 22 active days | AWS managed policies (7d, last changed [July 29, 2026](data/diffs/2026-07-29/aws-managed-policies.json)) |
| Azure | No movement | `+107` net · `+3` objects · `~4` objects · `+122` atoms · `-1` atom · 2 active days | Azure built-in roles (30d, last changed [July 15, 2026](data/diffs/2026-07-15/azure-built-in-roles.json)) |
| GCP | `+107` net · `+2` objects · `~38` objects · `+129` atoms · `-22` atoms · 1 active day | `+2,359` net · `+23` objects · `~256` objects · `+2,467` atoms · `-108` atoms · 5 active days | GCP predefined roles (7d, last changed [July 29, 2026](data/diffs/2026-07-29/gcp-predefined-roles.json)) |
| GitHub | `~4` objects · 2 active days | `~10` objects · 7 active days | GitHub fine-grained PAT permissions (7d, last changed [July 28, 2026](data/diffs/2026-07-28/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,553` | [July 29, 2026](data/diffs/2026-07-29/aws-managed-policies.json) | `+363` net · `+6` objects · `~19` objects · `+363` atoms · 6 active days | `+2,154` net · `+29` objects · `~75` objects · `+2,195` atoms · `-23` atoms · 22 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-29/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [July 15, 2026](data/diffs/2026-07-15/azure-built-in-roles.json) | No movement | `+107` net · `+3` objects · `~4` objects · `+122` atoms · `-1` atom · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-29/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,366` | [July 29, 2026](data/diffs/2026-07-29/gcp-predefined-roles.json) | `+107` net · `+2` objects · `~38` objects · `+129` atoms · `-22` atoms · 1 active day | `+2,359` net · `+23` objects · `~256` objects · `+2,467` atoms · `-108` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-29/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-29/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [July 28, 2026](data/diffs/2026-07-28/github-fgpat-permissions.json) | `~4` objects · 2 active days | `~9` objects · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-29/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [July 21, 2026](data/diffs/2026-07-21/github-token-permissions.json) | No movement | `~1` object · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-29/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,553` objects.
- Last 7 days: `+363` net · `+6` objects · `~19` objects · `+363` atoms · 6 active days.
- Last 30 days: `+2,154` net · `+29` objects · `~75` objects · `+2,195` atoms · `-23` atoms · 22 active days.
- Recent highlights: July 29, 2026: ~4 changed, +4 atoms (`AWSTransformSecurityAgentExecutorAccess` (+2)); July 28, 2026: +1 objects, +33 atoms (`ROSAKarpenterControllerPolicy` (+33 atoms)); July 26, 2026: +1 objects, ~2 changed, +35 atoms (`AWSSDMPServiceRolePolicy` (+32 atoms), `AWSObservabilityAdminTelemetryEnablementServiceRolePolicy` (+2)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-29/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `+107` net · `+3` objects · `~4` objects · `+122` atoms · `-1` atom · 2 active days.
- Recent highlights: July 15, 2026: +2 objects, +110 atoms (`Azure Local Migrate Owner` (+64 atoms)); July 2, 2026: +1 objects, ~4 changed, +12 atoms, -1 atoms (`Azure Device Registry Administrator` (+1 atoms), `Container Registry Configuration Reader and Data Access Configuration Reader` (+6)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-29/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,366` objects.
- Last 7 days: `+107` net · `+2` objects · `~38` objects · `+129` atoms · `-22` atoms · 1 active day.
- Last 30 days: `+2,359` net · `+23` objects · `~256` objects · `+2,467` atoms · `-108` atoms · 5 active days.
- Recent highlights: July 29, 2026: +2 objects, ~38 changed, +129 atoms, -22 atoms (`AI Platform Editor` (+37 atoms), `Cloud Composer API Service Agent` (+6)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-29/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~4` objects · 2 active days.
- Last 30 days: `~9` objects · 6 active days.
- Recent highlights: July 28, 2026: ~2 changed (`Issues` (+3)); July 25, 2026: ~2 changed (`Contents` (+2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-29/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `~1` object · 1 active day.
- Recent highlights: July 21, 2026: ~1 changed (`code-quality` (metadata only)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-29/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-29/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
