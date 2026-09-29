---
name: interfaces
description: Separate SDK, application, transport, and user-interface responsibilities.
---

# Service Interface Architecture

## Summary

Name responsibilities before naming folders. When all roles exist, dependencies flow in this direction:

## Principle

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

A language-native SDK may expose domain/core behavior directly for embedding. Interfaces that need shared orchestration call the application boundary instead of rebuilding policy in callbacks. HTTP, OpenAPI, JSON-RPC, MCP, terminal, browser, and desktop concerns remain adapters. Core code never imports them.

These are logical roles, not mandatory package or directory names. A cohesive library may keep them in one package. Split packages only when a role earns independent consumption, runtime or dependency isolation, release compatibility, ownership, build tooling, or artifact verification.

## Role contracts

### Domain/core and SDK

- Keep domain rules, durable invariants, storage ports, and reusable behavior independent of transports and presentation.
- Expose the shortest supported language-native entry point. Prefer owning objects for identity, state, invariants, and lifecycle; use functions for stateless transforms.
- Keep HTTP request objects, terminal widgets, browser globals, parser types, and desktop-host values out of core signatures.
- Do not make an interface stack a prerequisite for importing the SDK.

### Application boundary

- Put cross-feature use cases, policy sequencing, transaction scope, and interface-neutral authorization checks here rather than in domain entities or route callbacks.
- Define typed request, result, error, pagination, event, cancellation, and idempotency semantics once when multiple callers share them.
- Validate untrusted input at the owning boundary. Then pass admitted values inward.
- Keep methods testable without framework request/response objects.
- Separate process-local dependency injection from durable or wire contracts.

Call this role `application/`, `service/`, `use-cases/`, `api/`, or a repository-specific equivalent. Do not create an `api/` folder that only re-exports the SDK.

### Transport adapters and clients

- Translate transport values to application calls. Translate results/errors back to the transport. Do not own business policy.
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

## Pattern and Anti-pattern

- **Pattern:** CLI and HTTP adapters call the same application operation.
- **Anti-pattern:** CLI and HTTP callbacks each implement their own transaction and business rules.

Transport mapping has separate ownership from shared policy.

## Sources

- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [TypeScript documentation](https://www.typescriptlang.org/docs/)
- [Python documentation](https://docs.python.org/3/)

Use [layouts](interfaces/layout.md) for package or language boundaries and [adapters](interfaces/adapter.md) for CLI, GUI, desktop, MCP, TUI, automation, or HTTP decisions.
