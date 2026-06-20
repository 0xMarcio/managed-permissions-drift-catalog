# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: June 20, 2026 · [daily report](docs/daily/2026-06-20.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+277` net · `+2` objects · `~12` objects · `+277` atoms · 4 active days | `+755` net · `+15` objects · `~61` objects · `+888` atoms · `-77` atoms · 16 active days | AWS managed policies (7d, last changed [June 20, 2026](data/diffs/2026-06-20/aws-managed-policies.json)) |
| Azure | No movement | `-14` net · `+1` object · `~15` objects · `+26` atoms · `-4` atoms · 3 active days | Azure built-in roles (30d, last changed [June 3, 2026](data/diffs/2026-06-03/azure-built-in-roles.json)) |
| GCP | No movement | `+661` net · `+14` objects · `~118` objects · `+669` atoms · `-8` atoms · 3 active days | GCP predefined roles (30d, last changed [June 12, 2026](data/diffs/2026-06-12/gcp-predefined-roles.json)) |
| GitHub | `~5` objects · 1 active day | `~9` objects · 3 active days | GitHub fine-grained PAT permissions (7d, last changed [June 19, 2026](data/diffs/2026-06-19/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,519` | [June 20, 2026](data/diffs/2026-06-20/aws-managed-policies.json) | `+277` net · `+2` objects · `~12` objects · `+277` atoms · 4 active days | `+755` net · `+15` objects · `~61` objects · `+888` atoms · `-77` atoms · 16 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-20/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `501` | [June 3, 2026](data/diffs/2026-06-03/azure-built-in-roles.json) | No movement | `-14` net · `+1` object · `~15` objects · `+26` atoms · `-4` atoms · 3 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-20/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,324` | [June 12, 2026](data/diffs/2026-06-12/gcp-predefined-roles.json) | No movement | `+661` net · `+14` objects · `~118` objects · `+669` atoms · `-8` atoms · 3 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-20/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-20/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `72` | [June 19, 2026](data/diffs/2026-06-19/github-fgpat-permissions.json) | `~5` objects · 1 active day | `~9` objects · 3 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-20/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-20/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,519` objects.
- Last 7 days: `+277` net · `+2` objects · `~12` objects · `+277` atoms · 4 active days.
- Last 30 days: `+755` net · `+15` objects · `~61` objects · `+888` atoms · `-77` atoms · 16 active days.
- Recent highlights: June 20, 2026: ~4 changed, +7 atoms (`AmazonEMRContainersServiceRolePolicy` (+6)); June 19, 2026: +1 objects, +219 atoms (`AWSResilienceHubV2AssessmentExecutionPolicy` (+219 atoms)); June 18, 2026: ~6 changed, +35 atoms (`ReadOnlyAccess` (+15)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-20/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `501` objects.
- Last 7 days: No movement.
- Last 30 days: `-14` net · `+1` object · `~15` objects · `+26` atoms · `-4` atoms · 3 active days.
- Recent highlights: June 3, 2026: ~10 changed, +22 atoms, -4 atoms (`Cosmos DB Operator` (+16)); May 29, 2026: +1 objects, +4 atoms (`Semantic Reranker User` (+4 atoms)); May 25, 2026: ~5 changed (`Azure AI Developer` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-20/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,324` objects.
- Last 7 days: No movement.
- Last 30 days: `+661` net · `+14` objects · `~118` objects · `+669` atoms · `-8` atoms · 3 active days.
- Recent highlights: June 12, 2026: +1 objects, ~51 changed, +274 atoms, -8 atoms (`Firebase Cloud Messaging API Viewer` (+10 atoms), `DLP Organization Data Profiles Driver` (+16)); June 4, 2026: +11 objects, ~26 changed, +235 atoms (`Connectors Editor` (+73 atoms), `Vertex AI Service Agent` (+9)); May 28, 2026: +2 objects, ~41 changed, +160 atoms (`Google Tag Gateway Admin Beta` (+14 atoms), `Cloud Composer API Service Agent` (+13)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-20/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `72` objects.
- Last 7 days: `~5` objects · 1 active day.
- Last 30 days: `~9` objects · 3 active days.
- Recent highlights: June 19, 2026: ~5 changed (`Artifact metadata` (+5, -5)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-20/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-20/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-20/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
