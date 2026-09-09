---
name: name
description: Name Python symbols and modules with consistent domain vocabulary.
---

# Names

## Summary

Names should be short enough to keep frequently read code readable and precise enough to preserve meaning. Use one word per concept. Explain new abbreviations in the change that introduces them.

## Do

- Keep frequently used symbols short. Leaf helpers may have longer names.
- `snake_case` functions/modules/vars; `PascalCase` classes; `SCREAMING_SNAKE_CASE` for module constants and established config-manager singletons such as `CM_*`. Keep that existing Python convention without imposing it on new TypeScript config services.
- Verb-first: `load_json`, `parse_spec`; registration helpers may read like `# pseudocode: register_handler(...)`.
- Predicates: `is_*`, `has_*`, `can_*`.

## Avoid

- Type suffixes such as `user_list`.
- Invented abbreviations without a local glossary.
- Redundant phrases like `database_connection_object_list`.

## Example

**Anti-pattern:**

```python
database_connection_object_list = load_database_connections()
```

**Recommended pattern:**

```python
dbs = load_dbs()
```

Names should be brief whenever possible. Carefully re-examine any snake-case name with 3 or more parts. Consider renaming it unless there is a good reason to keep it.

## Shared abbreviations

| Long | Short |
| --- | --- |
| Path join | `pj` |
| Database | `db` |
| Embedding | `emb` |
| Count / limit | `n_*`, `max_*` |
| Specification | `*Spec` |

Invented abbreviations belong in the same PR that introduces them. Framework-specific glossaries live in reference assets when needed.

Use the [vocabulary](vocab.md) for canonical nouns, paired verbs, and supported aliases.
