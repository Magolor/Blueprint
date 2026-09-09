---
name: python-vocab-aliases
description: Read before adding Python API or CLI aliases.
---

# Canonical names and aliases

## Summary

Recommend one full canonical name per meaning and maintain a small explicit set of common aliases. Aliases are alternate spellings of one live API, not parallel implementations or old-version compatibility shims.

| Canonical | Common alias | Scope |
| --- | --- | --- |
| `remove` | `rm`, sometimes `delete` | Member removal; use delete only when the exact same contract applies. |
| `delete` | `del`, sometimes `rm` | Existing deletion/native API or CLI spelling; do not overload an alias with different effects. |
| `list` | `ls` | CLI/interactive listing when the package offers the alias. |
| `config` | `cfg` | CLI/config command or short binding; configuration remains a KV service. |
| `toJson`, `fromJson` | `toJSON`, `fromJSON` | TypeScript JSON-shaped conversion; uppercase names have identical behavior, and toJSON preserves the JavaScript hook. |

The table defines recognized choices, not a requirement to expose every alias on every class. Official docs and examples recommend the canonical spelling. Every exposed alias shares validation, values, errors, side effects, ownership, and permission/transaction semantics with its target. Keep alias normalization in one registry/dispatch owner. Detect collisions rather than letting registration order pick a meaning.

Use full names in generated help and expose aliases beside them. CLI kebab-case and language casing can differ without changing vocabulary. Respect syntax: `del` is a Python keyword and cannot be a normal Python method declaration; it can be a CLI alias. TypeScript `delete` remains native on Map/Set. Do not force native APIs to rename themselves.

**Pattern:** `remove` and `rm` dispatch to the same member-removal operation with the same result and errors.

**Anti-pattern:** `rm` drops a table while `remove` deletes one row, or an alias forwards to a second implementation with different defaults.

See [verbs](verbs.md) for paired semantics and [nouns](nouns.md) for normalized provider and identity names.
