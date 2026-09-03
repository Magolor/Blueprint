---
id: interfaces
title: Service interface architecture
enabled: true
blocking: true
order: 460
category: project
keywords: [service architecture, TypeScript SDK, Python SDK, application boundary, transport adapter, REST, OpenAPI, async API, CLI, GUI, MCP, TUI, package boundary, desktop host]
description: Use when a package exposes an SDK, application service, API, CLI, GUI, MCP, TUI, dashboard, desktop app, or independently consumed transport.
---

# Service Interface Architecture

## Core rule

Name responsibilities before naming folders. When all roles exist, dependencies flow in this direction:

```text
CLI / GUI / MCP / TUI / automation
                |
                v
transport adapter or application client
                |
                v
transport-neutral application use cases
                |
                v
domain/core behavior
```

A language-native SDK may expose domain/core behavior directly for embedding. Interfaces that need shared orchestration call the application boundary instead of rebuilding policy in callbacks. HTTP, OpenAPI, JSON-RPC, MCP, terminal, browser, and desktop concerns remain adapters; core code never imports them.

These are logical roles, not mandatory package or directory names. A cohesive library may keep them in one package. Split packages only when a role earns independent consumption, runtime or dependency isolation, release compatibility, ownership, build tooling, or artifact verification.

## Apply when

- A package is embedded, deployed, or consumed through more than one interface.
- Code adds or redesigns an SDK, HTTP API, CLI, GUI, dashboard, MCP server, TUI, automation API, or desktop app.
- Validation, persistence, defaults, authorization, or use-case orchestration is duplicated across interfaces.
- A role may need an independently published package or process boundary.

## Role contracts

### Domain/core and SDK

- Keep domain rules, durable invariants, storage ports, and reusable behavior independent of transports and presentation.
- Expose the shortest supported language-native entry point. Prefer owning objects for identity, state, invariants, and lifecycle; use functions for stateless transforms.
- Keep HTTP request objects, terminal widgets, browser globals, parser types, and desktop-host values out of core signatures.
- Do not make an interface stack a prerequisite for importing the SDK.

### Application boundary

- Put cross-feature use cases, policy sequencing, transaction scope, and interface-neutral authorization checks here rather than in domain entities or route callbacks.
- Define typed request, result, error, pagination, event, cancellation, and idempotency semantics once when multiple callers share them.
- Validate untrusted input at the owning boundary, then pass admitted values inward.
- Keep methods testable without framework request/response objects.
- Separate process-local dependency injection from durable or wire contracts.

Call this role `application/`, `service/`, `use-cases/`, `api/`, or a repository-specific equivalent. Do not create an `api/` folder that only re-exports the SDK.

### Transport adapters and clients

- Translate transport values to application calls and translate results/errors back; do not own business policy.
- Define serialization per boundary. Storage, public JSON, wire messages, logs, and cache keys may share primitives but are not automatically the same contract.
- For HTTP/JSON services, publish or check an OpenAPI contract when clients or external consumers need one. Generate it from the same admitted request/result definitions when practical.
- Keep listener/process startup in a composition root, not an import side effect.
- For remote or I/O-heavy work, define concurrency, timeouts, cancellation, retry/idempotency, backpressure, and cleanup explicitly.
- Local callers may use an in-process application client; remote callers use a protocol client. Both paths should preserve operation and error semantics where the product promises parity.

### Interfaces and composition roots

- CLI, GUI, MCP, TUI, and automation surfaces own input collection, presentation, interface lifecycle, and composition only.
- Interface-only dependencies must not leak onto the core SDK import path.
- A new interface should normally add mappings over existing use cases, not a second implementation.
- Put an interface in the owning package when it shares that package's runtime, release, and toolchain. Put it under an app root when it has a distinct runtime, bundler, host, dependency set, or distribution artifact.

## Physical layouts

### Cohesive package

Use one package while the roles change and ship together:

```text
src/
  index.ts | __init__.py       # supported SDK facade
  domain/                      # business behavior and ports
  application/                 # transport-neutral use cases
  adapters/
    http/                      # optional protocol adapter/client
  interfaces/
    cli/                       # optional thin interface
    mcp/                       # optional thin interface
```

Names are illustrative. Feature-local folders are equally valid when they preserve the same dependency direction.

### Earned workspace packages

Use packages when the boundary has concrete pressure:

```text
packages/
  core/                        # embeddable domain/public SDK
  application/                 # portable application contract/client
  server/                      # service implementation + transports
  testkit/                     # only when external conformance needs it
apps/
  cli/                         # private composition root
  server/                      # process/listener root
  desktop/                     # distinct UI/host toolchain
```

