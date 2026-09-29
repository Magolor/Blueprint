---
name: design-philosophy-surface
description: Read before you choose public classes, methods, and user flows.
---

# Small public OOP surface

## Summary

Keep the ordinary user flow small and cohesive. Put domain behavior on objects users already know without turning unrelated responsibilities or stateless transforms into classes.

## Principle

Start with one supported import and one short ordinary flow: construct or load the domain object, then call its operation. Prefer a method or classmethod on the existing owner over a new public function, factory, wrapper, flag, or DSL. Each added public concept must remove more user complexity than it introduces.

A class earns its place through domain meaning, behavior, invariants, identity, state, or lifecycle. Do not minimize the class count by merging unrelated responsibilities into one large object. Do not maximize OOP by wrapping every value or stateless algorithm in a class. Prefer member methods wherever an existing domain object naturally owns the operation, including static construction and pure conversion. `Entity.fromJson(data)` owns entity validation; `ws.upsert(product)` owns workspace mutation. Statelessness alone does not justify a separate factory or helper API. Use native protocols and direct functions for independent transforms with no natural domain owner. Public OOP cohesion and private functional implementation can coexist.

Separate ordinary users from extension authors. Users follow domain methods; extension authors receive stable, documented contracts. Neither audience should navigate private registries or helper factories to complete its normal task.

## Least-surprise interfaces

Design a new interface from the perspective of a capable user who knows the language and domain but has no implementation background. From the surrounding API and the task description, that user should be able to predict the owning object or import, operation name, argument shape, return value, absence and failure behavior, side effects, and lifecycle. Start with the repository's established public patterns, then use language and domain conventions for choices the repository does not own.

Sketch the expected call before finalizing the signature. Ask what verb the user would try in autocomplete, which operand belongs positionally, which choices need names, what the result must contain, and whether the call reads as I/O, mutation, construction, lookup, or conversion. If a plausible expectation differs from the proposed behavior, align the interface or make the distinction explicit in its name, types, and documentation. Do not use a canonical vocabulary mechanically when its ordinary meaning would mislead users.

Least surprise applies to behavior as well as spelling. Similar operations preserve argument order, defaults, return cardinality, error and absence semantics, mutation and ownership rules, async behavior, and lifecycle expectations unless the interface makes the difference visible.

**Pattern:** Nearby lookups use `get(id)` and return an optional value without I/O. A new exact in-memory lookup follows that contract; a remote operation uses the repository's distinct retrieval verb and documented failure type.

**Anti-pattern:** Name a network request `get` because it is short, return a collection for one ID, and convert permission failures into absence even though users would infer the repository's established lookup behavior.

## Pattern and Anti-pattern

These are illustrative pseudocode, not a required API or package layout.

```text
Pattern:      project = Project.load(path); project.export(target)
Anti-pattern: loader = LoaderFactory.create(); data = loader.load(path)
              exporter = ExportManager(ExportContext(data)); exporter.run(target)
```

For one ordinary export flow, expose the domain operation. Keep internal loading and export services private unless users need their independent contracts.

```text
Pattern:      normalize(text)
Anti-pattern: TextNormalizerFactory.create().normalize(text)
```

Use a direct function for an independent stateless transform. A wrapper class adds no domain meaning here.
