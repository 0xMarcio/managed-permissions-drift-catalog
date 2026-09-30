# Managed Permissions Drift Catalog

- Refreshed: September 30, 2026 · [daily report](daily/2026-09-30.md)
- Leading platform: `GCP` (`+314` net score)
- Driver: `GCP predefined roles` (+5 objects, ~67 changed, -6 removed, +367 atoms, -53 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+6` | `+0 / ~3 / -0` | `+6 / -0` | AWS managed policies (~3 changed, +6 atoms) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `+314` | `+5 / ~67 / -6` | `+367 / -53` | GCP predefined roles (+5 objects, ~67 changed, -6 removed, +367 atoms, -53 atoms) |
| GitHub | `+5` | `+2 / ~1 / -0` | `+2 / -0` | GitHub fine-grained PAT permissions (+2 objects, ~1 changed, +2 atoms) |

## Dataset overview

| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | --- | ---: | ---: | ---: | --- |
| AWS managed policies | AWS | `1,598` | `+0 / ~3 / -0` | `+6 / -0` | [snapshot](../data/latest/aws-managed-policies.json) · [diff](../data/diffs/2026-09-30/aws-managed-policies.json) · [reverse index](../data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | Azure | `504` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/azure-built-in-roles.json) · [diff](../data/diffs/2026-09-30/azure-built-in-roles.json) · [reverse index](../data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | GCP | `2,386` | `+5 / ~67 / -6` | `+367 / -53` | [snapshot](../data/latest/gcp-predefined-roles.json) · [diff](../data/diffs/2026-09-30/gcp-predefined-roles.json) · [reverse index](../data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | GitHub | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-actions-default-workflow-settings.json) · [diff](../data/diffs/2026-09-30/github-actions-default-workflow-settings.json) · [reverse index](../data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | GitHub | `76` | `+2 / ~1 / -0` | `+2 / -0` | [snapshot](../data/latest/github-fgpat-permissions.json) · [diff](../data/diffs/2026-09-30/github-fgpat-permissions.json) · [reverse index](../data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | GitHub | `16` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-token-permissions.json) · [diff](../data/diffs/2026-09-30/github-token-permissions.json) · [reverse index](../data/reverse-index/github-token-permissions.json) |

## Platform pages

- [AWS](platforms/aws.md)
- [Azure](platforms/azure.md)
- [GCP](platforms/gcp.md)
- [GitHub](platforms/github.md)
