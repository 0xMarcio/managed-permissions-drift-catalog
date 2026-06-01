# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: June 1, 2026 · [daily report](docs/daily/2026-06-01.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+76` net · `+2` objects · `~10` objects · `+166` atoms · `-70` atoms · 4 active days | `+376` net · `+7` objects · `~59` objects · `+605` atoms · `-181` atoms · 21 active days | AWS managed policies (7d, last changed [May 31, 2026](data/diffs/2026-05-31/aws-managed-policies.json)) |
| Azure | `+1` object · `+4` atoms · 1 active day | `+18` net · `+3` objects · `~9` objects · `+22` atoms · 4 active days | Azure built-in roles (7d, last changed [May 29, 2026](data/diffs/2026-05-29/azure-built-in-roles.json)) |
| GCP | `+160` net · `+2` objects · `~41` objects · `+160` atoms · 1 active day | `-18,261` net · `+29` objects · `~294` objects · `-10` objects · `+1,694` atoms · `-19,955` atoms · 5 active days | GCP predefined roles (7d, last changed [May 28, 2026](data/diffs/2026-05-28/gcp-predefined-roles.json)) |
| GitHub | No movement | `+16` net · `+6` objects · `~6` objects · `+11` atoms · 4 active days | GitHub fine-grained PAT permissions (30d, last changed [May 21, 2026](data/diffs/2026-05-21/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,506` | [May 31, 2026](data/diffs/2026-05-31/aws-managed-policies.json) | `+76` net · `+2` objects · `~10` objects · `+166` atoms · `-70` atoms · 4 active days | `+376` net · `+7` objects · `~59` objects · `+605` atoms · `-181` atoms · 21 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-01/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `501` | [May 29, 2026](data/diffs/2026-05-29/azure-built-in-roles.json) | `+1` object · `+4` atoms · 1 active day | `+18` net · `+3` objects · `~9` objects · `+22` atoms · 4 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-01/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,312` | [May 28, 2026](data/diffs/2026-05-28/gcp-predefined-roles.json) | `+160` net · `+2` objects · `~41` objects · `+160` atoms · 1 active day | `-18,261` net · `+29` objects · `~294` objects · `-10` objects · `+1,694` atoms · `-19,955` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-01/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-01/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `72` | [May 21, 2026](data/diffs/2026-05-21/github-fgpat-permissions.json) | No movement | `+13` net · `+5` objects · `~6` objects · `+9` atoms · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-01/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [May 12, 2026](data/diffs/2026-05-12/github-token-permissions.json) | No movement | `+3` net · `+1` object · `+2` atoms · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-01/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,506` objects.
- Last 7 days: `+76` net · `+2` objects · `~10` objects · `+166` atoms · `-70` atoms · 4 active days.
- Last 30 days: `+376` net · `+7` objects · `~59` objects · `+605` atoms · `-181` atoms · 21 active days.
- Recent highlights: May 31, 2026: ~3 changed, +5 atoms (`AWSDeadlineCloud-UserAccessFarms` (+2)); May 30, 2026: +1 objects, ~1 changed, +7 atoms (`AWSResilienceHubServiceRolePolicy` (+7 atoms), `AmazonEBSCSIDriverEKSClusterScopedPolicy` (metadata only)); May 29, 2026: ~3 changed, +24 atoms, -63 atoms (`AmazonConnectServiceLinkedRolePolicy` (+13, -63)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-01/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `501` objects.
- Last 7 days: `+1` object · `+4` atoms · 1 active day.
- Last 30 days: `+18` net · `+3` objects · `~9` objects · `+22` atoms · 4 active days.
- Recent highlights: May 29, 2026: +1 objects, +4 atoms (`Semantic Reranker User` (+4 atoms)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-01/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,312` objects.
- Last 7 days: `+160` net · `+2` objects · `~41` objects · `+160` atoms · 1 active day.
- Last 30 days: `-18,261` net · `+29` objects · `~294` objects · `-10` objects · `+1,694` atoms · `-19,955` atoms · 5 active days.
- Recent highlights: May 28, 2026: +2 objects, ~41 changed, +160 atoms (`Google Tag Gateway Admin Beta` (+14 atoms), `Cloud Composer API Service Agent` (+13)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-01/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `72` objects.
- Last 7 days: No movement.
- Last 30 days: `+13` net · `+5` objects · `~6` objects · `+9` atoms · 4 active days.
- Recent highlights: May 21, 2026: ~1 changed (`Administration` (+2)); May 16, 2026: +1 objects, ~4 changed, +1 atoms (`Copilot agent settings` (+1 atoms), `Contents` (+1, -1)); May 12, 2026: +4 objects, +8 atoms (`Agent secrets` (+2 atoms)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-01/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+3` net · `+1` object · `+2` atoms · 1 active day.
- Recent highlights: May 12, 2026: +1 objects, +2 atoms (`code-quality` (+2 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-01/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-01/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
