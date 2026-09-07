---
id: py-verbs-value
title: Python value operations
description: Read for Python value operations.
---

# Python value operations

## Serialization and files

Use utility verbs for raw formats:

| Concept | Canonical |
| --- | --- |
| String/bytes conversion | `loads_*`, `dumps_*` |
| File conversion | `load_*`, `dump_*`; object artifact output may use `save(path)` |
| Path constructors | `from_path`, `from_file` |

Avoid `serialize`, `deserialize`, `toJSON`, and ad-hoc file verbs.

Use `save(path)` only for writing a file/artifact owned by the object, such as `LLMImage.save(path)`, or a future `Capsule.save(path)`. Do not use `save` for database rows, registries, workspace registration, or config writes that already persist immediately.

## Exportable objects

| Concept | Canonical |
| --- | --- |
| Build from mapping | `from_dict(cls, data, ...)` |
| Compile class/type from schema | `from_schema(cls, spec, ...)` |
| Export mapping | `to_dict(self)` |
| Copy with patch | `clone(self, **updates)` |
| Class-level retrieval | `load(cls, key=None, ...)` |
| Display | `to_str`, `__str__` delegates to `to_str` |
| UI/API projection | `to_view` |

Use `from_dict` for object/row instances built from data. Use `from_schema` when the input describes a class/type/schema rather than one row, for example `pkg.Entity.from_schema({...})`.

Use `load` as the class-level retrieval verb for public objects that can be reopened from a registry, cache, store, or configured default, for example `Project.load("shop")`, `Prompt.load("name")`, or `BackendType.load("sqlite")`. If a class supports both registry lookup and file loading, make file loading explicit with `path=`/`file=` or `from_path`/`from_file`. Never infer registry-versus-file meaning from a bare string.

## Example

**Anti-pattern:**

```python
class Row:
    def as_dict(self):
        return dict(self._data)

    def fetch(self, key):
        return self._data[key]
```

**Recommended pattern:**

```python
from typing import Any

class Row:
    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Row":
        return cls(data)

    def to_dict(self) -> dict[str, Any]:
        return dict(self._data)

    def clone(self, **updates: Any) -> "Row":
        return type(self)({**self._data, **updates})

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)
```
