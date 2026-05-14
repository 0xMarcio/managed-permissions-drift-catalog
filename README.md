# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: May 14, 2026 · [daily report](docs/daily/2026-05-14.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+123` net · `+5` objects · `~19` objects · `+184` atoms · `-37` atoms · 6 active days | `+445` net · `+6` objects · `~53` objects · `+564` atoms · `-95` atoms · 19 active days | AWS managed policies (7d, last changed [May 14, 2026](data/diffs/2026-05-14/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | `-18,600` net · `+26` objects · `~202` objects · `-10` objects · `+1,355` atoms · `-19,955` atoms · 2 active days | `-15,951` net · `+77` objects · `~373` objects · `-12` objects · `+4,052` atoms · `-20,003` atoms · 3 active days | GCP predefined roles (7d, last changed [May 13, 2026](data/diffs/2026-05-13/gcp-predefined-roles.json)) |
| GitHub | `+15` net · `+5` objects · `+10` atoms · 1 active day | `+19` net · `+7` objects · `~5` objects · `+13` atoms · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [May 12, 2026](data/diffs/2026-05-12/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,504` | [May 14, 2026](data/diffs/2026-05-14/aws-managed-policies.json) | `+123` net · `+5` objects · `~19` objects · `+184` atoms · `-37` atoms · 6 active days | `+445` net · `+6` objects · `~53` objects · `+564` atoms · `-95` atoms · 19 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-14/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `498` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-14/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,309` | [May 13, 2026](data/diffs/2026-05-13/gcp-predefined-roles.json) | `-18,600` net · `+26` objects · `~202` objects · `-10` objects · `+1,355` atoms · `-19,955` atoms · 2 active days | `-15,951` net · `+77` objects · `~373` objects · `-12` objects · `+4,052` atoms · `-20,003` atoms · 3 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-14/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-14/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `71` | [May 12, 2026](data/diffs/2026-05-12/github-fgpat-permissions.json) | `+12` net · `+4` objects · `+8` atoms · 1 active day | `+15` net · `+5` objects · `~4` objects · `+10` atoms · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-14/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [May 12, 2026](data/diffs/2026-05-12/github-token-permissions.json) | `+3` net · `+1` object · `+2` atoms · 1 active day | `+4` net · `+2` objects · `~1` object · `+3` atoms · 2 active days | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-14/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,504` objects.
- Last 7 days: `+123` net · `+5` objects · `~19` objects · `+184` atoms · `-37` atoms · 6 active days.
- Last 30 days: `+445` net · `+6` objects · `~53` objects · `+564` atoms · `-95` atoms · 19 active days.
- Recent highlights: May 14, 2026: ~1 changed (`AWSECRPullThroughCache_ServiceRolePolicy` (metadata only)); May 13, 2026: ~7 changed, +59 atoms, -37 atoms (`SageMakerStudioUserIAMDefaultExecutionPolicy` (+17, -19)); May 12, 2026: +2 objects, +14 atoms (`AWSVPCFlowLogsServiceRolePolicy` (+7 atoms)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-14/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `498` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-14/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,309` objects.
- Last 7 days: `-18,600` net · `+26` objects · `~202` objects · `-10` objects · `+1,355` atoms · `-19,955` atoms · 2 active days.
- Last 30 days: `-15,951` net · `+77` objects · `~373` objects · `-12` objects · `+4,052` atoms · `-20,003` atoms · 3 active days.
- Recent highlights: May 13, 2026: +26 objects, ~201 changed, -1 removed, +1,355 atoms, -62 atoms (`Gemini for Google Cloud Admin` (+100 atoms), `Security Admin` (+44)); May 8, 2026: ~1 changed, -9 removed, -19,893 atoms (`IAM Workforce Pool Editor` (metadata only), `Support User` (-6,286 atoms)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-14/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `71` objects.
- Last 7 days: `+12` net · `+4` objects · `+8` atoms · 1 active day.
- Last 30 days: `+15` net · `+5` objects · `~4` objects · `+10` atoms · 5 active days.
- Recent highlights: May 12, 2026: +4 objects, +8 atoms (`Agent secrets` (+2 atoms)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-14/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: `+3` net · `+1` object · `+2` atoms · 1 active day.
- Last 30 days: `+4` net · `+2` objects · `~1` object · `+3` atoms · 2 active days.
- Recent highlights: May 12, 2026: +1 objects, +2 atoms (`code-quality` (+2 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-14/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-14/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
