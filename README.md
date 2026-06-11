# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: June 11, 2026 · [daily report](docs/daily/2026-06-11.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+227` net · `+3` objects · `~13` objects · `+266` atoms · `-7` atoms · 3 active days | `+420` net · `+11` objects · `~63` objects · `+692` atoms · `-188` atoms · 18 active days | AWS managed policies (7d, last changed [June 9, 2026](data/diffs/2026-06-09/aws-managed-policies.json)) |
| Azure | No movement | `+4` net · `+3` objects · `~19` objects · `+44` atoms · `-4` atoms · 5 active days | Azure built-in roles (30d, last changed [June 3, 2026](data/diffs/2026-06-03/azure-built-in-roles.json)) |
| GCP | No movement | `+1,867` net · `+40` objects · `~319` objects · `-1` object · `+1,929` atoms · `-62` atoms · 5 active days | GCP predefined roles (30d, last changed [June 4, 2026](data/diffs/2026-06-04/gcp-predefined-roles.json)) |
| GitHub | No movement | `+1` net · `+1` object · `~9` objects · `+1` atom · 4 active days | GitHub fine-grained PAT permissions (30d, last changed [June 4, 2026](data/diffs/2026-06-04/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,515` | [June 9, 2026](data/diffs/2026-06-09/aws-managed-policies.json) | `+227` net · `+3` objects · `~13` objects · `+266` atoms · `-7` atoms · 3 active days | `+420` net · `+11` objects · `~63` objects · `+692` atoms · `-188` atoms · 18 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-11/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `501` | [June 3, 2026](data/diffs/2026-06-03/azure-built-in-roles.json) | No movement | `+4` net · `+3` objects · `~19` objects · `+44` atoms · `-4` atoms · 5 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-11/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,323` | [June 4, 2026](data/diffs/2026-06-04/gcp-predefined-roles.json) | No movement | `+1,867` net · `+40` objects · `~319` objects · `-1` object · `+1,929` atoms · `-62` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-11/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-11/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `72` | [June 4, 2026](data/diffs/2026-06-04/github-fgpat-permissions.json) | No movement | `+1` net · `+1` object · `~9` objects · `+1` atom · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-11/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-11/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,515` objects.
- Last 7 days: `+227` net · `+3` objects · `~13` objects · `+266` atoms · `-7` atoms · 3 active days.
- Last 30 days: `+420` net · `+11` objects · `~63` objects · `+692` atoms · `-188` atoms · 18 active days.
- Recent highlights: June 9, 2026: ~1 changed (`CloudWatchFullAccessV2` (metadata only)); June 7, 2026: ~4 changed, +47 atoms (`AIDevOpsAgentFullAccess` (+19)); June 6, 2026: +3 objects, ~8 changed, +219 atoms, -7 atoms (`FinOpsAgentAgentPolicy` (+81 atoms), `SageMakerStudioAdminIAMDefaultExecutionPolicy` (+11)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-11/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `501` objects.
- Last 7 days: No movement.
- Last 30 days: `+4` net · `+3` objects · `~19` objects · `+44` atoms · `-4` atoms · 5 active days.
- Recent highlights: June 3, 2026: ~10 changed, +22 atoms, -4 atoms (`Cosmos DB Operator` (+16)); May 29, 2026: +1 objects, +4 atoms (`Semantic Reranker User` (+4 atoms)); May 25, 2026: ~5 changed (`Azure AI Developer` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-11/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,323` objects.
- Last 7 days: No movement.
- Last 30 days: `+1,867` net · `+40` objects · `~319` objects · `-1` object · `+1,929` atoms · `-62` atoms · 5 active days.
- Recent highlights: June 4, 2026: +11 objects, ~26 changed, +235 atoms (`Connectors Editor` (+73 atoms), `Vertex AI Service Agent` (+9)); May 28, 2026: +2 objects, ~41 changed, +160 atoms (`Google Tag Gateway Admin Beta` (+14 atoms), `Cloud Composer API Service Agent` (+13)); May 21, 2026: ~6 changed (`Cloud Functions Admin` (metadata only)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-11/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `72` objects.
- Last 7 days: No movement.
- Last 30 days: `+1` net · `+1` object · `~9` objects · `+1` atom · 4 active days.
- Recent highlights: June 4, 2026: ~1 changed (`Administration` (+1)); June 3, 2026: ~3 changed (`Administration` (+1)); May 21, 2026: ~1 changed (`Administration` (+2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-11/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-11/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-11/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