Do not copy these names mechanically. A package must answer at least one of these questions:

- Who consumes it independently?
- Which runtime, dependency set, or security boundary does it isolate?
- Which compatibility or release contract does it own?
- Which clean packed-consumer or extraction check proves the boundary?

If the answers are “nobody” and “none,” keep a folder inside the cohesive owner.

## TypeScript and Python

TypeScript and Python are equal language-native surfaces. Use the repository's declared language and preserve coherent shipped behavior. For greenfield service work, TypeScript is a strong default when the runtime, browser, package, or future Node integration benefits from one type system; Python remains fully appropriate when its ecosystem and existing domain ownership are the better fit.

When both languages exist, avoid implementing the same core twice by default. Prefer one authoritative service/application contract with an idiomatic client in the other language, unless offline embedding or performance evidence genuinely requires two implementations. Cross-language parity belongs to protocol and behavior tests, not mirrored internal folder names.

## CLI contract

- Use one repository-declared parser/framework by default.
- Keep parser definitions and handlers feature-local, then compose them at one explicit entry point.
- Handlers accept parsed/validated values, call application use cases or a client, and render results.
- Keep exit codes, stdout/stderr ownership, cancellation, and signal-driven teardown explicit and tested.
- Test the built or packed command entry when it is published.

If a repository explicitly promises multiple CLI-framework backends, define one parser-neutral command model and compile it to those backends. That compatibility profile needs named consumers and parity tests; it is not a default for ordinary CLIs.

## GUI and desktop contract

- Prefer TypeScript for a new browser UI unless repository evidence favors another frontend language.
- Keep UI state/presentation separate from the application service and transport client.
- Place a distinct frontend/desktop toolchain under an app root such as `apps/desktop/` or the repository's convention. Package-local placement is fine when it truly shares package tooling and distribution.
- Choose browser delivery, a system WebView, an existing desktop framework, or another native host from distribution, security, accessibility, update, binary-size, platform, and team evidence. A thin system WebView is a good option for a local tool, not a universal mandate.
- A host owns window/process lifecycle, secure navigation/origin policy, application packaging, and teardown. It does not become a second domain implementation.
- Keep framework and host dependencies off the core SDK path.

See [local GUI layout](../../examples/code/local-gui-layout.md) for cohesive and workspace examples, and [GUI style](../../design/gui-style.md) for visual and interaction criteria.

## Other interface contracts

- **MCP:** map tools, resources, and prompts to application operations. Keep schemas generated from or checked against the same admitted contracts when practical.
- **TUI:** reuse application use cases or a client; terminal widgets do not bypass orchestration.
- **Automation/agents:** call a documented SDK or protocol contract and preserve stable machine-readable errors rather than scraping human CLI output.
- **REST/OpenAPI:** use it when HTTP clients and interoperability justify it; do not introduce HTTP merely to mediate two modules in one process.

## Avoid

- Interface callbacks that import storage/provider internals and reimplement policy.
- A separate business-logic implementation for every interface.
- An `api` module that only re-exports symbols while implying a service boundary.
- Framework request/response objects in application or domain signatures.
- Process-global request state or listener startup during import.
- Package-per-noun layouts without independent pressure.
- Cross-package source-path imports that bypass published exports.
- Mirrored TypeScript/Python cores maintained only for visual symmetry.
- A desktop-host rule chosen from taste alone rather than product constraints.

## Review checks

- Can the core SDK be imported without an interface stack?
- Are use cases testable without transport objects?
- Do interfaces and transports depend inward, never the reverse?
- Is every physical package boundary earned and verified as an artifact?
- Are external values admitted once, with async ownership and errors explicit?
- Does each interface contain presentation/composition rather than domain policy?
- When languages or local/remote clients coexist, is the promised parity executable?
- Could a new interface reuse the application contract without changing core behavior?

## Sources

- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [TypeScript documentation](https://www.typescriptlang.org/docs/)
- [Python documentation](https://docs.python.org/3/)

## Related rules

For TypeScript, apply [architecture](../code/typescript/architecture.md), [API design](../code/typescript/api.md), [utilities](../code/typescript/util.md), [types](../code/typescript/types.md), [modules](../code/typescript/modules.md), [async](../code/typescript/async.md), [docs](../code/typescript/docs.md), and [environment](../code/typescript/environment.md). For Python, apply [mental model](../code/python/model.md), [OOP vocabulary](../code/python/oop.md), [file organization](../code/python/files.md), and [docstrings](../code/python/docstring.md). Apply [extension points](extension.md), [tests](test.md), and [docs](docs.md) as the surface requires.
