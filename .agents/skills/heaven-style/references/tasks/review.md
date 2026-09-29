---
name: code-review
description: Read before reviewing code, a branch, or a pull request.
task_kind: code-review
status: active
---

# Code review

## Summary

Review the declared comparison with evidence-based findings and explicit verification gaps.

## Scope and prerequisites

Review the requested diff, files, module, branch, PR, recent commits, or linked issue. If unspecified, use staged and uncommitted changes. State the comparison base explicitly. Complete [required reading](../rules/project/read.md) before judging code: the full applicable language tree and shared project rules, including nested pages. Read repository policy, nearby source, and relevant docs too.

Use [review criteria](../rules/project/review.md) as applicability questions; do not invent findings for untouched surfaces. Public surfaces include exports, package entries, CLI behavior, configurable input, interactions, tools, events, wire/file formats, and documented promises.

Recheck status and the diff before any authorized fix. Unexpected edits may belong to another person or agent; preserve them. Architecture health work without a concrete code-review target uses [design](design/README.md).

## Findings and follow-up

Start with a Summary stating the finding conclusion, then report detailed findings. Each finding includes triage checkbox, severity, rule/category, file and line, problem, impact, and concrete fix direction. Add a user-annotation field when useful. With no findings, say so and state review gaps.

Use the canonical [severity scale and finding format](../rules/project/review.md#severity). Every issue carries an explicit Severity; do not maintain a separate scale here.

Save a report only for an explicit request, a Linear/PR gate, or auditable follow-up; otherwise return findings inline. Default saved path: `docs/reports/reviews/<YYYY-MM-DD>-<scope>-heaven-style-review.md`, subject to repository policy. Include scope/base, evidence/commands, findings, annotations, verification gaps, and acceptance.

Use the [repeated-review completion rule](../rules/project/review.md#repeated-review-completion): resolve or explicitly waive P1–P3, complete required checks, and stop when only P4/P5 suggestions remain. Update the report with evidence and limits. After a review-only request, wait for annotation before fixing; existing review-and-fix authority permits continuation.

Make external issue/comment updates only when authorized. For continuous Linear follow-up, edit one rolling status comment; use separate comments for distinct decisions, blockers, handoffs, or explicit requests.
