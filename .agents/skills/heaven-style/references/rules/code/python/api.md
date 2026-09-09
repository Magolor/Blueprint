---
name: model
description: Minimize Python public APIs and choose owning objects or functions.
---

# Mental model

## Summary

Keep the public OOP interface as small as possible. For each feature, expose the shortest flow through its owning object. Classmethods create or load objects. Instance methods perform lifecycle actions. Common code reads as `obj = Class(...); obj.verb()` or `Class.from_dict(...).verb()`. Do not introduce public classes, free functions, constructor flags, or DSL syntax unless they remove real complexity for users.

## Do

- Prefer object member functions as much as the domain permits. Put domain operations on existing methods or classmethods, including pure construction and conversion, instead of parallel free functions. Statelessness alone does not remove domain ownership.
- Use a direct function only for a genuinely independent utility or algorithm without a natural domain owner. Do not invent a wrapper class for it.
- Put behavior on the object that owns the state: `from_dict`, `from_schema`, and `load` create or reopen objects; `register`, `set_default`, `verify`, `connect`, and `close` act on those objects.
- Prefer keyword arguments whenever possible, especially for options, flags, limits, and values with similar types. Use keyword-only parameters to make that intent explicit; keep a natural primary operand positional where useful. There is no hard-coded positional-argument count limit.
- Keep constructors focused on identity and essential configuration. Move optional lifecycle side effects to explicit methods.
- Prefer familiar Python protocols and industrial interfaces over invented mini-languages.
- Keep one clear data container with structured attributes when extra wrapper classes add no behavior.
- Use dedicated classes only for behavior, invariants, lifecycle, or recognized domain concepts.
- Keep the ordinary user entry point domain-shaped. Hide incidental Registry mechanics. Also expose one stable, documented extension-author contract for manifests, registration, inspection, and lifecycle. Extension authors must not depend on private internals. Public docs and examples start from the target package's supported facade and owning object.
- Use the reviewer gate for each public API change: the happy path must fit one short OOP sentence, such as "create the object, then call the lifecycle verb", "build the spec from a dict, then register it", or "load the named object, then mutate or query it".
- Require a reviewer or architect justification when a new top-level function, nested helper, or constructor flag is easier to implement but harder to teach. The burden of proof is on the larger surface, not on the shorter OOP path.

## Avoid

- Parallel APIs that do the same thing.
- Constructor flags that hide follow-up actions, especially private-looking flags such as `_register_global=False`, `_set_default=True`, or `_isolated=False` in user-facing flows.
- Nested functional pipelines such as `register_x(build_x(...))` when the same flow can be `X.from_dict(...).register()`.
- Thin public classes that only rename one field.
- Public examples that force users through `pkg.ext.*`, registry internals, or helper factories before they see the core domain object.
- DSLs where dictionaries, ORM-style expressions, or ordinary Python would be clearer.

For constructor, registration, fluent-field, and data-container comparisons, read [examples](api/example.md).

## Named arguments

**Anti-pattern:** `ws.query(expr, 20, False, True)` makes the reader memorize unrelated positional meanings.

**Pattern:** `ws.query(expr, limit=limit, include_deleted=False, explain=True)` states those meanings. A signature such as `def query(self, expr, *, limit=None, include_deleted=False, explain=False)` makes optional choices keyword-only; resolve tunable omitted defaults through the config owner and use complete types/docstrings in production.
