---
id: ts-async
title: TypeScript async, errors, and resources
enabled: true
blocking: true
order: 70
category: code-quality
keywords: [TypeScript promise, no-floating-promises, AbortSignal, error cause, dispose, async lifecycle, callback exception, subprocess security, teardown]
description: Use when TypeScript code handles promises, callbacks, events, cancellation, errors, subprocesses, resources, concurrency, startup, or teardown.
---

# TypeScript Async, Errors, and Resources

## Core rule

Async work has an owner, a cancellation path, an observed result, and a completed teardown. Every promise is awaited, returned, or deliberately handed to an owner that contains its rejection. Errors preserve context and stable facts; boundary code minimizes ambient authority.

## Apply when

- Adding async functions, timers, streams, workers, subprocesses, background tasks, event listeners, callbacks, queues, connection pools, or cleanup.
- Catching/rethrowing errors, defining result/error types, implementing retries/timeouts, or accepting `AbortSignal`.
- Registering callbacks/plugins, acquiring resources, or translating between in-band and thrown failures.
- Handling credentials, environments, temporary files, or untrusted output.

## Promise ownership

- Await a promise when subsequent behavior depends on completion.
- Return it when the caller owns completion and failure.
- Deliberately detach only when another owner observes/logs rejection and lifecycle.
- `void task()` documents discarded value, not handled failure. Use it only when `task` contains its own errors or the surrounding framework has a proven rejection owner.
- Use `Promise.all` when all operations must succeed, `Promise.allSettled` when every outcome must be observed, and an explicit concurrency limiter when fan-out can exhaust resources.
- Do not use `forEach(async ...)`; choose sequential `for...of` or awaited parallel composition.

**Anti-pattern:**

```ts
items.forEach(async item => {
  await persist(item)
})
return { saved: true }
```

**Recommended pattern:**

```ts
for (const item of items) {
  await persist(item)
}
return { saved: true }
```

Use `Promise.all` instead when operations are independent and bounded parallelism is intended. It is fail-fast, not atomic: sibling operations keep running after one rejects. If partial completion is invalid, use the storage/provider's real transaction or compensation contract; if every outcome must be observed before returning, use `Promise.allSettled` and inspect every rejection.

Enable type-aware linting for async-heavy, lifecycle-owning, or published code. At minimum enforce equivalents of:

- `@typescript-eslint/no-floating-promises`
- `@typescript-eslint/no-misused-promises`
- `@typescript-eslint/require-await`

Do not disable them for an entire test tree. Relax one rule for a narrow mock/test pattern and explain why the promise contract remains safe.

## Cancellation and timeouts

- Accept and forward `AbortSignal` through every layer that can cancel work.
- Check pre-aborted signals before starting irreversible work.
- Compose caller cancellation with timeouts without losing which condition occurred.
- Remove abort listeners and clear timers in every completion path.
- A timeout is policy; the operation/result reports the actual outcome separately.
- Do not translate cancellation into an unrelated generic failure or silently retry it.

```ts
async function fetchProfile(id: ProfileId, signal: AbortSignal): Promise<Profile> {
  signal.throwIfAborted()
  const response = await fetch(`/profiles/${id}`, { signal })
  if (!response.ok) throw new HttpError(response.status, 'profile request failed')
  return ProfileSchema.parse(await response.json())
}
```

Use `using`/`await using` and `Symbol.dispose`/`Symbol.asyncDispose` for lexical resources when the target runtimes and dependencies support explicit resource management. Otherwise use a short `try/finally`; do not rely on every caller remembering a separate cleanup call.

## Observe real state

- Drive async control flow from the event, promise, stream state, or durable record that proves a transition occurred.
- Do not set work in motion and immediately branch on state that changes later.
- If waiting for a transition, handle the branch where no transition can occur; an idle wait with no submitted work must not hang.
- Serialize operations that share a key or mutable resource across `await` points. The JavaScript event loop still permits logical races.

**Anti-pattern:**

