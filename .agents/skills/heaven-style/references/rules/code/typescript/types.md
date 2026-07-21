---
id: ts-types
title: TypeScript types and language shape
enabled: true
blocking: true
order: 220
category: code-quality
keywords: [TypeScript strict, unknown, any, assertion, discriminated union, branded type, readonly, satisfies, exactOptionalPropertyTypes, runtime validation]
description: Use when adding or reviewing TypeScript types, public signatures, external data, unions, identifiers, config shapes, assertions, or strict compiler options.
---

# TypeScript Types and Language Shape

## Core rule

Make invalid states difficult to represent and external states impossible to trust accidentally. Compile all owned TypeScript under a strict project, keep untrusted values `unknown` until runtime validation succeeds, and use assertions only at small boundaries whose invariant is explained and tested.

## Apply when

- Adding or changing exported functions, classes, interfaces, schemas, events, result types, IDs, config, or wire/persistence formats.
- Reading JSON, environment variables, CLI arguments, HTTP/provider payloads, database rows, message events, or plugin input.
- Using `any`, `unknown`, `as`, `!`, enums, namespaces, index signatures, optional properties, or generic helper types.
- Adding compiler/linter escapes or deciding how much annotation is useful.

## Strict baseline

The exact compiler profile belongs to [TypeScript environment](environment.md). Semantically, owned code must be covered by `strict` checking, unchecked indexing must stay visible, optional-property presence must be deliberate, overrides/returns/switch fallthrough must be checked, and type-only imports must remain distinguishable from runtime edges.

- Typecheck source, tests, examples, scripts, and owned tool/config TypeScript. Use separate `tsconfig` files when different runtimes or globals require different environments.
- `exactOptionalPropertyTypes` is the greenfield default. Enabling it in an existing codebase is an intentional migration, not an incidental formatting edit.
- Do not enable `allowJs` unless the repository is performing an explicit JavaScript migration.
- Add DOM, JSX, Node, Bun, test, or framework globals only to the projects that use them.
- `skipLibCheck` is a performance tradeoff, not proof of strictness. Foundational published libraries should avoid it when feasible or compensate with a clean consumer declaration test.
- TypeScript project references and `tsc -b` are for a real package graph or measured typecheck problem, not default scaffold ceremony.

The runner/transpiler is not a typechecker. `bun test`, Bun's bundler, Vite, esbuild, and similar tools do not replace `tsc --noEmit` or an equivalent checked build.

## Annotation policy

- Annotate exported function/method parameters and return types so implementation inference cannot change the public contract accidentally.
- Annotate callbacks and internal boundaries when inference would widen, leak `any`, or obscure intent.
- Let local variables and obvious private helpers infer their types.
- Prefer a concrete domain type over `Record<string, unknown>` once the shape has meaning.
- Avoid type gymnastics that make callers pay for implementation cleverness. Complex generics are justified when they materially improve extension-author or caller safety and have type-level tests.

## External values stay unknown

Treat decoded JSON, wire payloads, environment values, persistence records, plugin messages, and caught errors as `unknown` until validated.

**Anti-pattern:**

```ts
const config = JSON.parse(text) as AppConfig
return client.run(config)
```

**Recommended pattern:**

```ts
const raw: unknown = JSON.parse(text)
const config = AppConfigSchema.parse(raw)
return client.run(config)
```

The schema library is repository-owned; do not add a validation dependency when a small type guard is enough. For important schemas, prefer one source that drives runtime validation and inferred TypeScript types. Test invalid values and, when conversion logic is nontrivial, property-test that encoding/validation agree.

## `unknown`, `any`, and assertions

- Use `unknown` at genuine integration boundaries and narrow it through a schema, predicate, `instanceof`, discriminant, or explicit property checks.
- Do not use implicit or convenience `any` in owned code. An upstream boundary or genuinely unrepresentable generic/interop implementation may use explicit `any` only in the narrowest statement/signature, with a reason, a typed public boundary, and type-level tests proving caller safety.
- Ban `as unknown as T`, broad assertion helpers, and assertion chains that manufacture trust.
- Prefer `satisfies` when checking an object without widening its inferred literals.
- Avoid non-null assertions. Prove presence with a guard or a lookup helper that throws contextually.
- Use `@ts-expect-error` only for a deliberate negative type test or a documented upstream defect. Include a reason and keep the suppression on the exact line; do not use `@ts-ignore`.

```ts
const DEFAULTS = {
  mode: 'safe',
  retries: 2,
} as const satisfies AppDefaults
```

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

Do not force genuinely orthogonal facts into a false union. A process may be timed out and still report an exit code after trapping the signal; model independent facts independently.

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

## Readonly and ownership

- Accept `readonly` arrays/objects when a function does not mutate caller-owned data.
- Prefer immutable configuration, capability, and strategy records.
- Clone or freeze at ownership boundaries. `readonly` is compile-time only and does not protect a mutable backing object shared with another owner.
- Avoid mutating arguments, cached return objects, registry snapshots, or event payloads after publication.
- Return snapshots or readonly views from mutable registries; document whether nested values remain live.

## Prefer erasable, standard syntax

- Prefer string literal unions plus `as const` data over runtime TypeScript enums.
- Avoid namespaces with runtime code, parameter properties, `import =`, and `export =` in new ESM code.
- Consider `erasableSyntaxOnly` for code intended to run through native type stripping or multiple runtimes.
- Prefer ordinary ECMAScript constructs so Bun, Node, bundlers, tests, and editors see the same runtime shape.
- Use `import type` and `export type` for type-only dependencies; combine this with `verbatimModuleSyntax`.

Frameworks that require decorators, emitted metadata, namespaces, or other non-erasable syntax are repository-level exceptions; keep those options scoped to their project.

## Names

- `camelCase` for variables, functions, and methods.
- `PascalCase` for classes, interfaces, type aliases, and components.
- `SCREAMING_SNAKE_CASE` only for true process/module constants, not ordinary immutable locals.
- Predicates start with `is`, `has`, or `can`.
- Use one term per concept and short names whose context remains obvious; do not port Python `snake_case` symbol rules into TypeScript.
- Prefer domain vocabulary over suffixes such as `Impl`, `Manager`, `Helper`, `Utils`, or `Data` unless the suffix conveys a real role.

## Review checks

- Does the compiler cover every owned TypeScript surface?
- Can external data reach domain code without runtime validation?
- Does any `any`, assertion, non-null assertion, or suppression lack a narrow reason?
- Are optional, undefined, and null states intentional?
- Can a discriminated union represent an impossible combination?
- Are IDs confused because they share `string`?
- Does `readonly` hide shared mutable backing state?
- Can a public return type change accidentally through inference?
- Does runtime-only TypeScript syntax reduce portability without buying real value?

## Related rules

Also apply [architecture.md](architecture.md) for open/closed variation and capability contracts, [modules.md](modules.md) for type-only imports and package boundaries, [async.md](async.md) for promises/errors/cancellation, [docs.md](docs.md) for public type semantics, and [environment.md](environment.md) for complete `tsconfig` and gate examples.
