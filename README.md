# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: May 8, 2026 · [daily report](docs/daily/2026-05-08.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+216` net · `~14` objects · `+216` atoms · 5 active days | `+369` net · `+1` object · `~40` objects · `+427` atoms · `-58` atoms · 14 active days | AWS managed policies (7d, last changed [May 8, 2026](data/diffs/2026-05-08/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | `-19,893` net · `~1` object · `-9` objects · `-19,893` atoms · 1 active day | `-17,244` net · `+51` objects · `~172` objects · `-11` objects · `+2,697` atoms · `-19,941` atoms · 2 active days | GCP predefined roles (7d, last changed [May 8, 2026](data/diffs/2026-05-08/gcp-predefined-roles.json)) |
| GitHub | `+3` net · `+1` object · `~1` object · `+2` atoms · 2 active days | `+4` net · `+2` objects · `~5` objects · `+3` atoms · 5 active days | GitHub fine-grained PAT permissions (7d, last changed [May 7, 2026](data/diffs/2026-05-07/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,499` | [May 8, 2026](data/diffs/2026-05-08/aws-managed-policies.json) | `+216` net · `~14` objects · `+216` atoms · 5 active days | `+369` net · `+1` object · `~40` objects · `+427` atoms · `-58` atoms · 14 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-08/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `498` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-08/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,284` | [May 8, 2026](data/diffs/2026-05-08/gcp-predefined-roles.json) | `-19,893` net · `~1` object · `-9` objects · `-19,893` atoms · 1 active day | `-17,244` net · `+51` objects · `~172` objects · `-11` objects · `+2,697` atoms · `-19,941` atoms · 2 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-08/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-08/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `67` | [May 7, 2026](data/diffs/2026-05-07/github-fgpat-permissions.json) | `+3` net · `+1` object · `~1` object · `+2` atoms · 2 active days | `+3` net · `+1` object · `~4` objects · `+2` atoms · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-08/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [April 24, 2026](data/diffs/2026-04-24/github-token-permissions.json) | No movement | `+1` net · `+1` object · `~1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-08/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,499` objects.
- Last 7 days: `+216` net · `~14` objects · `+216` atoms · 5 active days.
- Last 30 days: `+369` net · `+1` object · `~40` objects · `+427` atoms · `-58` atoms · 14 active days.
- Recent highlights: May 8, 2026: ~6 changed, +47 atoms (`SecurityAudit` (+26)); May 7, 2026: ~5 changed, +167 atoms (`ReadOnlyAccess` (+56)); May 5, 2026: ~1 changed (`SageMakerStudioProjectProvisioningRolePolicy` (metadata only)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-08/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `498` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-08/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,284` objects.
- Last 7 days: `-19,893` net · `~1` object · `-9` objects · `-19,893` atoms · 1 active day.
- Last 30 days: `-17,244` net · `+51` objects · `~172` objects · `-11` objects · `+2,697` atoms · `-19,941` atoms · 2 active days.
- Recent highlights: May 8, 2026: ~1 changed, -9 removed, -19,893 atoms (`IAM Workforce Pool Editor` (metadata only), `Support User` (-6,286 atoms)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-08/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `67` objects.
- Last 7 days: `+3` net · `+1` object · `~1` object · `+2` atoms · 2 active days.
- Last 30 days: `+3` net · `+1` object · `~4` objects · `+2` atoms · 4 active days.
- Recent highlights: May 7, 2026: ~1 changed (`Actions` (+3)); May 2, 2026: +1 objects, +2 atoms (`Copilot Spaces` (+2 atoms)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-08/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `+1` net · `+1` object · `~1` object · `+1` atom · 1 active day.
- Recent highlights: April 24, 2026: +1 objects, ~1 changed, +1 atoms (`vulnerability-alerts` (+1 atoms), `security-events` (metadata only)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-08/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-08/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
