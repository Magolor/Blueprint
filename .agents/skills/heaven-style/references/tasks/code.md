---
id: code
task_kind: code
status: active
enabled: true
order: 10
keywords: [implement feature, fix bug, modify code, refactor code, add tests, update docs, linear issue, stabilize]
triggers: [implement, fix, code, refactor, add feature, change behavior, stabilize, TAL]
description: Use when implementing Heaven-style features, fixes, refactors, tests, docs, or stabilization work.
related_rules: [overview, ts-util, ts-architecture, ts-api, ts-types, ts-config, ts-modules, ts-async, ts-sql, ts-docs, ts-compat, ts-environment, util, config, types, docstring, oop, model, solid, name, files, py, clean, error, sql, compat, environment, format, test, docs, extension, interfaces]
---

# Code Task

## Goal

Ship a small or medium code change in Heaven style without loading the full rule tree unless the change needs it.

Select rules by language: `ts-*` IDs and Python IDs are alternatives unless the change crosses a real TypeScript/Python boundary. For a new or unspecified project, start from TypeScript; preserve the declared language of an existing repository. Project rules apply to both but defer mechanics to the matched language environment.

## Fast Path

1. Read the user request, repo `AGENTS.md`, its canonical task queue, the project `environment` rule, target language/environment rules, declared lint/test entrypoints, docs authority map, and nearby source before editing.
2. If a Linear issue, plan file, or previous review is named, read it and extract objective, scope, acceptance criteria, open questions, and status.
3. Brainstorm only when the design is under-specified. Prefer one recommended approach with tradeoffs; then detail the accepted plan.
4. Claim an existing queue item or add one when the work is resumable, multi-slice, blocked, or independently delegated. Define the behavior change, public API impact, data/storage impact, docs/example impact, test surface, and non-goals without copying the plan into the queue.
5. For small local changes, use `SKILL.md` plus only directly matched rules from `references/rules/overview.md`.
6. For public APIs, shared utilities, storage/query layers, extension points, or cross-module refactors, load `references/workflows/developer.md` and the relevant rules before editing.
7. Apply minimal diffs using existing project patterns. Internal break-and-fix updates all owned call sites; published compatibility follows the repository policy, and any migration shim needs a named consumer and removal condition.
8. Exercise the feature with a quick probe, smoke path, or demo before broader validation when the behavior is user-facing or integration-heavy.
9. Add or update tests for the happy path, one edge case, and one error path when behavior changes. Add a short demo when the repo requires one.
10. Review the diff against Heaven-style criteria, fix confirmed issues, and repeat targeted tests as needed.
11. Run the target repository's declared style, lint, typecheck, test, build/package, and aggregate gates through `rtk`. TypeScript preserves its checked-in manager/scripts and uses `ts-environment`; Python uses its declared wrappers and environment owner.
12. Sync user-facing docs, engineering current/target/gap status, sibling docs repos, generated capability docs, examples, the development log, scratch cleanup, and task/issue state when the code changes their claims.
13. For Linear-driven work, edit the issue's existing rolling status comment for routine progress, verification, and next steps. Add a new comment only for a distinct decision, blocker, handoff, or user-requested update.

## Coding Criteria

- Code quality: follow Heaven architecture, repo guidance, and the matched language rules. TypeScript uses strict boundaries, repository-owned platform/config layers, and explicit package/runtime contracts; Python uses the repository's declared utility/config/database/error owners or direct Python APIs when none exists.
- Modularity: put state/lifecycle on its owning object, keep stateless transforms as functions, preserve dependency direction, register open extension families, and handle closed variants exhaustively.
- Brevity: prefer the smallest readable implementation; remove boilerplate, redundant helpers, and repeated branches.
- Ease of use: keep public mental models straightforward for users and maintainers; avoid unnecessary classes, modes, flags, or DSL branches.
- Cleanliness: remove ad-hoc code, dead code, stale TODOs, debug prints, unapproved or expired compatibility leftovers, and unused artifacts.
- API documentation: TypeScript published exports and stable seams follow `ts-docs`; Python public APIs follow `docstring`. Do not impose one language's comment format on the other.
- Robustness: validate untrusted boundaries, use contextual failures, avoid swallowed errors or unowned promises, and cover corner/lifecycle paths.
- Compatibility: follow the repository's public compatibility policy. TypeScript uses [ts-compat](../rules/code/typescript/compat.md); Python uses [compat](../rules/code/python/compat.md), including predecessor migrations when relevant.
- Sync: docs, examples, generated files, architecture notes, sibling docs repos, and Linear issue state must match the implementation when relevant.

## Completion Gate

Do not mark done until the implementation, tests, review, repository static/format gates, docs/example sync, generated artifacts, development-log evidence, scratch cleanup, queue closeout, issue updates, and final human report are either completed or explicitly waived with the reason.

## Output

Report what changed by rule/category, which verification commands ran, and any risks or explicit waivers.
