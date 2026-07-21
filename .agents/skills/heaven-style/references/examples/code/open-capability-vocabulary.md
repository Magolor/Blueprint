---
id: example-open-capability-vocabulary
title: Open capability vocabulary
enabled: true
order: 10
keywords: [code smell, design smell, capability, registry, open extension, OCP, ISP, plugin architecture]
description: Read when an extensible family keeps gaining hard-coded feature fields, feature-specific methods, switches, or unvalidated extra dictionaries.
---

# Open capability vocabulary

Use this example when third parties may add new kinds of optional behavior. The design test is simple:

> Can one extension add a capability without editing the central value type or growing the base interface?

If the vocabulary is intentionally closed, use an enum, discriminated union, or exhaustive match instead. A registry is not automatically better.

## Bad smell: the extension edits the center

```python
from dataclasses import dataclass, field


@dataclass
class BackendCapabilities:
    search: bool = False
    graph: bool = False
    batch_mode: str = "none"
    extra: dict[str, object] = field(default_factory=dict)


class Backend:
    capabilities = BackendCapabilities()

    def supports_search(self) -> bool:
        return self.capabilities.search

    def supports_graph(self) -> bool:
        return self.capabilities.graph
```

Smells:

- Every new feature adds a field to one central class.
- The shared interface gains one accessor or predicate per feature.
- Serialization, cloning, docs, and inspection tend to repeat the same feature list.
- `extra` creates a second, unvalidated capability system.
- Provider-specific vocabulary leaks into the abstraction all providers inherit.

The decisive smell is change amplification: adding one optional feature forces unrelated central edits.

## Good smell: the extension supplies a descriptor

```python
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any, Generic, TypeVar


T = TypeVar("T")


@dataclass(frozen=True)
class Capability(Generic[T]):
    identifier: str
    default: T
    normalize: Callable[[object], T]
    description: str = ""

    def register(self) -> "Capability[T]": ...


class CapabilityValues:
    def __init__(
        self,
        values: Mapping[str | Capability[Any], object] | None = None,
    ) -> None: ...

    def get(self, key: Capability[T]) -> T: ...


class Backend:
    declared = CapabilityValues()

    def capability_overrides(self) -> Mapping[str, object]:
        return {}

    def capability(self, key: Capability[T]) -> T: ...

    def supports(self, key: Capability[bool]) -> bool:
        return self.capability(key)
```

An extension declares its own vocabulary and data:

```python
def require_bool(value: object) -> bool:
    if type(value) is not bool:
        raise TypeError("expected bool")
    return value


SEARCH = Capability(
    "search",
    False,
    require_bool,
    "Whether search is complete and native.",
).register()


class SearchBackend(Backend):
    declared = CapabilityValues({SEARCH: True})
```

Good smells:

- The base protocol stays small: generic read, Boolean support, and runtime override hooks.
- One descriptor owns identity, defaulting, validation, documentation, and serialization policy.
- Static declarations are data; live facts use one generic override mapping.
- Consumers depend on the descriptor they understand, not on provider names.
- A structured capability can use its own focused immutable value type without closing the whole vocabulary.
- Inspection can publish descriptor definitions separately from resolved instance values.

## Review heuristic

For an open extension family, trace the smallest plausible new capability.

- **Bad smell:** it modifies a central dataclass, base method list, provider switch, serializer list, and metadata list.
- **Good smell:** it registers one descriptor, declares or overrides one value, and updates only the consumer that understands it.

Prefer the good-smell shape only when independent extensions genuinely own new identifiers. Keep closed domains closed.
