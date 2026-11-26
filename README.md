# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: November 26, 2026 · [daily report](docs/daily/2026-11-26.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `+3,700` net · `+12` objects · `~55` objects · `+3,720` atoms · 6 active days | `+6,611` net · `+36` objects · `~204` objects · `+7,207` atoms · `-102` atoms · 23 active days | AWS managed policies (7d, last changed [November 26, 2026](data/diffs/2026-11-26/aws-managed-policies.json)) |
| Azure | No movement | `+44` net · `+3` objects · `~5` objects · `+44` atoms · 3 active days | Azure built-in roles (30d, last changed [November 19, 2026](data/diffs/2026-11-19/azure-built-in-roles.json)) |
| GCP | `~1` object · 1 active day | `+2,474` net · `+18` objects · `~269` objects · `+2,549` atoms · `-75` atoms · 4 active days | GCP predefined roles (7d, last changed [November 24, 2026](data/diffs/2026-11-24/gcp-predefined-roles.json)) |
| GitHub | No movement | `+6` net · `+2` objects · `~8` objects · `+4` atoms · 7 active days | GitHub fine-grained PAT permissions (30d, last changed [November 18, 2026](data/diffs/2026-11-18/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,644` | [November 26, 2026](data/diffs/2026-11-26/aws-managed-policies.json) | `+3,700` net · `+12` objects · `~55` objects · `+3,720` atoms · 6 active days | `+6,611` net · `+36` objects · `~204` objects · `+7,207` atoms · `-102` atoms · 23 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-26/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `507` | [November 19, 2026](data/diffs/2026-11-19/azure-built-in-roles.json) | No movement | `+44` net · `+3` objects · `~5` objects · `+44` atoms · 3 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-26/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,422` | [November 24, 2026](data/diffs/2026-11-24/gcp-predefined-roles.json) | `~1` object · 1 active day | `+2,474` net · `+18` objects · `~269` objects · `+2,549` atoms · `-75` atoms · 4 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-26/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-26/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `78` | [November 18, 2026](data/diffs/2026-11-18/github-fgpat-permissions.json) | No movement | `+6` net · `+2` objects · `~8` objects · `+4` atoms · 7 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-26/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | No movement | No movement | No movement | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-26/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,644` objects.
- Last 7 days: `+3,700` net · `+12` objects · `~55` objects · `+3,720` atoms · 6 active days.
- Last 30 days: `+6,611` net · `+36` objects · `~204` objects · `+7,207` atoms · `-102` atoms · 23 active days.
- Recent highlights: November 26, 2026: +1 objects, ~1 changed, +8 atoms (`AWSContinuumConfigurationsServiceRolePolicy` (+7 atoms), `CloudWatchReadOnlyAccess` (+1)); November 25, 2026: +1 objects, ~4 changed, +19 atoms (`CloudWatchOmniProvisioningPolicy` (+12 atoms), `AmazonLaunchWizardFullAccessV2` (+4)); November 24, 2026: ~1 changed, +1 atoms (`CloudWatchReadOnlyAccess` (+1)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-26/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `507` objects.
- Last 7 days: No movement.
- Last 30 days: `+44` net · `+3` objects · `~5` objects · `+44` atoms · 3 active days.
- Recent highlights: November 19, 2026: +1 objects, +34 atoms (`Azure Arc Kubernetes Reader` (+34 atoms)); November 4, 2026: +2 objects, ~4 changed, +8 atoms (`Foundry Project Runtime User` (+3 atoms), `Foundry Account Owner` (+1)); October 30, 2026: ~1 changed, +2 atoms (`FHIR Data Bulk Operator` (+2)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-26/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,422` objects.
- Last 7 days: `~1` object · 1 active day.
- Last 30 days: `+2,474` net · `+18` objects · `~269` objects · `+2,549` atoms · `-75` atoms · 4 active days.
- Recent highlights: November 24, 2026: ~1 changed (`Data pipelines Invoker` (metadata only)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-26/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `78` objects.
- Last 7 days: No movement.
- Last 30 days: `+6` net · `+2` objects · `~8` objects · `+4` atoms · 7 active days.
- Recent highlights: November 18, 2026: ~1 changed (`Issues` (+1)); November 12, 2026: +2 objects, +4 atoms (`Issue Fields` (+2 atoms)); November 10, 2026: ~2 changed (`Administration` (+2)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-26/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-26/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-26/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
