---
name: solid
description: Review Python responsibility, extension, substitution, interface, and dependency boundaries.
---

# SOLID boundaries

## Summary

Use SOLID to check boundaries. Do not add procedural overhead merely to claim compliance. Classes, modules, and packages should follow these principles:

## Required principle pages

Read all five pages when designing or reviewing object boundaries. Each principle has its own AgentHeaven-style member-method patterns and anti-patterns:

- [SRP: single responsibility](solid/srp.md)
- [OCP: open/closed](solid/ocp.md)
- [LSP: Liskov substitution](solid/lsp.md)
- [ISP: interface segregation](solid/isp.md)
- [DIP: dependency inversion](solid/dip.md)

Keep the user's mental model small through domain objects and their methods. Use SOLID to separate internal responsibilities without making users assemble them.

## Principle

- **SRP** (single responsibility): one reason to change.
- **OCP** (open/closed): stable extension APIs.
- **LSP** (Liskov substitution): substitutable subclasses.
- **ISP** (interface segregation): minimal role-specific interfaces.
- **DIP** (dependency inversion): abstractions before concrete provider details.

## Do

- **SRP (Single Responsibility):** give each class or module one owner and one reason to change.
- **OCP (Open/Closed):** extend genuinely open families through registered implementations, strategies, or adapters. Use direct exhaustive branches for intentionally closed variants.
- **LSP (Liskov Substitution):** make every subclass honor the base contract for construction, lifecycle, errors, and return types. Represent differences as explicit capability flags or typed overrides.
- **ISP (Interface Segregation):** keep the base interface to required common behavior; split optional capabilities into subclass, protocol, adapter, or registry families.
- **DIP (Dependency Inversion):** make high-level flows depend on base classes, protocols, registries, and config. Concrete providers publish descriptors through the family registration contract and keep provider-specific metadata close to the provider; high-level policy does not import them merely to make them discoverable.

## Avoid

- Catch-all base classes or helper modules that mix lifecycle, parsing, storage, provider metadata, and query execution.
- `if provider == ...` / `if backend == ...` branches in orchestration paths when a registry or strategy API can own the variation.
- Subclasses that mutate caller-owned inputs, require hidden preconditions, return incompatible shapes, or silently ignore base-class guarantees.
- Interfaces that force every implementation to carry unused methods, no-op methods, or provider-specific arguments.
- High-level modules that import concrete driver, dialect, backend, or provider code just to choose behavior.

For an independently extensible capability vocabulary, also read [the capability comparison](../../../examples/code/capability.md).

