# Managed Permissions Drift Catalog

- Refreshed: November 19, 2026 · [daily report](daily/2026-11-19.md)
- Leading platform: `GCP` (`+687` net score)
- Driver: `GCP predefined roles` (+11 objects, ~80 changed, +737 atoms, -50 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `+44` | `+5 / ~12 / -0` | `+90 / -46` | AWS managed policies (+5 objects, ~12 changed, +90 atoms, -46 atoms) |
| Azure | `+34` | `+1 / ~0 / -0` | `+34 / -0` | Azure built-in roles (+1 objects, +34 atoms) |
| GCP | `+687` | `+11 / ~80 / -0` | `+737 / -50` | GCP predefined roles (+11 objects, ~80 changed, +737 atoms, -50 atoms) |
| GitHub | `0` | `+0 / ~0 / -0` | `+0 / -0` | GitHub Actions default workflow settings (no drift) |

## Dataset overview

| Dataset | Platform | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | --- | ---: | ---: | ---: | --- |
| AWS managed policies | AWS | `1,632` | `+5 / ~12 / -0` | `+90 / -46` | [snapshot](../data/latest/aws-managed-policies.json) · [diff](../data/diffs/2026-11-19/aws-managed-policies.json) · [reverse index](../data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | Azure | `507` | `+1 / ~0 / -0` | `+34 / -0` | [snapshot](../data/latest/azure-built-in-roles.json) · [diff](../data/diffs/2026-11-19/azure-built-in-roles.json) · [reverse index](../data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | GCP | `2,422` | `+11 / ~80 / -0` | `+737 / -50` | [snapshot](../data/latest/gcp-predefined-roles.json) · [diff](../data/diffs/2026-11-19/gcp-predefined-roles.json) · [reverse index](../data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | GitHub | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-actions-default-workflow-settings.json) · [diff](../data/diffs/2026-11-19/github-actions-default-workflow-settings.json) · [reverse index](../data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | GitHub | `78` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-fgpat-permissions.json) · [diff](../data/diffs/2026-11-19/github-fgpat-permissions.json) · [reverse index](../data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | GitHub | `17` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](../data/latest/github-token-permissions.json) · [diff](../data/diffs/2026-11-19/github-token-permissions.json) · [reverse index](../data/reverse-index/github-token-permissions.json) |

## Platform pages

- [AWS](platforms/aws.md)
- [Azure](platforms/azure.md)
- [GCP](platforms/gcp.md)
- [GitHub](platforms/github.md)
