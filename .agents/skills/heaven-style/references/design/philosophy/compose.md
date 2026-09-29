---
name: design-philosophy-compose
description: Read before you wire dependencies, lifecycle, and extension families.
---

# Explicit composition and extension

## Summary

Make ownership and lifecycle explicit. Extend genuinely open families through one declared contract and handle closed variants directly.

## Principle

Pass the owning context or dependencies explicitly when identity or lifecycle matters. An explicitly supplied owner must not silently fall back to global state. Keep construction, definition, registration, activation, execution, and shutdown distinct where they have different effects. Imports must not perform hidden I/O or activate optional implementations. Metadata inspection must not import or activate an implementation merely to describe it.

For genuinely open families, add implementations through the declared registration and selection contract. Bundled and external implementations use the same promised validation and lifecycle. Do not require central provider-name branches or package scans. Handle closed variants exhaustively; an enum does not need a plugin system.

Keep independently extensible implementations cohesive. Add internal pieces for independent variation, not to expose every internal role as another user-facing class.

## Pattern and Anti-pattern

These are illustrative pseudocode, not a required API or package layout.

```text
Pattern:      Store(context = suppliedContext)
Anti-pattern: Store(context = suppliedContext or globalContext)
```

Validate an explicitly supplied owner. Do not silently replace an invalid or unavailable one with global state.

```text
Pattern:      register(adapter, contract); select(adapterId)
Anti-pattern: scanPackages(); if providerName == "special": bypassValidation()
```

For an open family, bundled and external adapters follow the same promised contract. A closed set can use exhaustive branches without a registry.
