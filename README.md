# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: November 4, 2026 · [daily report](docs/daily/2026-11-04.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+969` net · `+5` objects · `~36` objects · `+972` atoms · `-1` atom · 5 active days | `+3,380` net · `+14` objects · `~106` objects · `+3,403` atoms · `-13` atoms · 24 active days | AWS managed policies (7d, last changed [November 4, 2026](data/diffs/2026-11-04/aws-managed-policies.json)) |
| Azure | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | Azure built-in roles (7d, last changed [November 4, 2026](data/diffs/2026-11-04/azure-built-in-roles.json)) |
| GCP | `+1,787` net · `+7` objects · `~188` objects · `+1,812` atoms · `-25` atoms · 2 active days | `+5,005` net · `+26` objects · `~728` objects · `-1` object · `+5,089` atoms · `-84` atoms · 7 active days | GCP predefined roles (7d, last changed [November 4, 2026](data/diffs/2026-11-04/gcp-predefined-roles.json)) |
| GitHub | `~1` object · 1 active day | `+2` net · `+1` object · `~5` objects · `+1` atom · 5 active days | GitHub fine-grained PAT permissions (7d, last changed [October 29, 2026](data/diffs/2026-10-29/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,614` | [November 4, 2026](data/diffs/2026-11-04/aws-managed-policies.json) | `+969` net · `+5` objects · `~36` objects · `+972` atoms · `-1` atom · 5 active days | `+3,380` net · `+14` objects · `~106` objects · `+3,403` atoms · `-13` atoms · 24 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-04/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `506` | [November 4, 2026](data/diffs/2026-11-04/azure-built-in-roles.json) | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-04/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,411` | [November 4, 2026](data/diffs/2026-11-04/gcp-predefined-roles.json) | `+1,787` net · `+7` objects · `~188` objects · `+1,812` atoms · `-25` atoms · 2 active days | `+5,005` net · `+26` objects · `~728` objects · `-1` object · `+5,089` atoms · `-84` atoms · 7 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-04/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-04/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [October 29, 2026](data/diffs/2026-10-29/github-fgpat-permissions.json) | `~1` object · 1 active day | `~5` objects · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-04/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | No movement | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-04/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,614` objects.
- Last 7 days: `+969` net · `+5` objects · `~36` objects · `+972` atoms · `-1` atom · 5 active days.
- Last 30 days: `+3,380` net · `+14` objects · `~106` objects · `+3,403` atoms · `-13` atoms · 24 active days.
- Recent highlights: November 4, 2026: ~4 changed, +3 atoms (`CloudWatchAPIKeyAccess` (+1)); November 1, 2026: +1 objects, ~4 changed, +72 atoms (`Route53PrivateHealthChecksServiceRolePolicy` (+7 atoms), `ReadOnlyAccess` (+49)); October 31, 2026: +1 objects, ~12 changed, +235 atoms (`FinOpsAgentIdentityReaderPolicy` (+3 atoms), `ViewOnlyAccess` (+87)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-04/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `506` objects.
- Last 7 days: `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days.
- Last 30 days: `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days.
- Recent highlights: November 4, 2026: +2 objects, ~4 changed, +8 atoms (`Foundry Project Runtime User` (+3 atoms), `Foundry Account Owner` (+1)); October 30, 2026: ~1 changed, +2 atoms (`FHIR Data Bulk Operator` (+2)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-04/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,411` objects.
- Last 7 days: `+1,787` net · `+7` objects · `~188` objects · `+1,812` atoms · `-25` atoms · 2 active days.
- Last 30 days: `+5,005` net · `+26` objects · `~728` objects · `-1` object · `+5,089` atoms · `-84` atoms · 7 active days.
- Recent highlights: November 4, 2026: ~117 changed, +906 atoms, -11 atoms (`DLP Organization Data Profiles Driver` (+63)); October 29, 2026: +7 objects, ~71 changed, +906 atoms, -14 atoms (`Cloud Functions Service Agent` (+265 atoms), `Wiz Cloud Inventory Viewer` (+259)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-04/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `~5` objects · 4 active days.
- Recent highlights: October 29, 2026: ~1 changed (`Repository security advisories` (+4)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-04/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-04/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-04/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
