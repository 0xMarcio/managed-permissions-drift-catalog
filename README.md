# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed at: `2026-04-24T04:27:09Z` · [daily report](docs/daily/2026-04-24.md)
- Leading platform: `AWS` (`+116` net score)
- Driver: `AWS managed policies` (~5 changed, +152 atoms, -36 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+116` | `+0 / ~5 / -0` | `+152 / -36` | AWS managed policies (~5 changed, +152 atoms, -36 atoms) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `0` | `+0 / ~0 / -0` | `+0 / -0` | GCP predefined roles (no drift) |
| GitHub | `+1` | `+1 / ~1 / -0` | `+1 / -0` | GitHub GITHUB_TOKEN permissions (+1 objects, ~1 changed, +1 atoms) |

## Dataset overview

| Dataset | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | ---: | ---: | ---: | --- |
| AWS managed policies | `1,498` | `+0 / ~5 / -0` | `+152 / -36` | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-04-24/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `498` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-04-24/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,293` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-04-24/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-04-24/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `66` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-04-24/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | `+1 / ~1 / -0` | `+1 / -0` | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-04-24/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,498` objects.
- Today: ~5 changed, +152 atoms, -36 atoms.
- Biggest changes: `AWSSupportServiceRolePolicy` (+146, -31), `AIDevOpsAgentAccessPolicy` (+3, -5), `ViewOnlyAccess` (+2).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-04-24/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `498` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-04-24/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,293` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-04-24/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `66` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-04-24/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Today: +1 objects, ~1 changed, +1 atoms.
- Biggest additions: `vulnerability-alerts` (+1 atoms).
- Biggest changes: `security-events` (metadata only).
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-04-24/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-04-24/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