```ts
agent.send(message)
if (agent.status === 'idle') return
```

**Recommended pattern:**

```ts
const turn = agent.send(message)
await turn.done
```

## Explicit startup and quiescent teardown

- Constructors stay synchronous and avoid network, filesystem, process, or registry effects.
- Use `create`, `connect`, `start`, or framework lifecycle hooks for acquisition.
- Teardown first prevents new notifications/work, then cancels/stops children, awaits their completion, closes resources, and only then resolves.
- Cleanup is idempotent or fails with a documented state error.
- Do not let a later close error hide an earlier drain/data-loss error; preserve both with `AggregateError` or `cause` while keeping the primary failure clear.
- Tests assert the resource is gone immediately after awaited disposal—not “eventually.”

```ts
async close(): Promise<void> {
  this.closed = true
  this.listeners.clear()
  const tasks = [...this.tasks]
  for (const task of tasks) task.abort()
  const failures: unknown[] = []
  const settled = await Promise.allSettled(tasks.map(task => task.done))
  for (const result of settled) {
    if (result.status === 'rejected' && !isExpectedAbort(result.reason)) {
      failures.push(result.reason)
    }
  }
  try {
    await this.client.close()
  } catch (cause: unknown) {
    failures.push(cause)
  }
  if (failures.length > 0) {
    throw new AggregateError(failures, 'service shutdown failed')
  }
}
```

The owner defines `isExpectedAbort` narrowly for its own cancellation contract. Never discard all rejected cleanup results merely because `allSettled` fulfilled.

## Callback and observer boundaries

- Document whether callbacks are trusted, ordered, short-circuiting, or isolated.
- For notification/subscriber APIs, catch each callback independently, report it through the owning logger/error channel, and continue unless veto semantics are explicit.
- For middleware/waterfalls, preserve the framework's delegation/short-circuit contract and test every valid completion mode.
- Register transactionally: validate first, make rollback/disposal available before invoking observers, and leave no half-installed state when a callback throws.
- Registration with a lifetime returns a disposer or is bound to an explicit owner scope.

```ts
type Listener = (event: DomainEvent) => void | Promise<void>

const listeners = [...this.listeners]
for (const listener of listeners) {
  try {
    await listener(event)
  } catch (cause: unknown) {
    this.log.error('event listener failed', { cause, event: event.kind })
  }
}
```

This example snapshots registration before dispatch and defines ordered async notification semantics; listener registration changes affect the next event, not the current walk. If listeners are intentionally synchronous, reject promise-returning listeners at the API boundary and keep the typed-lint guard. If they are intentionally parallel, use `Promise.allSettled` and report every rejection before returning.

Do not swallow callback failures without a named policy. A truly ignorable catch keeps the `try` as small as possible and comments which exact failure is intentionally ignored and why no other error can reach it.

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
- Bound attempts, total time, and backoff; make cancellation interrupt sleep and work.
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

## Review checks

- Is every promise awaited, returned, or owned by a rejection/lifecycle boundary?
- Can a timeout, abort, timer, listener, worker, or child process leak?
- Does teardown resolve only after resources reach quiescence?
- Does control flow assume a requested async transition happened synchronously?
- Can one callback exception starve later callbacks or reject core lifecycle?
- Does a catch add value, preserve `cause`, and avoid silent fallback?
- Do callers branch on stable error facts rather than messages?
- Are independent result facts modeled independently?
- Can retry duplicate a non-idempotent effect or ignore cancellation?
- Does any outbound process/wire object carry ambient secrets or unnecessary fields?

## Related rules

Also apply [architecture.md](architecture.md) for lifecycle ownership and registries, [api.md](api.md) for factories and lifecycle verbs, [util.md](util.md) for files/process/platform ownership, [types.md](types.md) for `unknown`/result contracts, [modules.md](modules.md) for optional imports, [sql.md](sql.md) for database transactions/resources, [docs.md](docs.md) for errors/disposal documentation, and [environment.md](environment.md) for typed lint and test gates.
