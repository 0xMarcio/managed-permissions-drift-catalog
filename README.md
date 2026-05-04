# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed at: `2026-05-04T04:35:48Z` · [daily report](docs/daily/2026-05-04.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+35` net · `+1` object · `~11` objects · `+35` atoms · 5 active days | `+155` net · `+1` object · `~28` objects · `+213` atoms · `-58` atoms · 11 active days | AWS managed policies (7d, last changed [2026-05-03](data/diffs/2026-05-03/aws-managed-policies.json)) |
| Azure | No movement | No movement | No movement |
| GCP | No movement | `+2,649` net · `+51` objects · `~171` objects · `-2` objects · `+2,697` atoms · `-48` atoms · 1 active day | GCP predefined roles (30d, last changed [2026-04-21](data/diffs/2026-04-21/gcp-predefined-roles.json)) |
| GitHub | `+3` net · `+1` object · `~1` object · `+2` atoms · 2 active days | `+4` net · `+2` objects · `~4` objects · `+3` atoms · 4 active days | GitHub fine-grained PAT permissions (7d, last changed [2026-05-02](data/diffs/2026-05-02/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,499` | [2026-05-03](data/diffs/2026-05-03/aws-managed-policies.json) | `+35` net · `+1` object · `~11` objects · `+35` atoms · 5 active days | `+155` net · `+1` object · `~28` objects · `+213` atoms · `-58` atoms · 11 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-04/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `498` | No movement | No movement | No movement | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-04/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,293` | [2026-04-21](data/diffs/2026-04-21/gcp-predefined-roles.json) | No movement | `+2,649` net · `+51` objects · `~171` objects · `-2` objects · `+2,697` atoms · `-48` atoms · 1 active day | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-04/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-04/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `67` | [2026-05-02](data/diffs/2026-05-02/github-fgpat-permissions.json) | `+3` net · `+1` object · `~1` object · `+2` atoms · 2 active days | `+3` net · `+1` object · `~3` objects · `+2` atoms · 3 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-04/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | [2026-04-24](data/diffs/2026-04-24/github-token-permissions.json) | No movement | `+1` net · `+1` object · `~1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-04/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,499` objects.
- Last 7 days: `+35` net · `+1` object · `~11` objects · `+35` atoms · 5 active days.
- Last 30 days: `+155` net · `+1` object · `~28` objects · `+213` atoms · `-58` atoms · 11 active days.
- Recent highlights: 2026-05-03: ~1 changed, +1 atoms (`AmazonCognitoUnAuthedIdentitiesSessionPolicy` (+1)); 2026-05-02: ~1 changed, +1 atoms (`SecurityAudit` (+1)); 2026-05-01: ~5 changed, +21 atoms (`AWSObservabilityAdminTelemetryEnablementServiceRolePolicy` (+11)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-04/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `498` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-04/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,293` objects.
- Last 7 days: No movement.
- Last 30 days: `+2,649` net · `+51` objects · `~171` objects · `-2` objects · `+2,697` atoms · `-48` atoms · 1 active day.
- Recent highlights: 2026-04-21: +51 objects, ~171 changed, -2 removed, +2,697 atoms, -48 atoms (`Aiplatform Editor` (+432 atoms), `Support User` (+79)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-04/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `67` objects.
- Last 7 days: `+3` net · `+1` object · `~1` object · `+2` atoms · 2 active days.
- Last 30 days: `+3` net · `+1` object · `~3` objects · `+2` atoms · 3 active days.
- Recent highlights: 2026-05-02: +1 objects, +2 atoms (`Copilot Spaces` (+2 atoms)); 2026-05-01: ~1 changed (`GitHub Copilot Business` (+4)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-04/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: `+1` net · `+1` object · `~1` object · `+1` atom · 1 active day.
- Recent highlights: 2026-04-24: +1 objects, ~1 changed, +1 atoms (`vulnerability-alerts` (+1 atoms), `security-events` (metadata only)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-04/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-04/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
