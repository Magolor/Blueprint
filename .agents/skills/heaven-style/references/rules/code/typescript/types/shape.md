---
name: ts-types-shape
description: Read before modeling TypeScript optionality, unions, or identifiers.
---

# TypeScript data shapes

## Summary

Represent presence, variants, and identifiers deliberately so types preserve domain distinctions.

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

- Use a stable literal tag that names its domain: `status` for outcomes, `operation` for operations, `provider` for providers. Avoid generic `kind`/`type` when the concept has a precise name; preserve external protocol fields.
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
  | { status: 'success'; value: Value }
  | { status: 'aborted'; reason: string }
  | { status: 'failure'; error: AppError }
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
