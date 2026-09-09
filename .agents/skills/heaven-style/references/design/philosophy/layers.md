---
name: design-philosophy-layers
description: Read before you assign policy owners and dependency boundaries.
---

# Decoupled layers with one owner

## Summary

Give each policy one owner and separate responsibilities that change independently. A small public facade can hide focused internal services.

## Principle

Organize by responsibility and reason to change. A small public facade may delegate to focused private services. Services call the responsible service directly; they must not route internal work back through the public facade. Add a layer only when it isolates a real policy, lifecycle, or independent axis of change.

Keep logical vocabulary and declarative specifications independent of physical I/O. When compilation is needed, pure compilers translate logical requests into neutral execution values. Provider adapters own physical execution. Orchestration owns coordination and result composition. GUI, CLI, HTTP, and tool adapters expose the same domain behavior without copying its policy.

Maintain one authority for each registry, configuration policy, routing decision, and lifecycle. Reuse repository infrastructure instead of introducing a second planner, configuration system, or registry. Generic utilities must not depend on application or provider policy. These are responsibility boundaries, not a mandatory directory tree or a requirement to add a compiler, provider, or registry to a small package.

## Pattern and Anti-pattern

These are illustrative pseudocode, not a required API or package layout.

```text
Pattern:      CLI -> project.export -> export service -> storage adapter
Anti-pattern: CLI -> its own export policy
              HTTP -> another copy of export policy
```

Adapters translate inputs and outputs; the domain owner supplies shared behavior.

```text
Pattern:      export service -> storage service
Anti-pattern: export service -> public facade -> storage service
```

Internal services call the responsible service directly. Routing back through the facade obscures ownership.
