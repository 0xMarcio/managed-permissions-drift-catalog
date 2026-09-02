# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: September 2, 2026 · [daily report](docs/daily/2026-09-02.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+478` net · `+2` objects · `~19` objects · `+478` atoms · 5 active days | `+2,557` net · `+26` objects · `~81` objects · `+2,587` atoms · `-12` atoms · 17 active days | AWS managed policies (7d, last changed [September 2, 2026](data/diffs/2026-09-02/aws-managed-policies.json)) |
| Azure | No movement | `~4` objects · 1 active day | Azure built-in roles (30d, last changed [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json)) |
| GCP | No movement | `+1,014` net · `+9` objects · `~172` objects · `+1,023` atoms · `-9` atoms · 5 active days | GCP predefined roles (30d, last changed [August 26, 2026](data/diffs/2026-08-26/gcp-predefined-roles.json)) |
| GitHub | No movement | `~2` objects · 2 active days | GitHub fine-grained PAT permissions (30d, last changed [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,585` | [September 2, 2026](data/diffs/2026-09-02/aws-managed-policies.json) | `+478` net · `+2` objects · `~19` objects · `+478` atoms · 5 active days | `+2,557` net · `+26` objects · `~81` objects · `+2,587` atoms · `-12` atoms · 17 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-02/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [August 12, 2026](data/diffs/2026-08-12/azure-built-in-roles.json) | No movement | `~4` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-02/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,375` | [August 26, 2026](data/diffs/2026-08-26/gcp-predefined-roles.json) | No movement | `+1,014` net · `+9` objects · `~172` objects · `+1,023` atoms · `-9` atoms · 5 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-02/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-02/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `73` | [August 22, 2026](data/diffs/2026-08-22/github-fgpat-permissions.json) | No movement | `~2` objects · 2 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-02/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-02/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,585` objects.
- Last 7 days: `+478` net · `+2` objects · `~19` objects · `+478` atoms · 5 active days.
- Last 30 days: `+2,557` net · `+26` objects · `~81` objects · `+2,587` atoms · `-12` atoms · 17 active days.
- Recent highlights: September 2, 2026: ~8 changed, +59 atoms (`CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy` (+19)); August 30, 2026: ~2 changed, +4 atoms (`AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy` (+4)); August 29, 2026: ~5 changed, +19 atoms (`AWSConfigServiceRolePolicy` (+8)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-02/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~4` objects · 1 active day.
- Recent highlights: August 12, 2026: ~4 changed (`Logic Apps Standard Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-02/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,375` objects.
- Last 7 days: No movement.
- Last 30 days: `+1,014` net · `+9` objects · `~172` objects · `+1,023` atoms · `-9` atoms · 5 active days.
- Recent highlights: August 26, 2026: +1 objects, ~49 changed, +90 atoms, -9 atoms (`Analytics Hub Service Agent` (+3 atoms), `Chronicle Service Agent` (+10)); August 20, 2026: +4 objects, ~51 changed, +345 atoms (`Cloud FTP Admin` (+20 atoms), `Security Admin` (+16)); August 18, 2026: ~2 changed (`Cloud Run SSH Read Only Beta` (metadata only)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-02/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `73` objects.
- Last 7 days: No movement.
- Last 30 days: `~2` objects · 2 active days.
- Recent highlights: August 22, 2026: ~1 changed (`Metadata` (+1)); August 7, 2026: ~1 changed (`Administration` (+1)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-02/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-02/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-02/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
