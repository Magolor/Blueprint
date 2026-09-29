---
name: design-philosophy-state
description: Read before you define state isolation, capabilities, and failure behavior.
---

# Explicit state and honest behavior

## Summary

Name the writable owner and expose execution truth. Keep definitions, live instances, caches, and inspection snapshots distinct.

## Principle

Name the owner of mutable state, resources, and persistence. Distinguish durable definitions from live instances and caches. Return detached values or snapshots where the contract promises isolation; inspection projections must not become another writable authority.

Describe what execution actually supports and performs. Distinguish native work, fallback, and unsupported paths when these affect the caller. Advertised capabilities are not proof of a successful execution route. Make errors and recovery observable. Do not hide unfinished behavior behind silent fallback or imply that an accepted design has shipped.

## Pattern and Anti-pattern

These are illustrative pseudocode, not a required API or package layout.

```text
Pattern:      snapshot = store.inspect(); edit(snapshot) leaves store unchanged
Anti-pattern: snapshot = store.inspect(); edit(snapshot) silently mutates store
```

When inspection promises isolation, return detached values and keep writes with their declared owner.

```text
Pattern:      execute(request) -> unsupported error with supported alternatives
Anti-pattern: execute(request) -> success after silently skipping unsupported work
```

Expose failure and recovery. Disclose a fallback when it changes caller-visible behavior; a capability label alone proves no execution route.
