# Managed Permissions Drift Catalog

- Refreshed: October 14, 2026 · [daily report](daily/2026-10-14.md)
- Leading platform: `AWS` (`+48` net score)
- Driver: `AWS managed policies` (+2 objects, ~1 changed, +48 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+48` | `+2 / ~1 / -0` | `+48 / -0` | AWS managed policies (+2 objects, ~1 changed, +48 atoms) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `0` | `+0 / ~0 / -0` | `+0 / -0` | GCP predefined roles (no drift) |
| GitHub | `+2` | `+1 / ~0 / -0` | `+1 / -0` | GitHub GITHUB_TOKEN permissions (+1 objects, +1 atoms) |

## Dataset overview

| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | --- | ---: | ---: | ---: | --- |
| AWS managed policies | AWS | `1,603` | `+2 / ~1 / -0` | `+48 / -0` | [snapshot](../data/latest/aws-managed-policies.json) · [diff](../data/diffs/2026-10-14/aws-managed-policies.json) · [reverse index](../data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | Azure | `504` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/azure-built-in-roles.json) · [diff](../data/diffs/2026-10-14/azure-built-in-roles.json) · [reverse index](../data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | GCP | `2,388` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/gcp-predefined-roles.json) · [diff](../data/diffs/2026-10-14/gcp-predefined-roles.json) · [reverse index](../data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | GitHub | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-actions-default-workflow-settings.json) · [diff](../data/diffs/2026-10-14/github-actions-default-workflow-settings.json) · [reverse index](../data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | GitHub | `76` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-fgpat-permissions.json) · [diff](../data/diffs/2026-10-14/github-fgpat-permissions.json) · [reverse index](../data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | GitHub | `17` | `+1 / ~0 / -0` | `+1 / -0` | [snapshot](../data/latest/github-token-permissions.json) · [diff](../data/diffs/2026-10-14/github-token-permissions.json) · [reverse index](../data/reverse-index/github-token-permissions.json) |

## Platform pages

- [AWS](platforms/aws.md)
- [Azure](platforms/azure.md)
- [GCP](platforms/gcp.md)
- [GitHub](platforms/github.md)
