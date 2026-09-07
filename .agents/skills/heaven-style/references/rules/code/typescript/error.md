---
id: ts-error
title: TypeScript errors and recovery
description: Read for TypeScript errors and recovery.
blocking: true
---

# TypeScript errors and recovery

## Error contracts

- Throw `Error` objects, not strings or arbitrary values.
- Catch `unknown` and narrow before reading properties.
- Catch only where the layer can add context, retry, translate into a documented result, or contain an integration failure.
- Preserve the original failure with `cause`.
- Infrastructure/public errors that callers branch on have a stable code or discriminated type; callers do not parse message text.
- Expected domain outcomes may be result variants. Programmer errors, violated invariants, and unusable infrastructure reject/throw.
- Keep orthogonal facts orthogonal. For process results, `timedOut`, `aborted`, `signal`, `exitCode`, and sandbox denial may coexist.
- Fail at the earliest point with complete knowledge: bootstrap for self-contained invalid config, otherwise when the referenced implementation/resource becomes knowable.

```ts
class IntegrationError extends Error {
  readonly code: 'MISSING_DEPENDENCY' | 'UNAVAILABLE' | 'INVALID_RESPONSE'

  constructor(
    code: 'MISSING_DEPENDENCY' | 'UNAVAILABLE' | 'INVALID_RESPONSE',
    message: string,
    options?: ErrorOptions,
  ) {
    super(message, options)
    this.name = 'IntegrationError'
    this.code = code
  }
}
```

Avoid one custom error class per message. Add taxonomy only where callers, logs, retries, protocols, or tests need stable distinctions.

## Retries and fallbacks

- Retry only errors proven transient and only when the operation is idempotent or has an idempotency key.
- Bound attempts, total time, and backoff. Make cancellation interrupt sleep and work.
- Preserve the final cause and attempt context.
- A fallback is explicit in the result/diagnostics. Never silently return `{}`, `[]`, `undefined`, cached data, or a local provider when the requested provider failed.
- Circuit breakers, queues, and retry frameworks require measured pressure; do not add them speculatively.

## Boundary authority and subprocesses

- Build outbound wire/process/persistence objects from allowlisted fields. Do not spread an internal object and redact afterward.
- Child processes receive the smallest environment required. Start from a scrubbed/allowlisted environment and add explicit values; do not inherit credentials by default.
- Never log tokens, authorization headers, full secret-bearing URLs, raw environment objects, or unsanitized provider errors.
- Bound captured output and record truncation. Spill only to a private directory with random names and exclusive owner-only creation.
- Pass command arguments as arrays where possible. If a shell is required, keep the shell boundary explicit and validate/escape untrusted input with a proven library.
- Give subprocesses a work directory, cancellation/timeout policy, ownership token when multi-tenant, and awaited cleanup.

**Anti-pattern:**

```ts
spawn(command, { env: process.env })
writeFile(`/tmp/result-${userId}.log`, output)
```

**Recommended pattern:**

```ts
spawn(executable, args, {
  env: pickProcessEnv(['PATH', 'HOME']),
  signal,
  cwd: workdir,
})
```

The exact environment/path helpers are repository-owned. The rule is minimal ambient authority and exclusive private resources, not one mandatory utility package.
