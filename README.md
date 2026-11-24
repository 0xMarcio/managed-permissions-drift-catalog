# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: November 24, 2026 · [daily report](docs/daily/2026-11-24.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+4,264` net · `+17` objects · `~66` objects · `+4,330` atoms · `-46` atoms · 6 active days | `+6,585` net · `+34` objects · `~200` objects · `+7,181` atoms · `-102` atoms · 22 active days | AWS managed policies (7d, last changed [November 24, 2026](data/diffs/2026-11-24/aws-managed-policies.json)) |
| Azure | `+34` net · `+1` object · `+34` atoms · 1 active day | `+44` net · `+3` objects · `~5` objects · `+44` atoms · 3 active days | Azure built-in roles (7d, last changed [November 19, 2026](data/diffs/2026-11-19/azure-built-in-roles.json)) |
| GCP | `+687` net · `+11` objects · `~81` objects · `+737` atoms · `-50` atoms · 2 active days | `+2,474` net · `+18` objects · `~269` objects · `+2,549` atoms · `-75` atoms · 4 active days | GCP predefined roles (7d, last changed [November 24, 2026](data/diffs/2026-11-24/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `+6` net · `+2` objects · `~8` objects · `+4` atoms · 7 active days | GitHub fine-grained PAT permissions (7d, last changed [November 18, 2026](data/diffs/2026-11-18/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,642` | [November 24, 2026](data/diffs/2026-11-24/aws-managed-policies.json) | `+4,264` net · `+17` objects · `~66` objects · `+4,330` atoms · `-46` atoms · 6 active days | `+6,585` net · `+34` objects · `~200` objects · `+7,181` atoms · `-102` atoms · 22 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-24/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `507` | [November 19, 2026](data/diffs/2026-11-19/azure-built-in-roles.json) | `+34` net · `+1` object · `+34` atoms · 1 active day | `+44` net · `+3` objects · `~5` objects · `+44` atoms · 3 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-24/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,422` | [November 24, 2026](data/diffs/2026-11-24/gcp-predefined-roles.json) | `+687` net · `+11` objects · `~81` objects · `+737` atoms · `-50` atoms · 2 active days | `+2,474` net · `+18` objects · `~269` objects · `+2,549` atoms · `-75` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-24/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-24/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `78` | [November 18, 2026](data/diffs/2026-11-18/github-fgpat-permissions.json) | `~1` object · 1 active day | `+6` net · `+2` objects · `~8` objects · `+4` atoms · 7 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-24/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-24/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,642` objects.
- Last 7 days: `+4,264` net · `+17` objects · `~66` objects · `+4,330` atoms · `-46` atoms · 6 active days.
- Last 30 days: `+6,585` net · `+34` objects · `~200` objects · `+7,181` atoms · `-102` atoms · 22 active days.
- Recent highlights: November 24, 2026: ~1 changed, +1 atoms (`CloudWatchReadOnlyAccess` (+1)); November 23, 2026: ~2 changed, +40 atoms (`AmazonFSxConsoleFullAccess` (+20)); November 22, 2026: +1 objects, ~13 changed, +2,385 atoms (`AWSBudgetsActionExecutionPolicy` (+12 atoms), `AWS_ConfigRole` (+1,167)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-24/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `507` objects.
- Last 7 days: `+34` net · `+1` object · `+34` atoms · 1 active day.
- Last 30 days: `+44` net · `+3` objects · `~5` objects · `+44` atoms · 3 active days.
- Recent highlights: November 19, 2026: +1 objects, +34 atoms (`Azure Arc Kubernetes Reader` (+34 atoms)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-24/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,422` objects.
- Last 7 days: `+687` net · `+11` objects · `~81` objects · `+737` atoms · `-50` atoms · 2 active days.
- Last 30 days: `+2,474` net · `+18` objects · `~269` objects · `+2,549` atoms · `-75` atoms · 4 active days.
- Recent highlights: November 24, 2026: ~1 changed (`Data pipelines Invoker` (metadata only)); November 19, 2026: +11 objects, ~80 changed, +737 atoms, -50 atoms (`Firebase Telemetry Admin Admin Beta` (+18 atoms), `Assured Workloads Monitoring Service Agent` (+112)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-24/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `78` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `+6` net · `+2` objects · `~8` objects · `+4` atoms · 7 active days.
- Recent highlights: November 18, 2026: ~1 changed (`Issues` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-24/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-24/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-24/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
