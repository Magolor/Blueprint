---
name: gui-techstack
description: Read before choosing a GUI framework, host, or package boundary.
---

# GUI tech stack

## Summary

Keep the repository’s coherent GUI stack and expose domain behavior through thin interface adapters.

## Stack and boundaries

Use the repository's existing framework, runtime, component system, and package manager. This visual guide is framework-neutral and does not require a new framework or workspace.

For a new host, service boundary, or separate GUI build, read [interface roles and layouts](../../rules/project/interfaces.md). Select physical packages only for actual runtime, dependency, consumer, release, or artifact boundaries. Keep UI and transport adapters over the public application/SDK contract.

For a TypeScript toolchain decision, use [environment](../../rules/code/typescript/env.md). Preserve Python services and their native packaging when already coherent. A mixed-language boundary needs an explicit serialized protocol.

Reuse canonical components and tokens. Integrate third-party widgets into their semantic, accessibility, state, and visual contracts. Transfers move hierarchy and roles into the target system rather than copying a source project's stack or raw markup.
