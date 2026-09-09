---
name: template-review
description: Read before writing a code, architecture, or documentation review.
---

# Review

## Summary

Summarize the verdict, affected capability, and most consequential finding.
If none are actionable, say so without implying exhaustive proof. Use the
repository's review metadata and severity convention.

## Findings

For each finding, explain the trigger, expected versus actual behavior,
consequence, location, and suggested action. Introduce symbols through their
role. Use a triage checkbox, explicit `Severity: P1–P5` under the [severity contract](../../references/rules/project/review.md#severity), category, location, problem, impact, and fix direction. Follow a declared repository scale instead when required. Add annotation space for a durable review. Separate verified defects, hypotheses, and optional suggestions.

## Scope and evidence

Locate the system responsibility and review question. Identify the exact
revision or comparison and the sources, tests, or behavior actually inspected.

## Verification and next steps

State checks run, results, limits, and unresolved decisions. Static inspection
is not runtime validation. Link follow-up to its existing owner and identify
changes that would make this review stale. Apply the [review stopping condition](../../references/rules/project/review.md#repeated-review-completion); P4/P5-only suggestions do not require another round after scope and checks are complete.

## References

Link reviewed revisions, canonical contracts, and supporting evidence.
