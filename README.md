# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: May 26, 2026 · [daily report](docs/daily/2026-05-26.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `-50` net · `~14` objects · `+27` atoms · `-73` atoms · 4 active days | `+334` net · `+6` objects · `~59` objects · `+473` atoms · `-111` atoms · 21 active days | AWS managed policies (7d, last changed [May 23, 2026](data/diffs/2026-05-23/aws-managed-policies.json)) |
| Azure | `~5` objects · 1 active day | `+18` net · `+2` objects · `~9` objects · `+18` atoms · 3 active days | Azure built-in roles (7d, last changed [May 25, 2026](data/diffs/2026-05-25/azure-built-in-roles.json)) |
| GCP | `+179` net · `+1` object · `~51` objects · `+179` atoms · 2 active days | `-18,421` net · `+27` objects · `~253` objects · `-10` objects · `+1,534` atoms · `-19,955` atoms · 4 active days | GCP predefined roles (7d, last changed [May 21, 2026](data/diffs/2026-05-21/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `+19` net · `+7` objects · `~7` objects · `+13` atoms · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [May 21, 2026](data/diffs/2026-05-21/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,504` | [May 23, 2026](data/diffs/2026-05-23/aws-managed-policies.json) | `-50` net · `~14` objects · `+27` atoms · `-73` atoms · 4 active days | `+334` net · `+6` objects · `~59` objects · `+473` atoms · `-111` atoms · 21 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-26/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `500` | [May 25, 2026](data/diffs/2026-05-25/azure-built-in-roles.json) | `~5` objects · 1 active day | `+18` net · `+2` objects · `~9` objects · `+18` atoms · 3 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-26/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,310` | [May 21, 2026](data/diffs/2026-05-21/gcp-predefined-roles.json) | `+179` net · `+1` object · `~51` objects · `+179` atoms · 2 active days | `-18,421` net · `+27` objects · `~253` objects · `-10` objects · `+1,534` atoms · `-19,955` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-26/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-26/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `72` | [May 21, 2026](data/diffs/2026-05-21/github-fgpat-permissions.json) | `~1` object · 1 active day | `+16` net · `+6` objects · `~7` objects · `+11` atoms · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-26/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [May 12, 2026](data/diffs/2026-05-12/github-token-permissions.json) | No movement | `+3` net · `+1` object · `+2` atoms · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-26/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,504` objects.
- Last 7 days: `-50` net · `~14` objects · `+27` atoms · `-73` atoms · 4 active days.
- Last 30 days: `+334` net · `+6` objects · `~59` objects · `+473` atoms · `-111` atoms · 21 active days.
- Recent highlights: May 23, 2026: ~1 changed, +2 atoms (`AIDevOpsOperatorAppAccessPolicy` (+2)); May 22, 2026: ~9 changed, +17 atoms (`AmazonQDeveloperAccess` (+4)); May 21, 2026: ~1 changed, +1 atoms (`AdministratorAccess-AWSElasticBeanstalk` (+1)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-26/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `500` objects.
- Last 7 days: `~5` objects · 1 active day.
- Last 30 days: `+18` net · `+2` objects · `~9` objects · `+18` atoms · 3 active days.
- Recent highlights: May 25, 2026: ~5 changed (`Azure AI Developer` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-26/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,310` objects.
- Last 7 days: `+179` net · `+1` object · `~51` objects · `+179` atoms · 2 active days.
- Last 30 days: `-18,421` net · `+27` objects · `~253` objects · `-10` objects · `+1,534` atoms · `-19,955` atoms · 4 active days.
- Recent highlights: May 21, 2026: ~6 changed (`Cloud Functions Admin` (metadata only)); May 20, 2026: +1 objects, ~45 changed, +179 atoms (`AlloyDB Admin for BackupDR` (+25 atoms), `Compute Admin` (+10)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-26/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `72` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `+16` net · `+6` objects · `~7` objects · `+11` atoms · 6 active days.
- Recent highlights: May 21, 2026: ~1 changed (`Administration` (+2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-26/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+3` net · `+1` object · `+2` atoms · 1 active day.
- Recent highlights: May 12, 2026: +1 objects, +2 atoms (`code-quality` (+2 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-26/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-26/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
