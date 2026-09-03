---
id: review
title: Review checklist
enabled: true
blocking: true
order: 470
category: project
keywords: [pr gate, code review, style review, inline comments, findings, approval, review criteria]
description: Use for PR, diff, module, branch, or Linear review, severity-marked findings, review artifacts, follow-up, or explicit waivers.
---

# Review checklist

## Core rule

Use this rule for reviews of code changes, recent changes, branches, modules, PRs, or Linear issues. The task playbook is [../../tasks/code-review.md](../../tasks/code-review.md).

Reviews are findings-first, severity-marked, and grounded in file/line evidence whenever possible.

Apply this checklist to every code review. Treat each criterion as an applicability question. Do not create a finding only because the change does not touch a listed surface.

## Apply when

- The task asks for review, PR review, diff review, recent-change review, branch review, module review, or Linear issue review.
- A change needs an explicit completion gate or waiver record.

## Do

- Lead with findings ordered by severity.
- Include file/line references whenever available.
- Re-check the diff before fixing findings because the working tree may change.
- State verification commands and residual risk.

## Avoid

- Leading with a summary before findings.
- Reverting unrelated changes.
- Treating style preferences as bugs without concrete impact.

## Criteria

- **Code quality:** Heaven architecture, repository conventions, and the matched language rules for utilities, configuration, types, naming, and public API shape.
- **First principles:** test the change against the verified user need, real constraints, and declared compatibility promises; question inherited assumptions or workaround-shaped behavior that no longer has evidence.
- **Modularity:** clean boundaries, clear ownership, layering, registries for genuinely open extensions, and exhaustive variants for closed protocols rather than central shortcuts.
- **Simplicity:** keep behavior, implementation, and public surface as small as the verified need allows; avoid boilerplate, duplicated branches, over-abstracted helpers, unnecessary files, and interfaces without a current consumer need.
- **Public interface:** check exported code, package entries, CLI behavior, user-configurable input, user interactions, tools, events, wire/file formats, and documented promises when the change touches them.
- **Ease of use:** straightforward mental model for users and developers; no parallel APIs, confusing flags, or alternate-name-heavy surfaces.
- **Cleanliness:** no ad-hoc hacks, unapproved compatibility leftovers, dead code, debug prints, stale placeholders, or unused artifacts.
- **API documentation:** public surfaces follow the matched language documentation rule: TypeScript uses [TypeScript API documentation](../code/typescript/docs.md), while Python uses [docstring](../code/python/docstring.md).
- **Robustness:** invalid input, security issues, unowned promises, corner cases, swallowed errors, resource leaks, races, and unsafe fallbacks are handled.
- **Migration alignment:** follow the repository's recorded release/compatibility policy. TypeScript uses [TypeScript compatibility](../code/typescript/compat.md); Python uses [Python compatibility](../code/python/compat.md), including predecessor migrations when relevant.
- **Sync:** tests, user/engineering docs, architecture current/target/gap status, generated artifacts, rule examples, development-log evidence, scratch cleanup, the one canonical task queue, and authorized external mirrors match the code.

## Severity

- `P0`: blocking correctness, security, data loss, or deployability issue.
- `P1`: likely bug, broken public contract, missing critical validation, or serious test/doc mismatch.
- `P2`: maintainability, modularity, coverage, API-documentation, or sync issue that should be addressed before declaring done.
- `P3`: polish, naming nuance, optional cleanup, or future improvement.

## Finding Template

```text
- [ ] P1 `configuration` `test` path/to/file:42
  Problem: A deployable default is hard-coded outside the repository's configuration owner and has no failure-path test.
  Impact: Downstream deployments cannot override it consistently and regressions are hard to catch.
  Fix: Route the default through the repository configuration owner and add happy/edge/failure coverage.
  User annotation:
```

## Output Rules

- Lead with findings, ordered by severity.
- Include file/line references whenever available.
- Assume the working tree may change while you review. Re-check the diff before fixing findings, preserve unrelated external edits, and call out when a finding may have already been addressed by parallel work.
- Save review reports with checkboxes and user annotation fields when the task asks for a durable review.
- For Linear-backed review follow-up, edit one rolling status/review comment for routine updates instead of creating repeated comments.
- State verification commands run and any gaps.
- If no findings exist, say so directly and name residual risk.

## Related rules

Apply all matched code/project rules for the reviewed diff, including [environment.md](environment.md) for verification-command policy. Use [../../tasks/code-review.md](../../tasks/code-review.md) for durable review workflow.
