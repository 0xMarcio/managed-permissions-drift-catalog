# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: October 21, 2026 · [daily report](docs/daily/2026-10-21.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+1,699` net · `+4` objects · `~19` objects · `+1,699` atoms · 5 active days | `+6,608` net · `+17` objects · `~83` objects · `-1` object · `+6,634` atoms · `-12` atoms · 24 active days | AWS managed policies (7d, last changed [October 21, 2026](data/diffs/2026-10-21/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | `+2,456` net · `+16` objects · `~349` objects · `+2,487` atoms · `-31` atoms · 3 active days | `+3,797` net · `+30` objects · `~650` objects · `-7` objects · `+3,909` atoms · `-112` atoms · 7 active days | GCP predefined roles (7d, last changed [October 21, 2026](data/diffs/2026-10-21/gcp-predefined-roles.json)) |
| GitHub | No movement | `+9` net · `+4` objects · `~5` objects · `+4` atoms · 6 active days | GitHub fine-grained PAT permissions (30d, last changed [October 9, 2026](data/diffs/2026-10-09/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,607` | [October 21, 2026](data/diffs/2026-10-21/aws-managed-policies.json) | `+1,699` net · `+4` objects · `~19` objects · `+1,699` atoms · 5 active days | `+6,608` net · `+17` objects · `~83` objects · `-1` object · `+6,634` atoms · `-12` atoms · 24 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-21/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-21/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,404` | [October 21, 2026](data/diffs/2026-10-21/gcp-predefined-roles.json) | `+2,456` net · `+16` objects · `~349` objects · `+2,487` atoms · `-31` atoms · 3 active days | `+3,797` net · `+30` objects · `~650` objects · `-7` objects · `+3,909` atoms · `-112` atoms · 7 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-21/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-21/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 9, 2026](data/diffs/2026-10-09/github-fgpat-permissions.json) | No movement | `+7` net · `+3` objects · `~5` objects · `+3` atoms · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-21/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | No movement | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-21/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,607` objects.
- Last 7 days: `+1,699` net · `+4` objects · `~19` objects · `+1,699` atoms · 5 active days.
- Last 30 days: `+6,608` net · `+17` objects · `~83` objects · `-1` object · `+6,634` atoms · `-12` atoms · 24 active days.
- Recent highlights: October 21, 2026: +2 objects, ~2 changed, +1,568 atoms (`AWSFinOpsAgentServiceRolePolicy` (+231 atoms), `AssuranceServiceRolePolicy` (+1,283)); October 18, 2026: ~2 changed, +6 atoms (`AWSPartnerCentralFullAccess` (+6)); October 17, 2026: +1 objects, ~5 changed, +53 atoms (`AWSContinuumCollectorServiceRolePolicy` (+41 atoms), `AWSPartnerCentralMarketingManagement` (+4)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-10-21/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-10-21/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,404` objects.
- Last 7 days: `+2,456` net · `+16` objects · `~349` objects · `+2,487` atoms · `-31` atoms · 3 active days.
- Last 30 days: `+3,797` net · `+30` objects · `~650` objects · `-7` objects · `+3,909` atoms · `-112` atoms · 7 active days.
- Recent highlights: October 21, 2026: +4 objects, ~252 changed, +1,151 atoms, -8 atoms (`Folder level Compute VM extension policies admin Beta` (+31 atoms), `Cloud Dataplex Service Agent` (+44, -8)); October 17, 2026: ~5 changed (`Advisory Support Editor` (metadata only)); October 15, 2026: +12 objects, ~92 changed, +1,336 atoms, -23 atoms (`Wiz Cloud Inventory Viewer` (+350 atoms), `Chronicle API Restricted Data Access Viewer Beta` (+160)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-10-21/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: No movement.
- Last 30 days: `+7` net · `+3` objects · `~5` objects · `+3` atoms · 5 active days.
- Recent highlights: October 9, 2026: ~1 changed (`Repository creation` (+1)); October 6, 2026: ~1 changed (`Pull requests` (+1)); September 30, 2026: +2 objects, ~1 changed, +2 atoms (`External custom properties for repositories` (+1 atoms), `Actions` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-10-21/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-10-21/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-10-21/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
