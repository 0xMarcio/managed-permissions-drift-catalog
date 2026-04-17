# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed at: `2026-04-17T20:32:18Z` · [daily report](docs/daily/2026-04-17.md)
- Leading platform: `GCP` (`+122,768` net score)
- Driver: `GCP predefined roles` (+2,244 objects, +122,768 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+47,341` | `+1,498 / ~0 / -0` | `+50,953 / -0` | AWS managed policies (+1,498 objects, +50,953 atoms) |
| Azure | `+5,604` | `+498 / ~0 / -0` | `+6,024 / -0` | Azure built-in roles (+498 objects, +6,024 atoms) |
| GCP | `+122,768` | `+2,244 / ~0 / -0` | `+122,768 / -0` | GCP predefined roles (+2,244 objects, +122,768 atoms) |
| GitHub | `+232` | `+87 / ~0 / -0` | `+177 / -0` | GitHub fine-grained PAT permissions (+66 objects, +118 atoms) |

## Dataset overview

| Dataset | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | ---: | ---: | ---: | --- |
| AWS managed policies | `1,498` | `+1,498 / ~0 / -0` | `+50,953 / -0` | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-04-17/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `498` | `+498 / ~0 / -0` | `+6,024 / -0` | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-04-17/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,244` | `+2,244 / ~0 / -0` | `+122,768 / -0` | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-04-17/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | `+6 / ~0 / -0` | `+31 / -0` | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-04-17/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `66` | `+66 / ~0 / -0` | `+118 / -0` | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-04-17/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `15` | `+15 / ~0 / -0` | `+28 / -0` | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-04-17/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,498` objects.
- Today: +1,498 objects, +50,953 atoms.
- Biggest additions: `AWSSupportServiceRolePolicy` (+4,054 atoms), `ReadOnlyAccess` (+2,744 atoms), `AWSConfigServiceRolePolicy` (+2,262 atoms).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-04-17/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `498` objects.
- Today: +498 objects, +6,024 atoms.
- Biggest additions: `Azure Stack HCI Administrator` (+101 atoms), `Backup Operator` (+98 atoms), `Azure AI Enterprise Network Connection Approver` (+89 atoms).
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-04-17/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,244` objects.
- Today: +2,244 objects, +122,768 atoms.
- Biggest additions: `Support User` (+6,207 atoms), `Security Auditor` (+3,805 atoms), `Security Admin` (+2,712 atoms).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-04-17/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `66` objects.
- Today: +66 objects, +118 atoms.
- Biggest additions: `Custom properties` (+3 atoms), `Actions` (+2 atoms), `Administration` (+2 atoms).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-04-17/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `15` objects.
- Today: +15 objects, +28 atoms.
- Biggest additions: `actions` (+2 atoms), `artifact-metadata` (+2 atoms), `attestations` (+2 atoms).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-04-17/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Today: +6 objects, +31 atoms.
- Biggest additions: `Get GitHub Actions permissions for an organization` (+8 atoms), `Get GitHub Actions permissions for a repository` (+7 atoms), `Get allowed actions and reusable workflows for a repository` (+4 atoms).
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-04-17/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
