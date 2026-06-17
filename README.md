# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: June 17, 2026 · [daily report](docs/daily/2026-06-17.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+62` net · `+3` objects · `~9` objects · `+62` atoms · 3 active days | `+458` net · `+14` objects · `~57` objects · `+668` atoms · `-150` atoms · 16 active days | AWS managed policies (7d, last changed [June 14, 2026](data/diffs/2026-06-14/aws-managed-policies.json)) |
| Azure | No movement | `+4` net · `+3` objects · `~15` objects · `+44` atoms · `-4` atoms · 4 active days | Azure built-in roles (30d, last changed [June 3, 2026](data/diffs/2026-06-03/azure-built-in-roles.json)) |
| GCP | `+266` net · `+1` object · `~51` objects · `+274` atoms · `-8` atoms · 1 active day | `+840` net · `+15` objects · `~169` objects · `+848` atoms · `-8` atoms · 5 active days | GCP predefined roles (7d, last changed [June 12, 2026](data/diffs/2026-06-12/gcp-predefined-roles.json)) |
| GitHub | No movement | `~5` objects · 3 active days | GitHub fine-grained PAT permissions (30d, last changed [June 4, 2026](data/diffs/2026-06-04/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,518` | [June 14, 2026](data/diffs/2026-06-14/aws-managed-policies.json) | `+62` net · `+3` objects · `~9` objects · `+62` atoms · 3 active days | `+458` net · `+14` objects · `~57` objects · `+668` atoms · `-150` atoms · 16 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-17/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `501` | [June 3, 2026](data/diffs/2026-06-03/azure-built-in-roles.json) | No movement | `+4` net · `+3` objects · `~15` objects · `+44` atoms · `-4` atoms · 4 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-17/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,324` | [June 12, 2026](data/diffs/2026-06-12/gcp-predefined-roles.json) | `+266` net · `+1` object · `~51` objects · `+274` atoms · `-8` atoms · 1 active day | `+840` net · `+15` objects · `~169` objects · `+848` atoms · `-8` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-17/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-17/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `72` | [June 4, 2026](data/diffs/2026-06-04/github-fgpat-permissions.json) | No movement | `~5` objects · 3 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-17/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-17/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,518` objects.
- Last 7 days: `+62` net · `+3` objects · `~9` objects · `+62` atoms · 3 active days.
- Last 30 days: `+458` net · `+14` objects · `~57` objects · `+668` atoms · `-150` atoms · 16 active days.
- Recent highlights: June 14, 2026: +1 objects, ~2 changed, +16 atoms (`AnthropicSelfHostedEnvironmentAccess` (+6 atoms), `AIDevOpsAgentFullAccess` (+5)); June 13, 2026: +1 objects, ~2 changed, +28 atoms (`AWSSecurityAgentServiceRolePolicy` (+8 atoms), `AWSSecurityAgentWebAppPolicy` (+15)); June 12, 2026: +1 objects, ~5 changed, +18 atoms (`ReInventTicketApprovalAccess` (+2 atoms), `AIDevOpsAgentFullAccess` (+5)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-17/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `501` objects.
- Last 7 days: No movement.
- Last 30 days: `+4` net · `+3` objects · `~15` objects · `+44` atoms · `-4` atoms · 4 active days.
- Recent highlights: June 3, 2026: ~10 changed, +22 atoms, -4 atoms (`Cosmos DB Operator` (+16)); May 29, 2026: +1 objects, +4 atoms (`Semantic Reranker User` (+4 atoms)); May 25, 2026: ~5 changed (`Azure AI Developer` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-17/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,324` objects.
- Last 7 days: `+266` net · `+1` object · `~51` objects · `+274` atoms · `-8` atoms · 1 active day.
- Last 30 days: `+840` net · `+15` objects · `~169` objects · `+848` atoms · `-8` atoms · 5 active days.
- Recent highlights: June 12, 2026: +1 objects, ~51 changed, +274 atoms, -8 atoms (`Firebase Cloud Messaging API Viewer` (+10 atoms), `DLP Organization Data Profiles Driver` (+16)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-17/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `72` objects.
- Last 7 days: No movement.
- Last 30 days: `~5` objects · 3 active days.
- Recent highlights: June 4, 2026: ~1 changed (`Administration` (+1)); June 3, 2026: ~3 changed (`Administration` (+1)); May 21, 2026: ~1 changed (`Administration` (+2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-17/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-17/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-17/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
