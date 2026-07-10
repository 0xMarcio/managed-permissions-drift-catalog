# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: July 10, 2026 · [daily report](docs/daily/2026-07-10.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+132` net · `+6` objects · `~13` objects · `+132` atoms · 4 active days | `+998` net · `+21` objects · `~65` objects · `+1,026` atoms · `-26` atoms · 21 active days | AWS managed policies (7d, last changed [July 10, 2026](data/diffs/2026-07-10/aws-managed-policies.json)) |
| Azure | No movement | `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days | Azure built-in roles (30d, last changed [July 2, 2026](data/diffs/2026-07-02/azure-built-in-roles.json)) |
| GCP | `+1,675` net · `+13` objects · `~69` objects · `+1,680` atoms · `-5` atoms · 1 active day | `+2,620` net · `+39` objects · `~241` objects · `+2,634` atoms · `-14` atoms · 5 active days | GCP predefined roles (7d, last changed [July 9, 2026](data/diffs/2026-07-09/gcp-predefined-roles.json)) |
| GitHub | No movement | `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days | GitHub fine-grained PAT permissions (30d, last changed [June 30, 2026](data/diffs/2026-06-30/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,536` | [July 10, 2026](data/diffs/2026-07-10/aws-managed-policies.json) | `+132` net · `+6` objects · `~13` objects · `+132` atoms · 4 active days | `+998` net · `+21` objects · `~65` objects · `+1,026` atoms · `-26` atoms · 21 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-10/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `502` | [July 2, 2026](data/diffs/2026-07-02/azure-built-in-roles.json) | No movement | `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-10/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,362` | [July 9, 2026](data/diffs/2026-07-09/gcp-predefined-roles.json) | `+1,675` net · `+13` objects · `~69` objects · `+1,680` atoms · `-5` atoms · 1 active day | `+2,620` net · `+39` objects · `~241` objects · `+2,634` atoms · `-14` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-10/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-10/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [June 30, 2026](data/diffs/2026-06-30/github-fgpat-permissions.json) | No movement | `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-10/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-10/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,536` objects.
- Last 7 days: `+132` net · `+6` objects · `~13` objects · `+132` atoms · 4 active days.
- Last 30 days: `+998` net · `+21` objects · `~65` objects · `+1,026` atoms · `-26` atoms · 21 active days.
- Recent highlights: July 10, 2026: +1 objects, ~4 changed, +25 atoms (`AWSMCPSignInOAuthAccessPolicy` (+2 atoms), `NetworkAdministrator` (+13)); July 9, 2026: ~3 changed, +8 atoms (`AmazonInspector2ReadOnlyAccess` (+7)); July 8, 2026: +2 objects, ~4 changed, +49 atoms (`DBModVirtualSource` (+39 atoms), `AWSResilienceHubServiceRolePolicy` (+6)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-07-10/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `502` objects.
- Last 7 days: No movement.
- Last 30 days: `+13` net · `+1` object · `~9` objects · `+18` atoms · `-3` atoms · 2 active days.
- Recent highlights: July 2, 2026: +1 objects, ~4 changed, +12 atoms, -1 atoms (`Azure Device Registry Administrator` (+1 atoms), `Container Registry Configuration Reader and Data Access Configuration Reader` (+6)); June 21, 2026: ~5 changed, +6 atoms, -2 atoms (`Foundry Owner` (+2)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-07-10/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,362` objects.
- Last 7 days: `+1,675` net · `+13` objects · `~69` objects · `+1,680` atoms · `-5` atoms · 1 active day.
- Last 30 days: `+2,620` net · `+39` objects · `~241` objects · `+2,634` atoms · `-14` atoms · 5 active days.
- Recent highlights: July 9, 2026: +13 objects, ~69 changed, +1,680 atoms, -5 atoms (`Cloud Asset Admin` (+582 atoms), `Customer Engagement Suite Service Agent` (+52)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-07-10/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: No movement.
- Last 30 days: `+1` net · `+1` object · `~7` objects · `+1` atom · 4 active days.
- Recent highlights: June 30, 2026: ~1 changed (`Administration` (+1, -1)); June 26, 2026: +1 objects, +1 atoms (`Code quality` (+1 atoms)); June 24, 2026: ~1 changed (`Administration` (+3)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-07-10/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-07-10/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-07-10/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
