---
id: solid
title: SOLID boundaries
blocking: true
description: Review Python responsibility, extension, substitution, interface, and dependency boundaries.
---

# SOLID boundaries

## Core rule

Use SOLID to check boundaries. Do not add procedural overhead merely to claim compliance. Classes, modules, and packages should follow these principles:

- **SRP** (single responsibility): one reason to change.
- **OCP** (open/closed): stable extension APIs.
- **LSP** (Liskov substitution): substitutable subclasses.
- **ISP** (interface segregation): minimal role-specific interfaces.
- **DIP** (dependency inversion): abstractions before concrete provider details.

## Do

- **SRP (Single Responsibility):** give each class or module one owner and one reason to change.
- **OCP (Open/Closed):** add behavior through registered implementations, strategy objects, adapters, or class-owned metadata instead of editing central conditionals.
- **LSP (Liskov Substitution):** make every subclass honor the base contract for construction, lifecycle, errors, and return types. Represent differences as explicit capability flags or typed overrides.
- **ISP (Interface Segregation):** keep the base interface to required common behavior; split optional capabilities into subclass, protocol, adapter, or registry families.
- **DIP (Dependency Inversion):** make high-level flows depend on base classes, protocols, registries, and config. Concrete providers publish descriptors through the family registration contract and keep provider-specific metadata close to the provider; high-level policy does not import them merely to make them discoverable.

## Avoid

- Catch-all base classes or helper modules that mix lifecycle, parsing, storage, provider metadata, and query execution.
- `if provider == ...` / `if backend == ...` branches in orchestration paths when a registry or strategy API can own the variation.
- Subclasses that mutate caller-owned inputs, require hidden preconditions, return incompatible shapes, or silently ignore base-class guarantees.
- Interfaces that force every implementation to carry unused methods, no-op methods, or provider-specific arguments.
- High-level modules that import concrete driver, dialect, backend, or provider code just to choose behavior.

Use [examples](solid/example.md) when a boundary tradeoff needs a concrete comparison.

For capability fields that proliferate across providers, use [the capability comparison](../../../examples/code/capability.md).
