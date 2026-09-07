---
id: workflow-design-module
title: Module design
description: Read for module design.
---

# Module design

## Summary

Describe how a consumer uses the component before describing its internals.
Give implementers a compact object protocol, explicit obligations, and acceptance
tests. Keep one small public model while separating internal responsibilities.

## Component protocol

Recommend one short abstract class protocol for each stateful or replaceable
component. State its attributes, member signatures, and what each implementation
must do. Use an existing owner when it already defines the contract. Prefer a
structural TypeScript interface or Python Protocol when runtime inheritance
adds no behavior. A stateless utility can remain a typed function.

Show one short code block. Mark it as proposed until accepted. Keep concrete
drivers, algorithms, and helper classes out of this view. For example, this
proposed TypeScript protocol states the required behavior of a byte store:

```ts
/** Owns byte records in one namespace. Acquire resources before use. */
export abstract class Store {
  /** Keep this namespace stable for the lifetime of the store. */
  abstract readonly namespace: string;

  /** Return detached bytes, or undefined for a missing key. Reject I/O failures. */
  abstract get(key: string): Promise<Uint8Array | undefined>;

  /** Replace the record with owned bytes. Resolve after the write completes. */
  abstract put(key: string, value: Uint8Array): Promise<void>;

  /** Drain admitted work and release owned resources. Repeated calls are safe. */
  abstract close(): Promise<void>;
}
```

Document required value bounds, failure, cancellation, concurrency, and resource
ownership where they affect substitution. This short sketch does not replace
the source declaration or full API documentation. Link those owners once they
exist. Do not keep a second manual signature catalog beside them.

Minimize public classes, not internal responsibility boundaries. Do not add a
public abstract/concrete pair for every folder. Export the contract only when
consumers or extension authors need it. Keep implementation classes private
where possible. Optional capabilities must not enlarge the required protocol
with no-op or unsupported methods.

## Module design output

Start with a short brief under the [plan workflow](plan.md). After confirmation,
expand the following facts where the component needs them. Put developer-only
detail in a fold or linked reference after the consumer path.

### Required sections

1. **Problem and success criteria** — user-visible outcome and measurable done state.
2. **Non-goals** — explicit exclusions to prevent scope creep.
3. **Layer placement** — which architectural layer owns the module; what it may import; what must not import it.
4. **Public surface** — classes, functions, CLI commands, and variation hooks. Examples use the target package's supported public facade and extension-author entry points.
5. **Component protocol** — attributes, signatures, short implementation obligations, and a link to their source owner.
6. **Data and control flow** — read/write paths, variation dispatch, and the target repository's matched configuration owner; direct settings/spec objects are valid when no shared manager exists.
7. **Variation seam** — Registry API for an open family or discriminated/exhaustive contract for a closed set; no concrete-name routing in high-level policy. For independently extensible families, document descriptor persistence, source-independent loading, provenance, conflict policy, and the built-in extraction fitness test.
8. **Migration / compatibility** — rename map, owned call-site sweep, external consumers, repository support policy, and removal conditions for temporary shims.
9. **Tests and examples** — behavior contracts agents must implement.
10. **Docs touch list** — user docs, mental model/reference pages, goals, development log, generated docs, and scratch cleanup.
11. **Slices** — ordered implementation slices with acceptance criteria and verification commands.
12. **Risks and waivers** — anything that needs explicit human approval.

Add an **Agile feedback gates** section before handoff: tests, demos, review checkpoints, or issue acceptance checks that let the design adapt after each implementation slice.

### API traceability

Use a table only when it helps trace several public symbols to their docs and
tests. Do not repeat the protocol. Select [TypeScript API design](../../rules/code/typescript/api.md)
or [Python OOP/naming](../../rules/code/python/verbs.md) for the target language.

| Symbol | Kind | Layer | Inputs | Returns | Failures | Variation seam | Doc page | Test anchor |
|--------|------|-------|--------|---------|----------|----------------|----------|-------------|
| `registerFoo` | function | composition | validated ID, builder | disposer | duplicate registration | open registry owned by app scope | `reference/foo.md` | registration contract suite |

Add columns only when they resolve ambiguity. Link the source for exact signatures.

## Acceptance

A consumer can identify the shortest use path and necessary public classes.
An implementer can identify required attributes, methods, failure behavior,
and tests without reading a concrete implementation. Each abstraction has a
real consumer or variation requirement. The [manager](../../tasks/manager.md)
checks these conditions before dispatch.
