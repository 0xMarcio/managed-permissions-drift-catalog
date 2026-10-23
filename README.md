# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: October 23, 2026 · [daily report](docs/daily/2026-10-23.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+1,697` net · `+4` objects · `~11` objects · `+1,697` atoms · 5 active days | `+6,031` net · `+12` objects · `~82` objects · `-1` object · `+6,051` atoms · `-12` atoms · 25 active days | AWS managed policies (7d, last changed [October 23, 2026](data/diffs/2026-10-23/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | `+1,143` net · `+4` objects · `~257` objects · `+1,151` atoms · `-8` atoms · 2 active days | `+3,532` net · `+24` objects · `~607` objects · `-7` objects · `+3,644` atoms · `-112` atoms · 6 active days | GCP predefined roles (7d, last changed [October 21, 2026](data/diffs/2026-10-21/gcp-predefined-roles.json)) |
| GitHub | No movement | `+9` net · `+4` objects · `~5` objects · `+4` atoms · 6 active days | GitHub fine-grained PAT permissions (30d, last changed [October 9, 2026](data/diffs/2026-10-09/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,608` | [October 23, 2026](data/diffs/2026-10-23/aws-managed-policies.json) | `+1,697` net · `+4` objects · `~11` objects · `+1,697` atoms · 5 active days | `+6,031` net · `+12` objects · `~82` objects · `-1` object · `+6,051` atoms · `-12` atoms · 25 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-23/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-23/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,404` | [October 21, 2026](data/diffs/2026-10-21/gcp-predefined-roles.json) | `+1,143` net · `+4` objects · `~257` objects · `+1,151` atoms · `-8` atoms · 2 active days | `+3,532` net · `+24` objects · `~607` objects · `-7` objects · `+3,644` atoms · `-112` atoms · 6 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-23/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-23/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 9, 2026](data/diffs/2026-10-09/github-fgpat-permissions.json) | No movement | `+7` net · `+3` objects · `~5` objects · `+3` atoms · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-23/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | No movement | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-23/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,608` objects.
- Last 7 days: `+1,697` net · `+4` objects · `~11` objects · `+1,697` atoms · 5 active days.
- Last 30 days: `+6,031` net · `+12` objects · `~82` objects · `-1` object · `+6,051` atoms · `-12` atoms · 25 active days.
- Recent highlights: October 23, 2026: ~1 changed, +1 atoms (`AmazonEKSServiceRolePolicy` (+1)); October 22, 2026: +1 objects, ~1 changed, +69 atoms (`AssuranceOperatorPolicy` (+68 atoms), `CloudWatchFullAccessV2` (+1)); October 21, 2026: +2 objects, ~2 changed, +1,568 atoms (`AWSFinOpsAgentServiceRolePolicy` (+231 atoms), `AssuranceServiceRolePolicy` (+1,283)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-23/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-23/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,404` objects.
- Last 7 days: `+1,143` net · `+4` objects · `~257` objects · `+1,151` atoms · `-8` atoms · 2 active days.
- Last 30 days: `+3,532` net · `+24` objects · `~607` objects · `-7` objects · `+3,644` atoms · `-112` atoms · 6 active days.
- Recent highlights: October 21, 2026: +4 objects, ~252 changed, +1,151 atoms, -8 atoms (`Folder level Compute VM extension policies admin Beta` (+31 atoms), `Cloud Dataplex Service Agent` (+44, -8)); October 17, 2026: ~5 changed (`Advisory Support Editor` (metadata only)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-23/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: No movement.
- Last 30 days: `+7` net · `+3` objects · `~5` objects · `+3` atoms · 5 active days.
- Recent highlights: October 9, 2026: ~1 changed (`Repository creation` (+1)); October 6, 2026: ~1 changed (`Pull requests` (+1)); September 30, 2026: +2 objects, ~1 changed, +2 atoms (`External custom properties for repositories` (+1 atoms), `Actions` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-23/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-23/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-23/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
