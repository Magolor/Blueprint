# Code-style decisions

## Summary

Apply the maintainer's decisions to the legacy drift survey: paired vocabulary and aliases, domain-owned APIs, shared utilities, logical guards, stable-prefix imports, ORM-first SQL, named arguments, and compact code. Preserve modern typing, full Python docstrings, one live API, and TypeScript's declared runtime/import controls.

- Status: Done
- Created: 2026-09-09
- Task: STYLE-003
- Scope: Heaven Style rules and decision-survey closeout

## Steps

1. Align code rules, examples, catalogs, and vocabulary folders for both languages.
2. Record accepted, revised, retained, and unresolved survey outcomes.
3. Validate rules/index and both product gates, synchronize branches, and reinstall.

## Closeout

Completed the [recorded decisions](../reports/surveys/2026-09-09-code-style-drift-survey.md). Both branches share the exact 207-file skill tree; full gates passed (16 TypeScript tests and packed consumer; 44 Python tests). Skill validation/index checks passed and the global installation was refreshed. STYLE-003 was removed from the queue. TypeScript logging and tool selection remain repository-owned pending a separate decision.
