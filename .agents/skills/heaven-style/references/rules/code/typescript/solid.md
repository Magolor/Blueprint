---
id: ts-architecture
title: TypeScript architecture
blocking: true
description: Review TypeScript SOLID, dependency direction, extension, and composition boundaries.
---

# TypeScript SOLID boundaries

Use structural interfaces and composition to test actual boundaries. Repository policy and compatibility contracts win. Choose the smallest testable design for verified change pressure; do not port Python mechanics or add layers to claim compliance.

| Principle | TypeScript contract |
| --- | --- |
| SRP | Group modules/classes by reason to change. Objects own state, identity, or lifecycle; stateless transforms use typed functions. |
| OCP | Register genuinely open implementations. Exhaust closed unions. Use one public contract for bundled and independent extensions when promised. |
| LSP | Implementations preserve construction, lifecycle, errors, return shapes, and caller ownership. No hidden preconditions or ignored guarantees. |
| ISP | Keep required interfaces minimal. Separate optional capabilities and prove them before use; no no-op or always-unsupported methods. |
| DIP | Domain policy and orchestration depend on stable contracts. Provider details depend inward; policy does not import concrete providers for selection. |

A package may import its own or a lower/stabler layer, never a higher composition/UI layer. Cross-layer/package and initialization-order cycles are blockers. An intrinsic local cycle requires an owner and a fitness test; real package graphs need a dependency check.

Constructors validate and store identity/configuration. Keep I/O and registration explicit through `create`, `connect`, or `start`, with awaited `close`/`dispose`. `static async create(config)` is appropriate when the public result is an already-ready object and failure stays explicit in the promise.

Entry modules stay side-effect-free. Optional SDKs load within the selected adapter's creation/connect path and use explicit package subpaths. Missing dependencies fail actionably. Follow [optional integration checks](files/optional.md) so evaluation errors are not mislabeled as missing packages.

Read [extension boundaries](solid/extend.md) for open/closed sets, capability facts, and role interfaces; [composition](solid/compose.md) for specs, execution, registries, and durable/runtime authority.

## Fitness checks

For standing boundary promises, use the smallest relevant check: shared implementation contracts, late registration without router edits, alias/canonical IDs, truthful capabilities/fallbacks, optional-free root imports, registry scope/duplicates, packed consumers, or dependency graphs. Do not build matrices for imagined implementations.
