# Managed Permissions Drift Catalog

- Refreshed: July 22, 2026 · [daily report](daily/2026-07-22.md)
- Leading platform: `GCP` (`+273` net score)
- Driver: `GCP predefined roles` (+2 objects, ~53 changed, +293 atoms, -20 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+147` | `+6 / ~4 / -0` | `+147 / -0` | AWS managed policies (+6 objects, ~4 changed, +147 atoms) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `+273` | `+2 / ~53 / -0` | `+293 / -20` | GCP predefined roles (+2 objects, ~53 changed, +293 atoms, -20 atoms) |
| GitHub | `0` | `+0 / ~0 / -0` | `+0 / -0` | GitHub Actions default workflow settings (no drift) |

## Dataset overview

| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | --- | ---: | ---: | ---: | --- |
| AWS managed policies | AWS | `1,547` | `+6 / ~4 / -0` | `+147 / -0` | [snapshot](../data/latest/aws-managed-policies.json) · [diff](../data/diffs/2026-07-22/aws-managed-policies.json) · [reverse index](../data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | Azure | `504` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/azure-built-in-roles.json) · [diff](../data/diffs/2026-07-22/azure-built-in-roles.json) · [reverse index](../data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | GCP | `2,364` | `+2 / ~53 / -0` | `+293 / -20` | [snapshot](../data/latest/gcp-predefined-roles.json) · [diff](../data/diffs/2026-07-22/gcp-predefined-roles.json) · [reverse index](../data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | GitHub | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-actions-default-workflow-settings.json) · [diff](../data/diffs/2026-07-22/github-actions-default-workflow-settings.json) · [reverse index](../data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | GitHub | `73` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-fgpat-permissions.json) · [diff](../data/diffs/2026-07-22/github-fgpat-permissions.json) · [reverse index](../data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | GitHub | `17` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-token-permissions.json) · [diff](../data/diffs/2026-07-22/github-token-permissions.json) · [reverse index](../data/reverse-index/github-token-permissions.json) |

## Platform pages

- [AWS](platforms/aws.md)
- [Azure](platforms/azure.md)
- [GCP](platforms/gcp.md)
- [GitHub](platforms/github.md)
