# managed-permissions-drift-catalog

Daily drift catalog for AWS managed policies, Azure built-in roles, GCP predefined roles, GitHub fine-grained PAT permissions, and GitHub Actions token/settings schemas.

## Latest drift

- Refreshed at: `2026-04-21T04:23:56Z` · [daily report](docs/daily/2026-04-21.md)
- Leading platform: `GCP` (`+2,649` net score)
- Driver: `GCP predefined roles` (+51 objects, ~171 changed, -2 removed, +2,697 atoms, -48 atoms)

## Platform overview

| Platform | Net score | Objects (+/~/-) | Atoms (+/-) | Main driver |
| --- | ---: | ---: | ---: | --- |
| AWS | `0` | `+0 / ~0 / -0` | `+0 / -0` | AWS managed policies (no drift) |
| Azure | `0` | `+0 / ~0 / -0` | `+0 / -0` | Azure built-in roles (no drift) |
| GCP | `+2,649` | `+51 / ~171 / -2` | `+2,697 / -48` | GCP predefined roles (+51 objects, ~171 changed, -2 removed, +2,697 atoms, -48 atoms) |
| GitHub | `0` | `+0 / ~0 / -0` | `+0 / -0` | GitHub Actions default workflow settings (no drift) |

## Dataset overview

| Dataset | Inventory | Objects (+/~/-) | Atoms (+/-) | Files |
| --- | ---: | ---: | ---: | --- |
| AWS managed policies | `1,498` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-04-21/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json) |
| Azure built-in roles | `498` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-04-21/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json) |
| GCP predefined roles | `2,293` | `+51 / ~171 / -2` | `+2,697 / -48` | [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-04-21/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json) |
| GitHub Actions default workflow settings | `6` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-04-21/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json) |
| GitHub fine-grained PAT permissions | `66` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-04-21/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json) |
| GitHub GITHUB_TOKEN permissions | `15` | `+0 / ~0 / -0` | `+0 / -0` | [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-04-21/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json) |

## Latest dataset movement

### AWS managed policies

- Inventory: `1,498` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/aws-managed-policies.json) · [diff](data/diffs/2026-04-21/aws-managed-policies.json) · [reverse index](data/reverse-index/aws-managed-policies.json)

### Azure built-in roles

- Inventory: `498` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/azure-built-in-roles.json) · [diff](data/diffs/2026-04-21/azure-built-in-roles.json) · [reverse index](data/reverse-index/azure-built-in-roles.json)

### GCP predefined roles

- Inventory: `2,293` objects.
- Today: +51 objects, ~171 changed, -2 removed, +2,697 atoms, -48 atoms.
- Biggest additions: `Aiplatform Editor` (+432 atoms), `Gemini Cloud Assist Admin Beta` (+116 atoms), `Gemini Cloud Assist Editor Beta` (+111 atoms).
- Biggest changes: `Support User` (+79), `DLP Organization Data Profiles Driver` (+68), `DLP Project Data Profiles Driver` (+68).
- Biggest removals: `Developerconnect Editor Beta` (-44 atoms), `MCP Admin` (-3 atoms).
- Files: [snapshot](data/latest/gcp-predefined-roles.json) · [diff](data/diffs/2026-04-21/gcp-predefined-roles.json) · [reverse index](data/reverse-index/gcp-predefined-roles.json)

### GitHub fine-grained PAT permissions

- Inventory: `66` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-fgpat-permissions.json) · [diff](data/diffs/2026-04-21/github-fgpat-permissions.json) · [reverse index](data/reverse-index/github-fgpat-permissions.json)

### GitHub GITHUB_TOKEN permissions

- Inventory: `15` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-token-permissions.json) · [diff](data/diffs/2026-04-21/github-token-permissions.json) · [reverse index](data/reverse-index/github-token-permissions.json)

### GitHub Actions default workflow settings

- Inventory: `6` objects.
- Today: No drift detected.
- Files: [snapshot](data/latest/github-actions-default-workflow-settings.json) · [diff](data/diffs/2026-04-21/github-actions-default-workflow-settings.json) · [reverse index](data/reverse-index/github-actions-default-workflow-settings.json)
