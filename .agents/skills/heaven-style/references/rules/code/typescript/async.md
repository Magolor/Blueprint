---
id: ts-async
title: TypeScript async, errors, and resources
blocking: true
description: Own promises, cancellation, timeouts, resources, and asynchronous state.
---

# TypeScript Async, Errors, and Resources

## Core rule

Async work has an owner, a cancellation path, an observed result, and completed teardown. Await or return every promise, or deliberately transfer it to an owner that contains its rejection. Errors preserve context and stable facts. Boundary code minimizes ambient authority.

## Promise ownership

- Await a promise when subsequent behavior depends on completion.
- Return it when the caller owns completion and failure.
- Deliberately detach only when another owner observes/logs rejection and lifecycle.
- `void task()` documents discarded value, not handled failure. Use it only when `task` contains its own errors or the surrounding framework has a proven rejection owner.
- Use `Promise.all` when all operations must succeed. Use `Promise.allSettled` when every outcome must be observed. Use an explicit concurrency limiter when concurrent work can exhaust resources.
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

Use `Promise.all` instead when operations are independent and bounded parallelism is intended. It fails on the first rejection but is not atomic: sibling operations keep running after one rejects. If partial completion is invalid, use the storage/provider's real transaction or compensation contract. If every outcome must be observed before returning, use `Promise.allSettled`. Inspect every rejection in that case.

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

For startup, observation, callbacks, and teardown, read [lifecycle](async/life.md). For failures, retries, fallback, and subprocess authority, read [errors](error.md).
