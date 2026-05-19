# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: May 19, 2026 · [daily report](docs/daily/2026-05-19.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+57` net · `~17` objects · `+119` atoms · `-38` atoms · 6 active days | `+504` net · `+6` objects · `~61` objects · `+624` atoms · `-96` atoms · 22 active days | AWS managed policies (7d, last changed [May 19, 2026](data/diffs/2026-05-19/aws-managed-policies.json)) |
| Azure | `+18` net · `+2` objects · `~4` objects · `+18` atoms · 2 active days | `+18` net · `+2` objects · `~4` objects · `+18` atoms · 2 active days | Azure built-in roles (7d, last changed [May 19, 2026](data/diffs/2026-05-19/azure-built-in-roles.json)) |
| GCP | `+1,293` net · `+26` objects · `~201` objects · `-1` object · `+1,355` atoms · `-62` atoms · 1 active day | `-15,951` net · `+77` objects · `~373` objects · `-12` objects · `+4,052` atoms · `-20,003` atoms · 3 active days | GCP predefined roles (7d, last changed [May 13, 2026](data/diffs/2026-05-13/gcp-predefined-roles.json)) |
| GitHub | `+1` net · `+1` object · `~4` objects · `+1` atom · 1 active day | `+20` net · `+8` objects · `~9` objects · `+14` atoms · 7 active days | GitHub fine-grained PAT permissions (7d, last changed [May 16, 2026](data/diffs/2026-05-16/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,504` | [May 19, 2026](data/diffs/2026-05-19/aws-managed-policies.json) | `+57` net · `~17` objects · `+119` atoms · `-38` atoms · 6 active days | `+504` net · `+6` objects · `~61` objects · `+624` atoms · `-96` atoms · 22 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-19/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `500` | [May 19, 2026](data/diffs/2026-05-19/azure-built-in-roles.json) | `+18` net · `+2` objects · `~4` objects · `+18` atoms · 2 active days | `+18` net · `+2` objects · `~4` objects · `+18` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-19/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,309` | [May 13, 2026](data/diffs/2026-05-13/gcp-predefined-roles.json) | `+1,293` net · `+26` objects · `~201` objects · `-1` object · `+1,355` atoms · `-62` atoms · 1 active day | `-15,951` net · `+77` objects · `~373` objects · `-12` objects · `+4,052` atoms · `-20,003` atoms · 3 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-19/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-19/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `72` | [May 16, 2026](data/diffs/2026-05-16/github-fgpat-permissions.json) | `+1` net · `+1` object · `~4` objects · `+1` atom · 1 active day | `+16` net · `+6` objects · `~8` objects · `+11` atoms · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-19/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [May 12, 2026](data/diffs/2026-05-12/github-token-permissions.json) | No movement | `+4` net · `+2` objects · `~1` object · `+3` atoms · 2 active days | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-19/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,504` objects.
- Last 7 days: `+57` net · `~17` objects · `+119` atoms · `-38` atoms · 6 active days.
- Last 30 days: `+504` net · `+6` objects · `~61` objects · `+624` atoms · `-96` atoms · 22 active days.
- Recent highlights: May 19, 2026: ~2 changed, +33 atoms (`ReadOnlyAccess` (+26)); May 17, 2026: ~1 changed, +2 atoms (`AWSServiceRoleForLogDeliveryPolicy` (+2)); May 16, 2026: ~1 changed, +4 atoms (`AWSTrustedAdvisorServiceRolePolicy` (+4)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-19/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `500` objects.
- Last 7 days: `+18` net · `+2` objects · `~4` objects · `+18` atoms · 2 active days.
- Last 30 days: `+18` net · `+2` objects · `~4` objects · `+18` atoms · 2 active days.
- Recent highlights: May 19, 2026: +2 objects, +18 atoms (`Azure Managed Redis Contributor` (+9 atoms)); May 16, 2026: ~4 changed (`Foundry Account Owner` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-19/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,309` objects.
- Last 7 days: `+1,293` net · `+26` objects · `~201` objects · `-1` object · `+1,355` atoms · `-62` atoms · 1 active day.
- Last 30 days: `-15,951` net · `+77` objects · `~373` objects · `-12` objects · `+4,052` atoms · `-20,003` atoms · 3 active days.
- Recent highlights: May 13, 2026: +26 objects, ~201 changed, -1 removed, +1,355 atoms, -62 atoms (`Gemini for Google Cloud Admin` (+100 atoms), `Security Admin` (+44)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-19/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `72` objects.
- Last 7 days: `+1` net · `+1` object · `~4` objects · `+1` atom · 1 active day.
- Last 30 days: `+16` net · `+6` objects · `~8` objects · `+11` atoms · 6 active days.
- Recent highlights: May 16, 2026: +1 objects, ~4 changed, +1 atoms (`Copilot agent settings` (+1 atoms), `Contents` (+1, -1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-19/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+4` net · `+2` objects · `~1` object · `+3` atoms · 2 active days.
- Recent highlights: May 12, 2026: +1 objects, +2 atoms (`code-quality` (+2 atoms)); April 24, 2026: +1 objects, ~1 changed, +1 atoms (`vulnerability-alerts` (+1 atoms), `security-events` (metadata only)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-19/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-19/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
