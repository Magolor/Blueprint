---
id: ts-docs
title: TypeScript API documentation
blocking: true
description: Write semantic public TSDoc and validate API documentation.
---

# TypeScript API documentation

Published exports, stable extension seams, public functions/classes/methods, service interfaces, events, config schemas, and result types use semantic TSDoc in `/** ... */`. Follow Google TypeScript documentation conventions and the repository renderer. Types explain shape; prose explains caller-visible meaning and safe use.

- Put the comment immediately before its owning public declaration. A trivial re-export may rely on that owner's documentation.
- Lead function summaries with a verb and class/type summaries with a noun phrase. Add only details that change correct use.
- Public functions and methods have explicit return types. Document parameter/result roles, units, bounds, defaults, ownership, and side effects when the names and types do not establish them.
- Explain caller-observable thrown/rejected errors, cancellation, disposal, mutation, ordering, retry/idempotency, and concurrency guarantees where relevant.
- Public classes explain their object model and constructor/config role. Document constructor fields once.
- Use supported `@param`, `@returns`, `@throws`, and `@example` tags when they add semantics or the repository generator requires them. Do not repeat TypeScript types or copy Python `Args:` sections.
- Keep facts on their owning declaration. Private algorithms, incidental order, and historical rationale are not public guarantees. Module-level purpose comments are optional when they help consumers.

Read [semantics and tags](doc/format.md) for absence, snapshots, lifecycle, literals, or supported tags; [example](doc/example.md) for a caller-facing function; and [checks](doc/check.md) for generated docs or published-package gates. Use [implementation comments](comment.md) for internal explanation. Ordinary API edits need no documentation generator or extra gate.
