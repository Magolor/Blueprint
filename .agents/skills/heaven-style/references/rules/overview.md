---
id: overview
title: Rule overview
blocking: true
description: Check required language rules and shared design contracts.
---

# Rule map

Before any code-related task, read every rule in the applicable language column and every nested Markdown file in that language tree. Read all shared project rules recursively and the [design philosophy](../design/philosophy.md). This map is a checklist, not a menu. Use both language trees when the task spans both. Repository policy wins; the Markdown owner defines behavior, while metadata supports lookup. Checked JavaScript uses relevant TypeScript rules only under an explicit checking or migration policy.

| Topic | TypeScript | Python |
| --- | --- | --- |
| Public API shape | [API](code/typescript/api.md) | [API](code/python/api.md) |
| Operation vocabulary | [Verbs](code/typescript/verbs.md) | [Verbs](code/python/verbs.md) |
| SOLID and boundaries | [SOLID](code/typescript/solid.md) | [SOLID](code/python/solid.md) |
| Types and input | [Types](code/typescript/types.md) | [Types](code/python/types.md) |
| Configuration | [Config](code/typescript/config.md) | [Config](code/python/config.md) |
| Utilities | [Util](code/typescript/util.md) | [Util](code/python/util.md) |
| Files and packages | [Files](code/typescript/files.md) | [Files](code/python/files.md) |
| Names | [Names](code/typescript/name.md) | [Names](code/python/name.md) |
| Clean and flow | [Flow](code/typescript/flow.md) | [Flow](code/python/flow.md), [helpers](code/python/clean.md) |
| API documentation | [TSDoc](code/typescript/doc.md) | [Docstrings](code/python/doc.md) |
| Implementation comments | [Comments](code/typescript/comment.md) | [Comments](code/python/comment.md) |
| Failures and lifetime | [Errors](code/typescript/error.md), [async](code/typescript/async.md) | [Errors](code/python/error.md) |
| Database access | [SQL](code/typescript/sql.md) | [SQL](code/python/sql.md) |
| Compatibility | [Compat](code/typescript/compat.md) | [Compat](code/python/compat.md) |
| Toolchain | [Environment](code/typescript/env.md) | [Environment](project/environment.md) |

Shared decisions: [interfaces](project/interfaces.md), [extensions](project/extension.md), [tests](project/test.md), [formatting](project/format.md), [review](project/review.md), [documentation](project/docs.md), and [shell commands](project/environment.md).

Keep language mechanics native: TSDoc tags versus Google sections, JavaScript protocols versus dunder methods, ESM exports versus Python facades/stubs. Shared intent does not require identical syntax or an extra rule file.

For GUI work read [style](../design/gui/style.md) and the complete GUI tree. For task or failure routing use [tasks](../workflows/start.md) or the [index](../index.yaml); do not load the full catalogs.
