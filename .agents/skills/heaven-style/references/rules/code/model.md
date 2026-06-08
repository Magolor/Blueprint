---
id: model
title: Mental model
enabled: true
blocking: true
order: 35
category: code-quality
keywords: [api surface, class count, function count, DSL, user model, interface design, abstraction]
description: Use when adding public classes or functions, designing a user-facing surface, choosing method versus free function, or proposing a DSL.
---

# Mental model

## Core rule

Keep the public OOP interface as small as possible. For each functionality, aim for the cleanest user mental model, preferably three or fewer core classes. Do not introduce new public classes, functions, or DSL syntax unless they remove real complexity for users.

## Apply when

- Code adds public classes, functions, modules, decorators, DSL syntax, or user-facing data structures.
- A feature can be represented as either an object method, classmethod, free function, or new wrapper class.
- A proposed abstraction adds a new concept users must learn.

## Do

- Prefer existing object methods or classmethods over parallel free functions.
- Prefer familiar Python protocols and industrial interfaces over invented mini-languages.
- Keep one clear data container with structured attributes when extra wrapper classes add no behavior.
- Use dedicated classes only for behavior, invariants, lifecycle, or recognized domain concepts.

## Avoid

- Parallel APIs that do the same thing.
- Thin public classes that only rename one field.
- DSLs where dictionaries, ORM-style expressions, or ordinary Python would be clearer.

Prefer:

1. Existing object methods or classmethods over parallel free functions.
2. Built-in Python protocols and familiar industrial interfaces over invented syntax.
3. One clear data container with structured attributes over multiple thin wrapper classes.
4. MongoDB-style query dictionaries or Python ORM-style expressions over custom mini-languages when those standards fit.

## Anti-pattern

```python
class EntityRegistry:
    def register_entity(self, entity: type["Entity"]) -> None: ...

def register_entity(entity: type["Entity"]) -> None: ...

class MetadataAttribute: ...
class Metadata: ...
class Data: ...
```

## Good pattern

```python
class Entity:
    @classmethod
    def register(cls) -> None: ...

class Data:
    metadata: dict[str, object]

value = data.metadata["attr"]
```

Use a dedicated class only when it carries behavior, invariants, lifecycle, or a widely recognized domain concept. If the class only names one field, keep it as a field.

## Related rules

Also apply [oop.md](oop.md) for method vocabulary, [name.md](name.md) for symbols, [types.md](types.md) for public contracts, and [clean.md](clean.md) for helper abstraction costs.
