# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: July 19, 2026 · [daily report](docs/daily/2026-07-19.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+1,227` net · `+5` objects · `~12` objects · `+1,247` atoms · `-2` atoms · 4 active days | `+2,012` net · `+22` objects · `~69` objects · `+2,060` atoms · `-28` atoms · 22 active days | AWS managed policies (7d, last changed [July 19, 2026](data/diffs/2026-07-19/aws-managed-policies.json)) |
| Azure | `+98` net · `+2` objects · `+110` atoms · 1 active day | `+111` net · `+3` objects · `~9` objects · `+128` atoms · `-3` atoms · 3 active days | Azure built-in roles (7d, last changed [July 15, 2026](data/diffs/2026-07-15/azure-built-in-roles.json)) |
| GCP | `+109` net · `~41` objects · `+169` atoms · `-60` atoms · 1 active day | `+2,463` net · `+38` objects · `~231` objects · `+2,529` atoms · `-66` atoms · 5 active days | GCP predefined roles (7d, last changed [July 15, 2026](data/diffs/2026-07-15/gcp-predefined-roles.json)) |
| GitHub | `~3` objects · 2 active days | `+1` net · `+1` object · `~6` objects · `+1` atom · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [July 19, 2026](data/diffs/2026-07-19/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,541` | [July 19, 2026](data/diffs/2026-07-19/aws-managed-policies.json) | `+1,227` net · `+5` objects · `~12` objects · `+1,247` atoms · `-2` atoms · 4 active days | `+2,012` net · `+22` objects · `~69` objects · `+2,060` atoms · `-28` atoms · 22 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-19/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [July 15, 2026](data/diffs/2026-07-15/azure-built-in-roles.json) | `+98` net · `+2` objects · `+110` atoms · 1 active day | `+111` net · `+3` objects · `~9` objects · `+128` atoms · `-3` atoms · 3 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-19/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,362` | [July 15, 2026](data/diffs/2026-07-15/gcp-predefined-roles.json) | `+109` net · `~41` objects · `+169` atoms · `-60` atoms · 1 active day | `+2,463` net · `+38` objects · `~231` objects · `+2,529` atoms · `-66` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-19/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-19/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [July 19, 2026](data/diffs/2026-07-19/github-fgpat-permissions.json) | `~3` objects · 2 active days | `+1` net · `+1` object · `~6` objects · `+1` atom · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-19/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-19/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,541` objects.
- Last 7 days: `+1,227` net · `+5` objects · `~12` objects · `+1,247` atoms · `-2` atoms · 4 active days.
- Last 30 days: `+2,012` net · `+22` objects · `~69` objects · `+2,060` atoms · `-28` atoms · 22 active days.
- Recent highlights: July 19, 2026: +3 objects, ~2 changed, +102 atoms (`AWSBudgetsSpendLimitMemberRolePolicy` (+85 atoms), `AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy` (+2)); July 18, 2026: +1 objects, ~2 changed, +1,118 atoms (`WellArchitectedAgentResourceScanning` (+1,117 atoms), `AmazonPrometheusScraperServiceRolePolicy` (+1)); July 17, 2026: +1 objects, ~2 changed, +6 atoms (`AWSIAMRoleManagerServiceRolePolicy` (+2 atoms), `SecurityLakeServiceLinkedRole` (+3)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-19/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: `+98` net · `+2` objects · `+110` atoms · 1 active day.
- Last 30 days: `+111` net · `+3` objects · `~9` objects · `+128` atoms · `-3` atoms · 3 active days.
- Recent highlights: July 15, 2026: +2 objects, +110 atoms (`Azure Local Migrate Owner` (+64 atoms)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-19/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,362` objects.
- Last 7 days: `+109` net · `~41` objects · `+169` atoms · `-60` atoms · 1 active day.
- Last 30 days: `+2,463` net · `+38` objects · `~231` objects · `+2,529` atoms · `-66` atoms · 5 active days.
- Recent highlights: July 15, 2026: ~41 changed, +169 atoms, -60 atoms (`DLP Organization Data Profiles Driver` (-12)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-19/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `~3` objects · 2 active days.
- Last 30 days: `+1` net · `+1` object · `~6` objects · `+1` atom · 6 active days.
- Recent highlights: July 19, 2026: ~1 changed (`Organization Copilot metrics` (+1)); July 15, 2026: ~2 changed (`Administration` (+4)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-19/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-19/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-19/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
