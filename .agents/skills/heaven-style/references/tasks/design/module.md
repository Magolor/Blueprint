---
name: workflow-design-module
description: Read before designing a module or component contract.
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

Start with the [design template](../../../assets/templates/design.md): explain the
idea, intuition, architectural relationships, and tradeoffs. A component protocol
is a focused contract supplement when needed; it does not turn the design into
an implementation plan. Keep consumer meaning before developer-only detail.

### Design and contract content

- **Motivation and non-goals:** the tension the idea resolves and its boundaries.
- **Layer placement:** responsibility, allowed imports, and forbidden dependencies.
- **Public mental model:** the smallest set of classes, functions, CLI concepts,
  and variation hooks. Examples use supported consumer or extension-author facades.
- **Component protocol:** where needed, link the attributes, signatures, and
  implementation obligations in their [contract owner](../../../assets/templates/contract.md).
- **Data and control flow:** read/write paths, dispatch, and configuration authority;
  direct settings/spec objects are valid without a shared manager.
- **Variation boundary:** registration for an open family, exhaustive contracts
  for closed variants. When independent extensibility is promised, explain
  descriptor persistence, source-independent loading, provenance, conflicts,
  and how bundled/external parity can be assessed.
- **Tradeoffs and open choices:** alternatives, failure/lifecycle implications,
  compatibility obligations, and any decision beyond existing authority.

### Implementation handoff

When implementation is authorized, the linked [plan](plan.md) owns measurable
success criteria, behavior tests/examples, exact verification commands, and
ordered slices. Include the rename map and owned-call-site sweep, external
consumer promises, and removal conditions for temporary shims there. Name
user docs, mental models/references, goals, devlog, generated docs, and scratch
cleanup in the plan's docs touch list. Each slice has feedback through tests,
demos, review checkpoints, or issue acceptance. Do not force these execution
details into a document whose purpose is to explain the idea.

### API traceability

Use a table only when it helps trace several public symbols to their docs and
tests. Do not repeat the protocol. Select [TypeScript API design](../../rules/code/typescript/api.md)
or [Python OOP/naming](../../rules/code/python/vocab/verbs.md) for the target language.

| Symbol | Kind | Layer | Inputs | Returns | Failures | Variation seam | Doc page | Test anchor |
|--------|------|-------|--------|---------|----------|----------------|----------|-------------|
| `registerFoo` | function | composition | validated ID, builder | disposer | duplicate registration | open registry owned by app scope | `reference/foo.md` | registration contract suite |

Add columns only when they resolve ambiguity. Link the source for exact signatures.

## Contract handoff readiness

A consumer can identify the shortest use path and necessary public classes.
An implementer can identify required attributes, methods, failure behavior,
and tests without reading a concrete implementation. Each abstraction has a
real consumer or variation requirement. The [manager](../coordinate/README.md)
checks these conditions before dispatch.
