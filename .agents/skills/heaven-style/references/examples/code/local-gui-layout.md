---
id: example-local-gui-layout
title: Local GUI layout
enabled: true
order: 20
keywords: [local GUI, app root, desktop, TypeScript UI, application boundary, REST OpenAPI, package topology, source plane, artifact plane]
description: Read when placing a GUI beside a service, choosing a cohesive package versus workspace packages, or wiring UI, host, transport, application, and domain dependencies.
---

# Local GUI Layout

This example demonstrates roles and dependency direction. It does not prescribe exact folder names, a desktop host, or one package topology.

## Cohesive repository

Start here when the service, SDK, and interfaces share ownership and release cadence:

```text
repo/
  src/
    index.ts                 # supported SDK
    domain/                  # core behavior
    application/             # transport-neutral use cases
    adapters/http/           # optional HTTP/OpenAPI adapter
    interfaces/cli/          # optional thin CLI
  apps/desktop/              # only when UI/host tooling is distinct
    ui/                      # TypeScript presentation
    host/                    # browser/WebView/native host + packaging
```

Python may own the service package with the same logical roles while a TypeScript UI remains under the app root. Match the repository's language and naming conventions; do not mirror folders merely for symmetry.

## Earned workspace

Split packages only when consumers, runtime isolation, dependencies, compatibility, or artifact checks justify them:

```text
repo/
  packages/
    core/                    # embeddable domain/public SDK
    application/             # portable operations/client contract
    server/                  # service implementation + protocol adapters
    testkit/                 # optional external conformance support
  apps/
    server/                  # listener/process composition
    cli/                     # command composition
    desktop/                 # UI + host distribution
```

This shape is useful for a published core, a separately consumed application client, or a service with dependencies that must not leak to embedders. It is needless overhead when everything changes and ships together.

## Dependency arrows

```text
desktop UI ──client/protocol──▶ application use cases ──▶ domain/core
desktop host ──launch/teardown──▶ server or in-process composition
CLI / MCP / TUI ───────────────▶ application use cases or client

domain/core -/-> application, transports, UI, terminal, or host
application -/-> concrete UI or desktop host
```

The UI may call an in-process client or a remote protocol. HTTP/OpenAPI is appropriate when it is a real interoperability or process boundary; it is not required between modules in one process.

## Host choice

A browser, system WebView, established desktop framework, or native host can all be correct. Decide from distribution, security, accessibility, update policy, platform coverage, binary size, native integration, and team capability. Keep the host thin: it owns window/process lifecycle and packaging, not a second domain model.

## Artifact checks

- Source tests verify application behavior through repository mappings.
- Build checks verify emitted UI and server artifacts.
- Packed-consumer tests verify public package exports and declarations.
- A distribution smoke verifies the actual desktop/server entry path and teardown.

Source-plane success does not prove the artifact plane. Add only the checks corresponding to artifacts the repository actually publishes.

## Smells

- UI routes query databases or choose providers directly.
- A host owns business rules because it was convenient during prototyping.
- Every conceptual layer became a package without an independent consumer.
- Workspace aliases or sibling source imports are the only evidence that public packages work.
- A second language reimplements core behavior only to match folder diagrams.
- The repository adopts a desktop runtime because a style guide named it, without product evidence.

## Related rules

- [Service interface architecture](../../rules/project/interfaces.md)
- [TypeScript modules and package boundaries](../../rules/code/typescript/modules.md)
- [TypeScript environment and toolchain](../../rules/code/typescript/environment.md)
- [Tests and examples](../../rules/project/test.md)
- [GUI style](../../design/gui-style.md)
