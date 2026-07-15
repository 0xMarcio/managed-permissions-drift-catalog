# Managed Permissions Drift Catalog

- Refreshed: July 15, 2026 · [daily report](daily/2026-07-15.md)
- Leading platform: `GCP` (`+109` net score)
- Driver: `GCP predefined roles` (~41 changed, +169 atoms, -60 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `0` | `+0 / ~0 / -0` | `+0 / -0` | AWS managed policies (no drift) |
| Azure | `+98` | `+2 / ~0 / -0` | `+110 / -0` | Azure built-in roles (+2 objects, +110 atoms) |
| GCP | `+109` | `+0 / ~41 / -0` | `+169 / -60` | GCP predefined roles (~41 changed, +169 atoms, -60 atoms) |
| GitHub | `0` | `+0 / ~2 / -0` | `+0 / -0` | GitHub fine-grained PAT permissions (~2 changed) |

## Dataset overview

| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | --- | ---: | ---: | ---: | --- |
| AWS managed policies | AWS | `1,536` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/aws-managed-policies.json) · [diff](../data/diffs/2026-07-15/aws-managed-policies.json) · [reverse index](../data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | Azure | `504` | `+2 / ~0 / -0` | `+110 / -0` | [snapshot](../data/latest/azure-built-in-roles.json) · [diff](../data/diffs/2026-07-15/azure-built-in-roles.json) · [reverse index](../data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | GCP | `2,362` | `+0 / ~41 / -0` | `+169 / -60` | [snapshot](../data/latest/gcp-predefined-roles.json) · [diff](../data/diffs/2026-07-15/gcp-predefined-roles.json) · [reverse index](../data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | GitHub | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-actions-default-workflow-settings.json) · [diff](../data/diffs/2026-07-15/github-actions-default-workflow-settings.json) · [reverse index](../data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | GitHub | `73` | `+0 / ~2 / -0` | `+0 / -0` | [snapshot](../data/latest/github-fgpat-permissions.json) · [diff](../data/diffs/2026-07-15/github-fgpat-permissions.json) · [reverse index](../data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | GitHub | `17` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-token-permissions.json) · [diff](../data/diffs/2026-07-15/github-token-permissions.json) · [reverse index](../data/reverse-index/github-token-permissions.json) |

## Platform pages

- [AWS](platforms/aws.md)
- [Azure](platforms/azure.md)
- [GCP](platforms/gcp.md)
- [GitHub](platforms/github.md)
