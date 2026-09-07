---
id: model
title: Mental model
blocking: true
description: Minimize Python public APIs and choose owning objects or functions.
---

# Mental model

## Core rule

Keep the public OOP interface as small as possible. For each feature, expose the shortest flow through its owning object. Classmethods create or load objects. Instance methods perform lifecycle actions. Common code reads as `obj = Class(...); obj.verb()` or `Class.from_dict(...).verb()`. Do not introduce public classes, free functions, constructor flags, or DSL syntax unless they remove real complexity for users.

## Do

- Prefer existing object methods or classmethods over parallel free functions.
- Put behavior on the object that owns the state: `from_dict`, `from_schema`, and `load` create or reopen objects; `register`, `set_default`, `verify`, `connect`, and `close` act on those objects.
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
