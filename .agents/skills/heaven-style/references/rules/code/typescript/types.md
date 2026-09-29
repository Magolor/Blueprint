---
name: ts-types
description: Define strict TypeScript contracts, validated input, and ownership.
---

# TypeScript Types and Language Shape

## Summary

Make invalid states difficult to represent and external states impossible to trust accidentally. Compile all owned TypeScript under a strict project. Keep untrusted values `unknown` until runtime validation succeeds. Use assertions only at small boundaries whose invariant is explained and tested.

## Strict baseline

The exact compiler profile belongs to [TypeScript environment](env.md). Owned code must be covered by `strict` checking. Unchecked indexing must stay visible. Optional-property presence must be deliberate. Overrides, returns, and switch fallthrough must be checked. Type-only imports must remain distinguishable from runtime edges.

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

For external values or escapes, read [input validation](types/input.md). For optionality, variants, or IDs, read [data shapes](types/shape.md). Symbol naming lives in [names](name.md).
