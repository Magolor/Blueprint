---
name: ts-async-life
description: Read before implementing TypeScript startup, observers, or teardown.
---

# TypeScript resource lifecycle

## Summary

Observe actual async transitions and complete owned teardown before reporting disposal.

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
- During teardown, first prevent new notifications/work. Then cancel/stop children. Await their completion. Close resources. Resolve teardown only after these steps finish.
- Cleanup is idempotent or fails with a documented state error.
- Do not let a later close error hide an earlier drain/data-loss error; preserve both with `AggregateError` or `cause` while keeping the primary failure clear.
- Tests assert that the resource is gone immediately after awaited disposal, not “eventually”.

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
- For notification/subscriber APIs, catch each callback failure independently. Report it through the owning logger/error channel. Continue unless veto semantics are explicit.
- For middleware/waterfalls, preserve the framework's delegation/short-circuit contract and test every valid completion mode.
- Register transactionally. Validate first. Make rollback/disposal available before invoking observers. Leave no half-installed state when a callback throws.
- Registration with a lifetime returns a disposer or is bound to an explicit owner scope.

```ts
type Listener = (event: DomainEvent) => void | Promise<void>

const listeners = [...this.listeners]
for (const listener of listeners) {
  try {
    await listener(event)
  } catch (cause: unknown) {
    this.log.error('event listener failed', { cause, event: event.eventType })
  }
}
```

This example snapshots registration before dispatch and defines ordered async notification semantics. Listener registration changes affect the next event, not the current dispatch. If listeners are intentionally synchronous, reject promise-returning listeners at the API boundary. Keep the typed-lint guard for those synchronous listeners. If listeners are intentionally parallel, use `Promise.allSettled`. Report every rejection before returning from parallel dispatch.

Do not swallow callback failures without a named policy. A truly ignorable catch keeps the `try` as small as possible and comments which exact failure is intentionally ignored and why no other error can reach it.
