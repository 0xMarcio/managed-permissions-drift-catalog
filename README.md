# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed at: `2026-04-23T04:24:06Z` · [daily report](docs/daily/2026-04-23.md)
- Leading platform: none

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `0` | `+0 / ~7 / -0` | `+22 / -22` | AWS managed policies (~7 changed, +22 atoms, -22 atoms) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `0` | `+0 / ~0 / -0` | `+0 / -0` | GCP predefined roles (no drift) |
| GitHub | `0` | `+0 / ~2 / -0` | `+0 / -0` | GitHub fine-grained PAT permissions (~2 changed) |

## Dataset overview

| Dataset | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | ---: | ---: | ---: | --- |
| AWS managed policies | `1,498` | `+0 / ~7 / -0` | `+22 / -22` | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-04-23/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `498` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-04-23/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,293` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-04-23/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-04-23/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `66` | `+0 / ~2 / -0` | `+0 / -0` | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-04-23/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `15` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-04-23/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,498` objects.
- Today: ~7 changed, +22 atoms, -22 atoms.
- Biggest changes: `AWSSecurityIncidentResponseFullAccess` (+9, -22), `AWSMarketplaceSellerFullAccess` (+4), `AWSMarketplaceProcurementSystemAdminFullAccess` (+3).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-04-23/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `498` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-04-23/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,293` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-04-23/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `66` objects.
- Today: ~2 changed; no atom-level change.
- Biggest changes: `Pull requests` (+5, -3), `Issues` (+3, -3).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-04-23/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `15` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-04-23/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-04-23/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
