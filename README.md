# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed at: `2026-05-02T04:28:04Z` · [daily report](docs/daily/2026-05-02.md)
- Leading platform: `GitHub` (`+3` net score)
- Driver: `GitHub fine-grained PAT permissions` (+1 objects, +2 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+1` | `+0 / ~1 / -0` | `+1 / -0` | AWS managed policies (~1 changed, +1 atoms) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `0` | `+0 / ~0 / -0` | `+0 / -0` | GCP predefined roles (no drift) |
| GitHub | `+3` | `+1 / ~0 / -0` | `+2 / -0` | GitHub fine-grained PAT permissions (+1 objects, +2 atoms) |

## Dataset overview

| Dataset | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | ---: | ---: | ---: | --- |
| AWS managed policies | `1,499` | `+0 / ~1 / -0` | `+1 / -0` | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-02/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `498` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-02/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,293` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-02/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-02/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `67` | `+1 / ~0 / -0` | `+2 / -0` | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-02/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `16` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-02/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,499` objects.
- Today: ~1 changed, +1 atoms.
- Biggest changes: `SecurityAudit` (+1).
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-05-02/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `498` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-05-02/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,293` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-05-02/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `67` objects.
- Today: +1 objects, +2 atoms.
- Biggest additions: `Copilot Spaces` (+2 atoms).
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-05-02/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `16` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-05-02/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-05-02/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
