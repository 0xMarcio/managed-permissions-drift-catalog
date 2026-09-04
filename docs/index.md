# Managed Permissions Drift Catalog

- Refreshed: September 4, 2026 · [daily report](daily/2026-09-04.md)
- Leading platform: `AWS` (`+4` net score)
- Driver: `AWS managed policies` (~4 changed, +4 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+4` | `+0 / ~4 / -0` | `+4 / -0` | AWS managed policies (~4 changed, +4 atoms) |
| Azure | `0` | `+0 / ~3 / -0` | `+0 / -0` | Azure built-in roles (~3 changed) |
| GCP | `0` | `+0 / ~0 / -0` | `+0 / -0` | GCP predefined roles (no drift) |
| GitHub | `0` | `+0 / ~2 / -0` | `+0 / -0` | GitHub fine-grained PAT permissions (~2 changed) |

## Dataset overview

| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | --- | ---: | ---: | ---: | --- |
| AWS managed policies | AWS | `1,585` | `+0 / ~4 / -0` | `+4 / -0` | [snapshot](../data/latest/aws-managed-policies.json) · [diff](../data/diffs/2026-09-04/aws-managed-policies.json) · [reverse index](../data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | Azure | `504` | `+0 / ~3 / -0` | `+0 / -0` | [snapshot](../data/latest/azure-built-in-roles.json) · [diff](../data/diffs/2026-09-04/azure-built-in-roles.json) · [reverse index](../data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | GCP | `2,374` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/gcp-predefined-roles.json) · [diff](../data/diffs/2026-09-04/gcp-predefined-roles.json) · [reverse index](../data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | GitHub | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-actions-default-workflow-settings.json) · [diff](../data/diffs/2026-09-04/github-actions-default-workflow-settings.json) · [reverse index](../data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | GitHub | `73` | `+0 / ~2 / -0` | `+0 / -0` | [snapshot](../data/latest/github-fgpat-permissions.json) · [diff](../data/diffs/2026-09-04/github-fgpat-permissions.json) · [reverse index](../data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | GitHub | `16` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-token-permissions.json) · [diff](../data/diffs/2026-09-04/github-token-permissions.json) · [reverse index](../data/reverse-index/github-token-permissions.json) |

## Platform pages

- [AWS](platforms/aws.md)
- [Azure](platforms/azure.md)
- [GCP](platforms/gcp.md)
- [GitHub](platforms/github.md)
