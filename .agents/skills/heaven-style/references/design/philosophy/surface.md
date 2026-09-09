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
