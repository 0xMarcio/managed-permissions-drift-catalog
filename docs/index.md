# Managed Permissions Drift Catalog

- Refreshed: July 1, 2026 · [daily report](daily/2026-07-01.md)
- Leading platform: `GCP` (`+195` net score)
- Driver: `GCP predefined roles` (+6 objects, ~55 changed, +196 atoms, -1 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+25` | `+2 / ~4 / -0` | `+25 / -0` | AWS managed policies (+2 objects, ~4 changed, +25 atoms) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `+195` | `+6 / ~55 / -0` | `+196 / -1` | GCP predefined roles (+6 objects, ~55 changed, +196 atoms, -1 atoms) |
| GitHub | `0` | `+0 / ~0 / -0` | `+0 / -0` | GitHub Actions default workflow settings (no drift) |

## Dataset overview

| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | --- | ---: | ---: | ---: | --- |
| AWS managed policies | AWS | `1,526` | `+2 / ~4 / -0` | `+25 / -0` | [snapshot](../data/latest/aws-managed-policies.json) · [diff](../data/diffs/2026-07-01/aws-managed-policies.json) · [reverse index](../data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | Azure | `501` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/azure-built-in-roles.json) · [diff](../data/diffs/2026-07-01/azure-built-in-roles.json) · [reverse index](../data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | GCP | `2,349` | `+6 / ~55 / -0` | `+196 / -1` | [snapshot](../data/latest/gcp-predefined-roles.json) · [diff](../data/diffs/2026-07-01/gcp-predefined-roles.json) · [reverse index](../data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | GitHub | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-actions-default-workflow-settings.json) · [diff](../data/diffs/2026-07-01/github-actions-default-workflow-settings.json) · [reverse index](../data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | GitHub | `73` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-fgpat-permissions.json) · [diff](../data/diffs/2026-07-01/github-fgpat-permissions.json) · [reverse index](../data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | GitHub | `17` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-token-permissions.json) · [diff](../data/diffs/2026-07-01/github-token-permissions.json) · [reverse index](../data/reverse-index/github-token-permissions.json) |

## Platform pages

- [AWS](platforms/aws.md)
- [Azure](platforms/azure.md)
- [GCP](platforms/gcp.md)
- [GitHub](platforms/github.md)
