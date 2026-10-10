# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: October 10, 2026 · [daily report](docs/daily/2026-10-10.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+378` net · `+1` object · `~22` objects · `+387` atoms · `-1` atom · 6 active days | `+5,630` net · `+13` objects · `~79` objects · `-1` object · `+5,656` atoms · `-12` atoms · 22 active days | AWS managed policies (7d, last changed [October 10, 2026](data/diffs/2026-10-10/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | `+762` net · `+3` objects · `~190` objects · `-1` object · `+790` atoms · `-28` atoms · 1 active day | `+2,111` net · `+21` objects · `~428` objects · `-7` objects · `+2,198` atoms · `-87` atoms · 4 active days | GCP predefined roles (7d, last changed [October 8, 2026](data/diffs/2026-10-08/gcp-predefined-roles.json)) |
| GitHub | `~2` objects · 2 active days | `+7` net · `+3` objects · `~12` objects · `+3` atoms · 8 active days | GitHub fine-grained PAT permissions (7d, last changed [October 9, 2026](data/diffs/2026-10-09/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,601` | [October 10, 2026](data/diffs/2026-10-10/aws-managed-policies.json) | `+378` net · `+1` object · `~22` objects · `+387` atoms · `-1` atom · 6 active days | `+5,630` net · `+13` objects · `~79` objects · `-1` object · `+5,656` atoms · `-12` atoms · 22 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-10/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-10/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,388` | [October 8, 2026](data/diffs/2026-10-08/gcp-predefined-roles.json) | `+762` net · `+3` objects · `~190` objects · `-1` object · `+790` atoms · `-28` atoms · 1 active day | `+2,111` net · `+21` objects · `~428` objects · `-7` objects · `+2,198` atoms · `-87` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-10/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-10/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 9, 2026](data/diffs/2026-10-09/github-fgpat-permissions.json) | `~2` objects · 2 active days | `+7` net · `+3` objects · `~12` objects · `+3` atoms · 8 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-10/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-10/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,601` objects.
- Last 7 days: `+378` net · `+1` object · `~22` objects · `+387` atoms · `-1` atom · 6 active days.
- Last 30 days: `+5,630` net · `+13` objects · `~79` objects · `-1` object · `+5,656` atoms · `-12` atoms · 22 active days.
- Recent highlights: October 10, 2026: ~9 changed, +36 atoms (`SageMakerStudioAdminIAMDefaultExecutionPolicy` (+21)); October 9, 2026: ~5 changed, +322 atoms (`ConsoleFullAccessFromVercel` (+132)); October 8, 2026: ~3 changed, +12 atoms, -1 atoms (`AWSSecurityAgentWebAppPolicy` (+7)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-10/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-10/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,388` objects.
- Last 7 days: `+762` net · `+3` objects · `~190` objects · `-1` object · `+790` atoms · `-28` atoms · 1 active day.
- Last 30 days: `+2,111` net · `+21` objects · `~428` objects · `-7` objects · `+2,198` atoms · `-87` atoms · 4 active days.
- Recent highlights: October 8, 2026: +3 objects, ~190 changed, -1 removed, +790 atoms, -28 atoms (`DLP Content Policies Editor` (+6 atoms), `Discovery Engine Editor` (+64)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-10/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `~2` objects · 2 active days.
- Last 30 days: `+7` net · `+3` objects · `~12` objects · `+3` atoms · 8 active days.
- Recent highlights: October 9, 2026: ~1 changed (`Repository creation` (+1)); October 6, 2026: ~1 changed (`Pull requests` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-10/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-10/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-10/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
