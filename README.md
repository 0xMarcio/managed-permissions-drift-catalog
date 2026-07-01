# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: July 1, 2026 · [daily report](docs/daily/2026-07-01.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+190` net · `+4` objects · `~19` objects · `+218` atoms · `-26` atoms · 6 active days | `+1,105` net · `+20` objects · `~65` objects · `+1,176` atoms · `-33` atoms · 19 active days | AWS managed policies (7d, last changed [July 1, 2026](data/diffs/2026-07-01/aws-managed-policies.json)) |
| Azure | No movement | `-10` net · `~15` objects · `+28` atoms · `-6` atoms · 2 active days | Azure built-in roles (30d, last changed [June 21, 2026](data/diffs/2026-06-21/azure-built-in-roles.json)) |
| GCP | `+553` net · `+15` objects · `~91` objects · `+554` atoms · `-1` atom · 2 active days | `+1,180` net · `+37` objects · `~198` objects · `+1,189` atoms · `-9` atoms · 5 active days | GCP predefined roles (7d, last changed [July 1, 2026](data/diffs/2026-07-01/gcp-predefined-roles.json)) |
| GitHub | `+1` net · `+1` object · `~1` object · `+1` atom · 2 active days | `+1` net · `+1` object · `~11` objects · `+1` atom · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [June 30, 2026](data/diffs/2026-06-30/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,526` | [July 1, 2026](data/diffs/2026-07-01/aws-managed-policies.json) | `+190` net · `+4` objects · `~19` objects · `+218` atoms · `-26` atoms · 6 active days | `+1,105` net · `+20` objects · `~65` objects · `+1,176` atoms · `-33` atoms · 19 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-01/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `501` | [June 21, 2026](data/diffs/2026-06-21/azure-built-in-roles.json) | No movement | `-10` net · `~15` objects · `+28` atoms · `-6` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-01/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,349` | [July 1, 2026](data/diffs/2026-07-01/gcp-predefined-roles.json) | `+553` net · `+15` objects · `~91` objects · `+554` atoms · `-1` atom · 2 active days | `+1,180` net · `+37` objects · `~198` objects · `+1,189` atoms · `-9` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-01/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-01/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [June 30, 2026](data/diffs/2026-06-30/github-fgpat-permissions.json) | `+1` net · `+1` object · `~1` object · `+1` atom · 2 active days | `+1` net · `+1` object · `~11` objects · `+1` atom · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-01/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-01/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,526` objects.
- Last 7 days: `+190` net · `+4` objects · `~19` objects · `+218` atoms · `-26` atoms · 6 active days.
- Last 30 days: `+1,105` net · `+20` objects · `~65` objects · `+1,176` atoms · `-33` atoms · 19 active days.
- Recent highlights: July 1, 2026: +2 objects, ~4 changed, +25 atoms (`AWSRevenueAttributionManagement` (+7 atoms), `AWSCertificateManagerReadOnly` (+9)); June 30, 2026: ~6 changed, +80 atoms, -21 atoms (`SageMakerStudioProjectUserRolePolicy` (+11, -18)); June 28, 2026: ~7 changed, +51 atoms (`AIDevOpsAgentAccessPolicy` (+28)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-01/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `501` objects.
- Last 7 days: No movement.
- Last 30 days: `-10` net · `~15` objects · `+28` atoms · `-6` atoms · 2 active days.
- Recent highlights: June 21, 2026: ~5 changed, +6 atoms, -2 atoms (`Foundry Owner` (+2)); June 3, 2026: ~10 changed, +22 atoms, -4 atoms (`Cosmos DB Operator` (+16)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-01/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,349` objects.
- Last 7 days: `+553` net · `+15` objects · `~91` objects · `+554` atoms · `-1` atom · 2 active days.
- Last 30 days: `+1,180` net · `+37` objects · `~198` objects · `+1,189` atoms · `-9` atoms · 5 active days.
- Recent highlights: July 1, 2026: +6 objects, ~55 changed, +196 atoms, -1 atoms (`Dataplex Data Domain Admin Beta` (+16 atoms), `Dataplex Administrator` (+14)); June 25, 2026: +9 objects, ~36 changed, +358 atoms (`Appengine Admin` (+30 atoms), `Chronicle SOAR Threat Manager` (+13)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-01/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: `+1` net · `+1` object · `~1` object · `+1` atom · 2 active days.
- Last 30 days: `+1` net · `+1` object · `~11` objects · `+1` atom · 6 active days.
- Recent highlights: June 30, 2026: ~1 changed (`Administration` (+1, -1)); June 26, 2026: +1 objects, +1 atoms (`Code quality` (+1 atoms)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-01/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-01/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-01/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
