---
id: code-review
task_kind: code-review
status: active
description: Review a diff, branch, PR, module, or linked issue.
---

# Code review

Review the requested diff, files, module, branch, PR, recent commits, or linked issue. If unspecified, use staged and uncommitted changes. State the comparison base explicitly. Complete [required reading](../workflows/read.md) before judging code: the full applicable language tree and shared project rules, including nested pages. Read repository policy, nearby source, and relevant docs too.

Use [review criteria](../rules/project/review.md) as applicability questions; do not invent findings for untouched surfaces. Public surfaces include exports, package entries, CLI behavior, configurable input, interactions, tools, events, wire/file formats, and documented promises.

Recheck status and the diff before any authorized fix. Unexpected edits may belong to another person or agent; preserve them. Architecture health work without a concrete code-review target uses [design](design.md).

## Findings and follow-up

Report findings first. Each finding includes triage checkbox, severity, rule/category, file and line, problem, impact, and concrete fix direction. Add a user-annotation field when useful. With no findings, say so and state review gaps.

- P0: blocking correctness, security, or data loss.
- P1: likely bug or broken contract.
- P2: maintainability, test, or docs gap.
- P3: polish or optional cleanup.

Save a report only for an explicit request, a Linear/PR gate, or auditable follow-up; otherwise return findings inline. Default saved path: `docs/reports/reviews/<YYYY-MM-DD>-<scope>-heaven-style-review.md`, subject to repository policy. Include scope/base, evidence/commands, findings, annotations, verification gaps, and acceptance.

Completion requires confirmed P0/P1 fixes, agreed P2 fixes or waivers, relevant tests/docs/examples/generated checks, and an updated report. After a review-only request, wait for annotation before fixing; existing review-and-fix authority permits continuation.

Make external issue/comment updates only when authorized. For continuous Linear follow-up, edit one rolling status comment; use separate comments for distinct decisions, blockers, handoffs, or explicit requests.
