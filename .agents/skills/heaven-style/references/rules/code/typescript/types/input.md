---
name: ts-types-input
description: Read before validating TypeScript input or using type assertions.
---

# TypeScript input validation

## Summary

Validate external values from unknown and keep type escapes narrow and justified.

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
const FORMAT_MARKERS = {
  json: 'application/json',
  text: 'text/plain',
} as const satisfies Record<string, string>
```
