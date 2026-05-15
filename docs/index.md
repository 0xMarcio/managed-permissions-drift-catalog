# Managed Permissions Drift Catalog

- Refreshed: May 15, 2026 · [daily report](daily/2026-05-15.md)
- Leading platform: `AWS` (`+20` net score)
- Driver: `AWS managed policies` (~5 changed, +21 atoms, -1 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+20` | `+0 / ~5 / -0` | `+21 / -1` | AWS managed policies (~5 changed, +21 atoms, -1 atoms) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `0` | `+0 / ~0 / -0` | `+0 / -0` | GCP predefined roles (no drift) |
| GitHub | `0` | `+0 / ~0 / -0` | `+0 / -0` | GitHub Actions default workflow settings (no drift) |

## Dataset overview

| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | --- | ---: | ---: | ---: | --- |
| AWS managed policies | AWS | `1,504` | `+0 / ~5 / -0` | `+21 / -1` | [snapshot](../data/latest/aws-managed-policies.json) · [diff](../data/diffs/2026-05-15/aws-managed-policies.json) · [reverse index](../data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | Azure | `498` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/azure-built-in-roles.json) · [diff](../data/diffs/2026-05-15/azure-built-in-roles.json) · [reverse index](../data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | GCP | `2,309` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/gcp-predefined-roles.json) · [diff](../data/diffs/2026-05-15/gcp-predefined-roles.json) · [reverse index](../data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | GitHub | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-actions-default-workflow-settings.json) · [diff](../data/diffs/2026-05-15/github-actions-default-workflow-settings.json) · [reverse index](../data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | GitHub | `71` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-fgpat-permissions.json) · [diff](../data/diffs/2026-05-15/github-fgpat-permissions.json) · [reverse index](../data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | GitHub | `17` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-token-permissions.json) · [diff](../data/diffs/2026-05-15/github-token-permissions.json) · [reverse index](../data/reverse-index/github-token-permissions.json) |

## Platform pages

- [AWS](platforms/aws.md)
- [Azure](platforms/azure.md)
- [GCP](platforms/gcp.md)
- [GitHub](platforms/github.md)
