---
id: ts-types-shape
title: TypeScript data shapes
description: Read for TypeScript data shapes.
blocking: true
---

# TypeScript data shapes

## Optionality is a contract

Distinguish these states deliberately:

- `field?: T` — the property may be absent.
- `field: T | undefined` — the property must be present, and its value may be undefined.
- `field: T | null` — null is a domain/wire value.

Do not append `| undefined` mechanically to every optional property. Use a required-but-undefined-capable field when presence itself is a safety or normalization invariant.

Raw requests may omit caller choices; runtime execution consumes a resolved spec:

```ts
interface RunRequest {
  readonly timeoutMs?: number
  readonly owner?: OwnerId
}

interface RunSpec {
  readonly timeoutMs: number
  readonly owner: OwnerId | undefined
}

function resolveRun(request: RunRequest, config: RunConfig): RunSpec {
  return {
    timeoutMs: request.timeoutMs ?? config.timeoutMs,
    owner: request.owner,
  }
}
```

Resolve and validate once in the layer that owns the defaults. Do not scatter `?? config...` through execution code.

## Discriminated unions

- Use a stable literal tag such as `kind`, `type`, or `status` for domain alternatives and state machines.
- Keep variant-specific fields on their variants rather than making every field optional on one broad interface.
- Switch on the tag. Closed unions end in an `assertNever` path and enable exhaustive-switch linting.
- An intentionally open/declaration-merge union cannot be exhaustive; handle known variants and document the unknown/fallback behavior.
- Prefer result variants for expected domain outcomes; reserve exceptions for failures that break the operation's contract.

**Anti-pattern:**

```ts
interface Outcome {
  ok: boolean
  value?: Value
  error?: Error
  aborted?: boolean
}
```

**Recommended pattern:**

```ts
type Outcome =
  | { kind: 'success'; value: Value }
  | { kind: 'aborted'; reason: string }
  | { kind: 'failure'; error: AppError }
```

Do not force independent facts into a false union. A process may be timed out and still report an exit code after trapping the signal. Model independent facts independently.

## Opaque identifiers

Use branded/opaque primitive types when two cross-boundary identifiers share a primitive and mixing them would be dangerous:

```ts
declare const brand: unique symbol
type Branded<Name extends string> = string & { readonly [brand]: Name }

type SessionId = Branded<'SessionId'>
type TaskId = Branded<'TaskId'>

function sessionId(value: string): SessionId {
  if (!value) throw new Error('session id must not be empty')
  return value as SessionId
}
```

- The owning module defines the brand and the narrow construction/validation function.
- Brand durable or wire-visible IDs that are easy to confuse, not every local string.
- Branding is not runtime validation; validate before casting.
