# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed: November 11, 2026 · [daily report](docs/daily/2026-11-11.md)

## Platform overview

| Platform | Last 7 days | Last 30 days | Main recent driver |
| --- | --- | --- | --- |
| AWS | `-35` net · `+4` objects · `~42` objects · `+462` atoms · `-27` atoms · 5 active days | `+2,973` net · `+17` objects · `~126` objects · `+3,484` atoms · `-39` atoms · 22 active days | AWS managed policies (7d, last changed [November 11, 2026](data/diffs/2026-11-11/aws-managed-policies.json)) |
| Azure | No movement | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | Azure built-in roles (30d, last changed [November 4, 2026](data/diffs/2026-11-04/azure-built-in-roles.json)) |
| GCP | No movement | `+4,243` net · `+23` objects · `~538` objects · `+4,299` atoms · `-56` atoms · 6 active days | GCP predefined roles (30d, last changed [November 4, 2026](data/diffs/2026-11-04/gcp-predefined-roles.json)) |
| GitHub | `~4` objects · 3 active days | `+2` net · `+1` object · `~7` objects · `+1` atom · 6 active days | GitHub fine-grained PAT permissions (7d, last changed [November 10, 2026](data/diffs/2026-11-10/github-fgpat-permissions.json)) |

## Dataset overview

| Dataset | Inventory | Last changed | Last 7 days | Last 30 days | Files |
| --- | ---: | --- | --- | --- | --- |
| AWS managed policies | `1,618` | [November 11, 2026](data/diffs/2026-11-11/aws-managed-policies.json) | `-35` net · `+4` objects · `~42` objects · `+462` atoms · `-27` atoms · 5 active days | `+2,973` net · `+17` objects · `~126` objects · `+3,484` atoms · `-39` atoms · 22 active days | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-11/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `506` | [November 4, 2026](data/diffs/2026-11-04/azure-built-in-roles.json) | No movement | `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-11/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,411` | [November 4, 2026](data/diffs/2026-11-04/gcp-predefined-roles.json) | No movement | `+4,243` net · `+23` objects · `~538` objects · `+4,299` atoms · `-56` atoms · 6 active days | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-11/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | No movement | No movement | No movement | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-11/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `76` | [November 10, 2026](data/diffs/2026-11-10/github-fgpat-permissions.json) | `~4` objects · 3 active days | `~7` objects · 5 active days | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-11/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `17` | [October 14, 2026](data/diffs/2026-10-14/github-token-permissions.json) | No movement | `+2` net · `+1` object · `+1` atom · 1 active day | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-11/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,618` objects.
- Last 7 days: `-35` net · `+4` objects · `~42` objects · `+462` atoms · `-27` atoms · 5 active days.
- Last 30 days: `+2,973` net · `+17` objects · `~126` objects · `+3,484` atoms · `-39` atoms · 22 active days.
- Recent highlights: November 11, 2026: ~15 changed, +75 atoms, -23 atoms (`AWSApplicationMigrationNetworkMigrationMultiAccount` (+20)); November 10, 2026: ~4 changed, +8 atoms (`AWSApplicationMigrationReadOnlyAccess` (+5)); November 8, 2026: +2 objects, ~6 changed, +46 atoms (`AIDevOpsOrganizationsAccessPolicy` (+19 atoms), `AmazonBioDiscoveryFullAccess` (+7)).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-11-11/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `506` objects.
- Last 7 days: No movement.
- Last 30 days: `+10` net · `+2` objects · `~5` objects · `+10` atoms · 2 active days.
- Recent highlights: November 4, 2026: +2 objects, ~4 changed, +8 atoms (`Foundry Project Runtime User` (+3 atoms), `Foundry Account Owner` (+1)); October 30, 2026: ~1 changed, +2 atoms (`FHIR Data Bulk Operator` (+2)).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-11-11/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,411` objects.
- Last 7 days: No movement.
- Last 30 days: `+4,243` net · `+23` objects · `~538` objects · `+4,299` atoms · `-56` atoms · 6 active days.
- Recent highlights: November 4, 2026: ~117 changed, +906 atoms, -11 atoms (`DLP Organization Data Profiles Driver` (+63)); October 29, 2026: +7 objects, ~71 changed, +906 atoms, -14 atoms (`Cloud Functions Service Agent` (+265 atoms), `Wiz Cloud Inventory Viewer` (+259)); October 21, 2026: +4 objects, ~252 changed, +1,151 atoms, -8 atoms (`Folder level Compute VM extension policies admin Beta` (+31 atoms), `Cloud Dataplex Service Agent` (+44, -8)).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-11-11/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `76` objects.
- Last 7 days: `~4` objects · 3 active days.
- Last 30 days: `~7` objects · 5 active days.
- Recent highlights: November 10, 2026: ~2 changed (`Administration` (+2)); November 7, 2026: ~1 changed (`Administration` (+2)); November 5, 2026: ~1 changed (`Copilot agent settings` (+3)).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-11-11/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `17` objects.
- Last 7 days: No movement.
- Last 30 days: `+2` net · `+1` object · `+1` atom · 1 active day.
- Recent highlights: October 14, 2026: +1 objects, +1 atoms (`copilot-requests` (+1 atoms)).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-11-11/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Last 7 days: No movement.
- Last 30 days: No movement.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-11-11/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
