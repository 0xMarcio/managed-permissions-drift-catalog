# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: September 25, 2026 · [daily report](docs/daily/2026-09-25.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+1,046` net · `+7` objects · `~10` objects · `+1,052` atoms · 5 active days | `+2,862` net · `+15` objects · `~71` objects · `+2,868` atoms · 20 active days | AWS managed policies (7d, last changed [September 25, 2026](data/diffs/2026-09-25/aws-managed-policies.json)) |
| Azure | No movement | `~3` objects · 1 active day | Azure built-in roles (30d, last changed [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json)) |
| GCP | `+265` net · `+6` objects · `~43` objects · `+265` atoms · 1 active day | `+1,333` net · `+14` objects · `~253` objects · `-2` objects · `+1,391` atoms · `-58` atoms · 3 active days | GCP predefined roles (7d, last changed [September 23, 2026](data/diffs/2026-09-23/gcp-predefined-roles.json)) |
| GitHub | `+2` net · `+1` object · `~1` object · `+1` atom · 1 active day | `+2` net · `+1` object · `~11` objects · `+1` atom · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [September 25, 2026](data/diffs/2026-09-25/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,598` | [September 25, 2026](data/diffs/2026-09-25/aws-managed-policies.json) | `+1,046` net · `+7` objects · `~10` objects · `+1,052` atoms · 5 active days | `+2,862` net · `+15` objects · `~71` objects · `+2,868` atoms · 20 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-25/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `504` | [September 4, 2026](data/diffs/2026-09-04/azure-built-in-roles.json) | No movement | `~3` objects · 1 active day | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-25/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,387` | [September 23, 2026](data/diffs/2026-09-23/gcp-predefined-roles.json) | `+265` net · `+6` objects · `~43` objects · `+265` atoms · 1 active day | `+1,333` net · `+14` objects · `~253` objects · `-2` objects · `+1,391` atoms · `-58` atoms · 3 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-25/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-25/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `74` | [September 25, 2026](data/diffs/2026-09-25/github-fgpat-permissions.json) | `+2` net · `+1` object · `~1` object · `+1` atom · 1 active day | `+2` net · `+1` object · `~11` objects · `+1` atom · 6 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-25/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-25/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,598` objects.
- Last 7 days: `+1,046` net · `+7` objects · `~10` objects · `+1,052` atoms · 5 active days.
- Last 30 days: `+2,862` net · `+15` objects · `~71` objects · `+2,868` atoms · 20 active days.
- Recent highlights: September 25, 2026: ~4 changed, +386 atoms (`AWSConfigServiceRolePolicy` (+192)); September 24, 2026: +1 objects, ~1 changed, +8 atoms (`AWSTransferServiceRolePolicy` (+5 atoms), `SageMakerStudioProjectProvisioningRolePolicy` (+3)); September 23, 2026: +6 objects, ~3 changed, +653 atoms (`CloudWatchOmniAWSIntegrationPolicy` (+499 atoms), `CloudWatchFullAccessV2` (+5)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-09-25/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `504` objects.
- Last 7 days: No movement.
- Last 30 days: `~3` objects · 1 active day.
- Recent highlights: September 4, 2026: ~3 changed (`Search Index Data Contributor` (metadata only)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-09-25/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,387` objects.
- Last 7 days: `+265` net · `+6` objects · `~43` objects · `+265` atoms · 1 active day.
- Last 30 days: `+1,333` net · `+14` objects · `~253` objects · `-2` objects · `+1,391` atoms · `-58` atoms · 3 active days.
- Recent highlights: September 23, 2026: +6 objects, ~43 changed, +265 atoms (`Universal Ledger Admin Beta` (+6 atoms), `SaaS Service Management Service Agent` (+23)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-09-25/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `74` objects.
- Last 7 days: `+2` net · `+1` object · `~1` object · `+1` atom · 1 active day.
- Last 30 days: `+2` net · `+1` object · `~11` objects · `+1` atom · 6 active days.
- Recent highlights: September 25, 2026: +1 objects, ~1 changed, +1 atoms (`Repository creation` (+1 atoms), `Administration` (+2, -2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-09-25/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-09-25/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-09-25/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
