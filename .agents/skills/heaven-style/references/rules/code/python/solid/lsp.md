---
name: python-solid-lsp
description: Read when applying liskov substitution to Python object and dependency boundaries.
---

# LSP: Liskov substitution

## Summary

Every implementation must preserve the behavior callers were promised, not just satisfy a type signature.

## Rule

Substitution covers defaults, missing values, validation, errors, mutation, lifecycle, and resource ownership. A subclass or structural implementation cannot silently narrow valid input, mutate caller-owned values, weaken durability, or turn a documented miss into an exception.

- State preconditions and postconditions on the common contract.
- Give stronger or different behavior a distinct operation with the canonical domain vocabulary.
- Do not advertise an optional capability to justify violating a required base method; segregate that capability instead.

## Pattern and Anti-pattern

These are illustrative API sketches. Domain types, package-owned utilities, configuration, composition, and unrelated method bodies are omitted. Production public methods also follow the language's annotation and documentation rules.

**Anti-pattern:**

```python
class Store:
    def get(self, key: str, default: str | None = None) -> str | None:
        return default

class DictStore(Store):
    def get(self, key: str, default: str | None = None) -> str | None:
        return self._data[key]  # Raises on a miss instead of returning default.
```

**Recommended pattern:**

```python
class DictStore(Store):
    def get(self, key: str, default: str | None = None) -> str | None:
        return self._data.get(key, default)
```

The same caller can use every Store without learning implementation-specific absence rules. Run shared behavior checks for actual implementations, including missing keys and empty values; static assignability alone cannot prove substitutability.

## Review

Run the same contract against each actual implementation. Include missing and falsy values, invalid input, caller-owned input mutation, failure propagation, and lifecycle promises that the interface declares. A subtype must not require callers to branch on its concrete name.

Read the other [SOLID principles](../solid.md) together: shrinking the public mental model must preserve independent internal responsibilities.
