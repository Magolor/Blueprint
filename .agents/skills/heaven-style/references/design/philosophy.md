---
id: design-philosophy
title: Design philosophy
blocking: true
description: Minimize public concepts and decouple internal ownership.
---

# Design philosophy

The core objective is a minimal mental model for users: as few public concepts and classes as possible, with cohesive domain behavior on the objects users already know. Internal decomposition serves this objective. It must not make users assemble the implementation themselves. Apply this philosophy with the complete language and project rules before code or architecture work.

## Small public OOP surface

Start with one supported import and one short ordinary flow: construct or load the domain object, then call its operation. Prefer a method or classmethod on the existing owner over a new public function, factory, wrapper, flag, or DSL. Each added public concept must remove more user complexity than it introduces.

A class earns its place through domain meaning, behavior, invariants, identity, state, or lifecycle. Do not minimize the class count by merging unrelated responsibilities into one large object. Do not maximize OOP by wrapping every value or stateless algorithm in a class. Use native protocols and direct functions for independent transforms where the language expects them. Public OOP cohesion and private functional implementation can coexist.

Separate ordinary users from extension authors. Users follow domain methods; extension authors receive stable, documented contracts. Neither audience should navigate private registries or helper factories to complete its normal task.

## Decoupled layers with one owner

Organize by responsibility and reason to change. A small public facade may delegate to focused private services. Services call the responsible service directly; they must not route internal work back through the public facade. Add a layer only when it isolates a real policy, lifecycle, or independent axis of change.

Keep logical vocabulary and declarative specifications independent of physical I/O. When compilation is needed, pure compilers translate logical requests into neutral execution values. Provider adapters own physical execution. Orchestration owns coordination and result composition. GUI, CLI, HTTP, and tool adapters expose the same domain behavior without copying its policy.

Maintain one authority for each registry, configuration policy, routing decision, and lifecycle. Reuse repository infrastructure instead of introducing a second planner, configuration system, or registry. Generic utilities must not depend on application or provider policy. These are responsibility boundaries, not a mandatory directory tree or a requirement to add a compiler, provider, or registry to a small package.

## Explicit composition and extension

Pass the owning context or dependencies explicitly when identity or lifecycle matters. An explicitly supplied owner must not silently fall back to global state. Keep construction, definition, registration, activation, execution, and shutdown distinct where they have different effects. Imports must not perform hidden I/O or activate optional implementations. Metadata inspection must not import or activate an implementation merely to describe it.

For genuinely open families, add implementations through the declared registration and selection contract. Bundled and external implementations use the same promised validation and lifecycle. Do not require central provider-name branches or package scans. Handle closed variants exhaustively; an enum does not need a plugin system.

Keep independently extensible implementations cohesive. Add internal pieces for independent variation, not to expose every internal role as another user-facing class.

## Explicit state and honest behavior

Name the owner of mutable state, resources, and persistence. Distinguish durable definitions from live instances and caches. Return detached values or snapshots where the contract promises isolation; inspection projections must not become another writable authority.

Describe what execution actually supports and performs. Distinguish native work, fallback, and unsupported paths when these affect the caller. Advertised capabilities are not proof of a successful execution route. Make errors and recovery observable. Do not hide unfinished behavior behind silent fallback or imply that an accepted design has shipped.

## Review the user cost

For each structural change, verify the shortest user flow, the owner of each policy, dependency direction, extension parity where promised, and lifecycle effects. Compare the number of concepts the caller must understand before and after. Require a concrete reason for added public surface.

Pair mandatory boundaries with focused behavioral tests, import checks, or concrete review criteria. Record current behavior, intended changes, and explicit non-goals in their canonical documentation owners. Keep language-specific [API and SOLID rules](../rules/overview.md), [extension contracts](../rules/project/extension.md), and [interface boundaries](../rules/project/interfaces.md) authoritative for their detailed mechanics.
