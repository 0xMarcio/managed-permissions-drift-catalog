# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: November 7, 2026 · [daily report](docs/daily/2026-11-07.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `-8` net · `+3` objects · `~25` objects · `+408` atoms · `-4` atoms · 4 active days | `+3,287` net · `+15` objects · `~118` objects · `+3,715` atoms · `-16` atoms · 23 active days | AWS managed policies (7d, last changed [November 7, 2026](data/diffs/2026-11-07/aws-managed-policies.json)) |
| Azure | `+8` net · `+2` objects · `~4` objects · `+8` atoms · 1 active day | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | Azure built-in roles (7d, last changed [November 4, 2026](data/diffs/2026-11-04/azure-built-in-roles.json)) |
| GCP | `+895` net · `~117` objects · `+906` atoms · `-11` atoms · 1 active day | `+4,243` net · `+23` objects · `~538` objects · `+4,299` atoms · `-56` atoms · 6 active days | GCP predefined roles (7d, last changed [November 4, 2026](data/diffs/2026-11-04/gcp-predefined-roles.json)) |
| GitHub | `~2` objects · 2 active days | `+2` net · `+1` object · `~6` objects · `+1` atom · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [November 7, 2026](data/diffs/2026-11-07/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,616` | [November 7, 2026](data/diffs/2026-11-07/aws-managed-policies.json) | `-8` net · `+3` objects · `~25` objects · `+408` atoms · `-4` atoms · 4 active days | `+3,287` net · `+15` objects · `~118` objects · `+3,715` atoms · `-16` atoms · 23 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-07/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `506` | [November 4, 2026](data/diffs/2026-11-04/azure-built-in-roles.json) | `+8` net · `+2` objects · `~4` objects · `+8` atoms · 1 active day | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-07/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,411` | [November 4, 2026](data/diffs/2026-11-04/gcp-predefined-roles.json) | `+895` net · `~117` objects · `+906` atoms · `-11` atoms · 1 active day | `+4,243` net · `+23` objects · `~538` objects · `+4,299` atoms · `-56` atoms · 6 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-07/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-07/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [November 7, 2026](data/diffs/2026-11-07/github-fgpat-permissions.json) | `~2` objects · 2 active days | `~6` objects · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-07/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | No movement | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-07/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,616` objects.
- Last 7 days: `-8` net · `+3` objects · `~25` objects · `+408` atoms · `-4` atoms · 4 active days.
- Last 30 days: `+3,287` net · `+15` objects · `~118` objects · `+3,715` atoms · `-16` atoms · 23 active days.
- Recent highlights: November 7, 2026: +1 objects, ~10 changed, +286 atoms, -1 atoms (`AWSCompromisedKeyQuarantineV4` (+205 atoms), `NetworkSecurityManagerServiceRolePolicy` (+58)); November 6, 2026: +1 objects, ~7 changed, +47 atoms, -3 atoms (`AWSPartnerCentralAccountManagementServiceRolePolicy` (+10 atoms), `AIDevOpsAgentAccessPolicy` (+23)); November 4, 2026: ~4 changed, +3 atoms (`CloudWatchAPIKeyAccess` (+1)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-07/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `506` objects.
- Last 7 days: `+8` net · `+2` objects · `~4` objects · `+8` atoms · 1 active day.
- Last 30 days: `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days.
- Recent highlights: November 4, 2026: +2 objects, ~4 changed, +8 atoms (`Foundry Project Runtime User` (+3 atoms), `Foundry Account Owner` (+1)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-07/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,411` objects.
- Last 7 days: `+895` net · `~117` objects · `+906` atoms · `-11` atoms · 1 active day.
- Last 30 days: `+4,243` net · `+23` objects · `~538` objects · `+4,299` atoms · `-56` atoms · 6 active days.
- Recent highlights: November 4, 2026: ~117 changed, +906 atoms, -11 atoms (`DLP Organization Data Profiles Driver` (+63)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-07/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `~2` objects · 2 active days.
- Last 30 days: `~6` objects · 5 active days.
- Recent highlights: November 7, 2026: ~1 changed (`Administration` (+2)); November 5, 2026: ~1 changed (`Copilot agent settings` (+3)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-07/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-07/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-07/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
