---
name: ts-files-check
description: Read before checking TypeScript generated code or module cycles.
---

# TypeScript module checks

## Summary

Keep generated and vendored ownership explicit and verify consequential dependency cycles.

## Generated and vendored code

- Keep generated output under a clearly owned path. Regenerate it through one command. Never hand-edit it.
- Provide a check mode that fails when committed generated output is stale.
- Keep generated output out of lint/typecheck only when the generator is the source of truth and the built consumer still validates it.
- Vendored code preserves upstream style and lives behind a manifest/sync procedure. Local modifications are logged and rechecked during upgrades.
- Do not copy a vendor's internal module layout into first-party code merely for symmetry.

## Cycles and architecture gates

- Cross-layer/package runtime cycles and cycles whose behavior depends on initialization order are blocking findings.
- A local runtime cycle is acceptable only when its owner documents why it is intrinsic, the runtime path is deterministic, and a focused fitness test proves initialization/import behavior. Otherwise break it; do not normalize cycles with broad lint exemptions.
- Type-only cycles still deserve review because they often reveal misplaced ownership, but they are not automatically defects.
- Multi-package repositories should check dependency constraints, unused exports/dependencies, and package manifests with a project-local gate.
- Owned config and script files must not fall outside every typecheck/lint graph. Give them a dedicated checked project or an explicit justified exception.
