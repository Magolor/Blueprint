---
id: ts-docs
title: TypeScript API documentation
enabled: true
blocking: true
order: 250
category: code-quality
keywords: [TSDoc, JSDoc, TypeScript public API, "@param", "@returns", "@throws", module comment, documentation examples, generated docs]
description: Use when adding or reviewing TypeScript public exports, package entry points, JSDoc/TSDoc, examples, generated catalogs, or declaration-facing documentation.
---

# TypeScript API Documentation

## Core rule

Public TypeScript contracts need semantic TSDoc/JSDoc, not Python Google-style sections and not comments that repeat names. Types describe shape; documentation explains meaning, lifecycle, ownership, failure, side effects, units, constraints, and safe use.

## Apply when

- Adding or changing a published export, extension seam, service interface, public class/function/method, package entry point, event, config schema, or result type.
- Changing behavior that appears in README examples, generated catalogs, API docs, package declarations, or checked code snippets.
- Adding a documentation generator or export-documentation gate.

## Public documentation baseline

- Published package exports and stable extension seams have a concise summary plus the semantics callers cannot infer from the type.
- Public functions/methods have explicit return types. Document parameters and returns when their role, units, bounds, ownership, defaulting, or side effects are not obvious.
- Document thrown/rejected errors callers can handle, cancellation behavior, resource ownership, disposal requirements, mutation, ordering, retry/idempotency, and concurrency guarantees.
- Public classes document the object model and constructor/config role. Do not repeat every constructor field in both the class and constructor comment.
- Package entry modules may have a module-level purpose comment when it materially helps consumers. Do not require a module comment on every internal file.
- Internal/private helpers need comments only for non-obvious invariants or transformations.
- Follow the target documentation renderer's TSDoc/JSDoc support; do not invent unsupported tags.

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

## What types do not explain

Document these when relevant:

- whether absence, `undefined`, and `null` differ;
- whether input is copied, frozen, retained, or mutated;
- whether returned collections are snapshots or live views;
- whether results preserve input order;
- units and inclusive/exclusive bounds;
- configuration precedence and when defaults resolve;
- lifecycle and whether `close`/disposal reaches quiescence;
- whether a nonzero process exit is a result or an exception;
- retry/idempotency and at-most/at-least/exactly-once behavior;
- callback ordering, short-circuiting, and error containment;
- capability/fallback honesty;
- supported literal values when a generated reference is not already authoritative.

Do not narrate implementation steps that callers cannot observe.

## Tags

- Use `@param` for non-obvious parameter semantics or when the repository's API generator requires every parameter.
- Use `@returns` when the result semantics are not obvious from the type.
- Use `@throws` for synchronous or rejected errors that form part of the public contract; state the condition, not every internal exception.
- Use `@example` for a short realistic path when it reduces misuse.
- Use `@remarks`/`@internal`/`@public` only when supported by the chosen documentation tool.
- Use `@deprecated` only when the repository's stable compatibility policy requires a deprecation window. Unreleased/internal break-and-fix changes remove the old API and update call sites.

Do not use Python `Args:`, `Returns:`, or `Raises:` sections in TypeScript comments.

## One authoritative home

- Give each durable fact one source of truth. Link to the owning type/schema/config page instead of copying tables into multiple READMEs.
- Generate catalogs, module graphs, event lists, config references, or API inventories from source when repeated manual sync has caused drift.
- Generated artifacts have a regeneration command and a check mode that fails when stale.
- Documentation describes the current contract, not the chronology of how it changed. Put historical decisions in ADRs, release notes, or progress reports.
- Planned behavior is labeled planned and does not appear in current API reference/examples.

## Examples and snippets

- Public examples import through the package's supported entry point, not source aliases or internal modules.
- Typecheck documentation snippets when the repository has enough examples for drift to be a recurring risk.
- Run important examples or smoke them against built/packed output before release.
- Use realistic values without real credentials or secret-shaped placeholders that users may copy into commits.
- Keep generated/runtime example output in the repository's declared temp path.
- If an example demonstrates an optional integration, name the install/config prerequisite and expected failure when absent.

## Mechanical gates

For a published library or large extension SDK, add narrow gates when they enforce real standing promises:

- exported symbols have description prose and explicit function return types;
- package exports match declarations and built files;
- checked snippets compile;
- generated API/config/event catalogs are current;
- links and package subpaths resolve;
- a clean consumer imports the public surface.

Do not impose module-level JSDoc on every file, a word budget, or a custom documentation generator without demonstrated maintenance pressure.

## Suppressions and waivers

- Documentation/lint/type escapes are line- or symbol-scoped and include why the invariant remains safe.
- A public symbol omitted from docs has a deliberate reason such as framework protocol inheritance, generated heritage, or an internal-marked export.
- Do not disable export documentation for an entire package because one generated symbol is awkward; add a narrow allowlist and a removal condition.

## Review checks

- Does the public comment explain semantics rather than restate the name/type?
- Are lifecycle, cancellation, ownership, errors, and side effects documented where callers need them?
- Can a public return type change accidentally through inference?
- Is the same fact copied into multiple authoritative-looking places?
- Do examples use supported package entry points and compile/run against the real contract?
- Are generated docs reproducible and checked for drift?
- Does any deprecation/compatibility prose conflict with the repository's actual release stance?
- Are private/internal comments carrying user-facing facts that belong on the public boundary?

## Related rules

Also apply [types.md](types.md) for public type contracts, [modules.md](modules.md) for exports and packed consumers, [async.md](async.md) for lifecycle/error semantics, [architecture.md](architecture.md) for the public mental model, and [../../project/docs.md](../../project/docs.md) for repository-wide docs synchronization.
