# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: June 23, 2026 · [daily report](docs/daily/2026-06-23.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+269` net · `+2` objects · `~14` objects · `+269` atoms · 5 active days | `+744` net · `+16` objects · `~55` objects · `+877` atoms · `-77` atoms · 16 active days | AWS managed policies (7d, last changed [June 23, 2026](data/diffs/2026-06-23/aws-managed-policies.json)) |
| Azure | `+4` net · `~5` objects · `+6` atoms · `-2` atoms · 1 active day | `-10` net · `+1` object · `~20` objects · `+32` atoms · `-6` atoms · 4 active days | Azure built-in roles (7d, last changed [June 21, 2026](data/diffs/2026-06-21/azure-built-in-roles.json)) |
| GCP | `+126` net · `+10` objects · `~30` objects · `+126` atoms · 1 active day | `+787` net · `+24` objects · `~148` objects · `+795` atoms · `-8` atoms · 4 active days | GCP predefined roles (7d, last changed [June 23, 2026](data/diffs/2026-06-23/gcp-predefined-roles.json)) |
| GitHub | `~5` objects · 1 active day | `~9` objects · 3 active days | GitHub fine-grained PAT permissions (7d, last changed [June 19, 2026](data/diffs/2026-06-19/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,520` | [June 23, 2026](data/diffs/2026-06-23/aws-managed-policies.json) | `+269` net · `+2` objects · `~14` objects · `+269` atoms · 5 active days | `+744` net · `+16` objects · `~55` objects · `+877` atoms · `-77` atoms · 16 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-23/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `501` | [June 21, 2026](data/diffs/2026-06-21/azure-built-in-roles.json) | `+4` net · `~5` objects · `+6` atoms · `-2` atoms · 1 active day | `-10` net · `+1` object · `~20` objects · `+32` atoms · `-6` atoms · 4 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-23/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,334` | [June 23, 2026](data/diffs/2026-06-23/gcp-predefined-roles.json) | `+126` net · `+10` objects · `~30` objects · `+126` atoms · 1 active day | `+787` net · `+24` objects · `~148` objects · `+795` atoms · `-8` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-23/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-23/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `72` | [June 19, 2026](data/diffs/2026-06-19/github-fgpat-permissions.json) | `~5` objects · 1 active day | `~9` objects · 3 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-23/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-23/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,520` objects.
- Last 7 days: `+269` net · `+2` objects · `~14` objects · `+269` atoms · 5 active days.
- Last 30 days: `+744` net · `+16` objects · `~55` objects · `+877` atoms · `-77` atoms · 16 active days.
- Recent highlights: June 23, 2026: +1 objects, ~3 changed, +7 atoms (`AWSLambdaNetworkConnectorOperatorPolicy` (+2 atoms), `AWSLambdaServiceRolePolicy` (+4)); June 21, 2026: ~1 changed, +1 atoms (`EC2ApplicationStatusChecksServiceRolePolicy` (+1)); June 20, 2026: ~4 changed, +7 atoms (`AmazonEMRContainersServiceRolePolicy` (+6)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-06-23/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `501` objects.
- Last 7 days: `+4` net · `~5` objects · `+6` atoms · `-2` atoms · 1 active day.
- Last 30 days: `-10` net · `+1` object · `~20` objects · `+32` atoms · `-6` atoms · 4 active days.
- Recent highlights: June 21, 2026: ~5 changed, +6 atoms, -2 atoms (`Foundry Owner` (+2)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-06-23/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,334` objects.
- Last 7 days: `+126` net · `+10` objects · `~30` objects · `+126` atoms · 1 active day.
- Last 30 days: `+787` net · `+24` objects · `~148` objects · `+795` atoms · `-8` atoms · 4 active days.
- Recent highlights: June 23, 2026: +10 objects, ~30 changed, +126 atoms (`Data Studio Managed Storage Service Agent` (+11 atoms), `Dataplex Administrator` (+11)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-06-23/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `72` objects.
- Last 7 days: `~5` objects · 1 active day.
- Last 30 days: `~9` objects · 3 active days.
- Recent highlights: June 19, 2026: ~5 changed (`Artifact metadata` (+5, -5)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-06-23/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-06-23/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-06-23/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
