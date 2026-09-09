---
name: review
description: Apply evidence-based review criteria, severity, and finding format.
---

# Review checklist

## Summary

Use this rule for reviews of code changes, recent changes, branches, modules, PRs, or Linear issues. The task playbook is [review](../../tasks/review.md).

## Principle

Open reviews with a Summary stating the finding conclusion. Put detailed findings next and mark their severity. Support them with file/line evidence whenever possible.

Apply this checklist to every code review. Treat each criterion as an applicability question. Do not create a finding only because the change does not touch a listed surface.

## Apply when

- The task asks for review, PR review, diff review, recent-change review, branch review, module review, or Linear issue review.
- A change needs an explicit completion gate or waiver record.

## Do

- Put detailed findings immediately after the opening Summary, ordered by severity.
- Include file/line references whenever available.
- Re-check the diff before fixing findings because the working tree may change.
- State verification commands and residual risk.

## Avoid

- Opening with generic reassurance or background that delays the finding conclusion.
- Reverting unrelated changes.
- Treating style preferences as bugs without concrete impact.

## Criteria

- **Code quality:** Heaven architecture, repository conventions, and the matched language rules for utilities, configuration, types, naming, and public API shape.
- **First principles:** test the change against the verified user need, real constraints, and declared compatibility promises. Question inherited assumptions or workarounds that no longer have supporting evidence.
- **Modularity:** clean boundaries, clear ownership, layering, registries for genuinely open extensions, and exhaustive variants for closed protocols rather than central shortcuts.
- **Simplicity:** keep behavior, implementation, and public surface as small as the verified need allows. Avoid boilerplate, duplicated branches, over-abstracted helpers, unnecessary files, and interfaces without a current consumer need.
- **Public interface:** check exported code, package entries, CLI behavior, user-configurable input, user interactions, tools, events, wire/file formats, and documented promises when the change touches them.
- **Ease of use:** straightforward mental model for users and developers; no parallel APIs, confusing flags, or alternate-name-heavy surfaces.
- **Cleanliness:** no ad-hoc hacks, unapproved compatibility leftovers, dead code, debug prints, stale placeholders, or unused artifacts.
- **API documentation:** public surfaces follow the matched language documentation rule: TypeScript uses [TypeScript API documentation](../code/typescript/doc.md), while Python uses [docstring](../code/python/doc.md).
- **Robustness:** invalid input, security issues, unowned promises, corner cases, swallowed errors, resource leaks, races, and unsafe fallbacks are handled.
- **Migration alignment:** follow the repository's recorded release/compatibility policy. TypeScript uses [TypeScript compatibility](../code/typescript/compat.md); Python uses [Python compatibility](../code/python/compat.md), including predecessor migrations when relevant.
- **Sync:** tests, user/engineering docs, architecture current/target/gap status, generated artifacts, rule examples, development-log evidence, scratch cleanup, the one canonical task queue, and authorized external mirrors match the code.

## Severity

Use the repository’s severity scale when declared. Otherwise use this five-tier scale. Classify by demonstrated impact, affected users, likelihood, and recovery cost—not the effort to fix it or the number of review rounds. State uncertainty separately from severity.

| Severity | Meaning | Disposition |
| --- | --- | --- |
| P1 — Critical | Credible severe security exposure, data loss, widespread outage, or inability to deploy or use the core system. | Immediate blocker; resolve before acceptance. |
| P2 — Major | A supported feature or public contract fails under realistic conditions, with substantial user impact or no reasonable workaround. | Resolve before acceptance. |
| P3 — Material | A bounded defect, misleading documentation, meaningful coverage gap, or maintainability problem with concrete recurring cost. | Fix in scope or obtain an explicit owner-approved waiver. |
| P4 — Minor | Local clarity, consistency, or usability improvement with low impact; current behavior remains usable and understandable. | Optional; does not block completion. |
| P5 — Negligible | Cosmetic preference or speculative refinement with no demonstrated practical impact. | Normally omit; almost always ignorable. |

An unclear name alone is P4/P5; a misleading name that causes callers to misuse a consequential operation can be P3 or higher. A critical fact omitted from docs is not minor merely because the fix is prose. When reporting into a different host scale, declare the mapping rather than silently reusing a label with another meaning.

## Finding Template

Keep a triage checkbox and an explicit Severity on each issue. Include category, location, problem, impact, and fix direction. Add user annotation space for durable reviews.

```text
- [ ] Configuration cannot be overridden through its declared owner
  Severity: P2 — Major
  Category: configuration, test
  Location: path/to/file:42
  Problem: Execution reads a fixed deployable default outside the configuration owner.
  Impact: Supported deployments cannot select their required configuration.
  Fix: Consume the validated setting from its owner and verify the override path.
  User annotation:
```

## Repeated-review completion

Review against the agreed scope and current revision. Resolve confirmed P1–P3 findings, or record an explicit waiver from the authorized owner under repository policy. Verify affected fixes and required gates. Do not downgrade a finding to end the loop or classify an unverified risk as cosmetic.

Finish when the agreed review coverage and checks are complete and all remaining findings are P4/P5. Report “Complete; only non-blocking suggestions remain” with any verification limits or waivers. Stop generating cleanup work merely to reach zero suggestions. Reopen the review only for material changes, new evidence, or an expanded scope. Missing required evidence remains a gap, not a P4/P5 pass.

## Output Rules

- State the finding conclusion in Summary, then list findings ordered by severity.
- Include file/line references whenever available.
- Assume the working tree may change while you review. Re-check the diff before fixing findings. Preserve unrelated external edits. State when parallel work may have already addressed a finding.
- Save review reports with checkboxes and user annotation fields when the task asks for a durable review.
- For Linear-backed review follow-up, edit one rolling status/review comment for routine updates instead of creating repeated comments.
- State verification commands run and any gaps.
- If no findings exist, say so directly and name residual risk.
