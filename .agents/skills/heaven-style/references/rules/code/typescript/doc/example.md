---
id: ts-doc-example
title: TypeScript TSDoc example
description: Read for TypeScript tsdoc example.
blocking: true
---

# TypeScript TSDoc example

**Anti-pattern:**

```ts
/** Gets a user. */
export async function getUser(id: string): Promise<User | undefined> {
  // ...
}
```

**Recommended pattern:**

```ts
/**
 * Loads a user by its durable ID.
 *
 * Returns `undefined` when no user exists. Provider or decoding failures reject;
 * callers may cancel the lookup with `signal`.
 *
 * @param id - Validated durable user ID.
 * @param signal - Cancels the provider request without converting cancellation into a miss.
 */
export async function getUser(id: UserId, signal?: AbortSignal): Promise<User | undefined> {
  // ...
}
```

The summary should start with a verb for functions and a noun phrase for types/classes. Keep prose short enough to remain true.
