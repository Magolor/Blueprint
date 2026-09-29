---
name: task-triage
description: Read before accepting review findings for a fix round.
---

# Triage findings

## Summary

Confirm that a finding describes a real, material problem under supported conditions before assigning a fix. A reviewer’s report is evidence to assess, not an automatic implementation mandate.

## Procedure

Recheck the current candidate and the finding’s location, contract, trigger, impact, and verification evidence. Reproduce the failure when practical; otherwise establish the failing path from authoritative code or documentation. Separate pre-existing issues from regressions and preserve relevant uncertainty.

Classify each finding as confirmed, duplicate, rejected with evidence, or unresolved with the missing evidence. Apply the [severity scale](../rules/project/review.md#severity). Judge actual exposure and consequences: a rare supported failure with severe impact may matter, while a hypothetical invalid internal state may not justify defensive machinery.

Assess the issue and its proposed remedy separately. A real defect can have a bad suggested fix. Retain the confirmed finding while replacing a remedy that special-cases one sample, adds speculative guards, or duplicates policy. Use [address issues](address.md) for confirmed, authorized changes at the owning boundary.

For each finding, answer: does it still occur on this candidate; which supported contract fails; what demonstrates the trigger and consequence; and is the proposed correction proportional? Check for an existing mechanism before proposing another. “Already fixed” needs evidence from the current path, not merely a similarly named helper.

For example, an alias proposed to repair an owned caller after an accepted rename is not the only remedy. Confirm the broken caller, then migrate it to the canonical entry under the compatibility rule. Rejecting the alias does not dismiss the caller defect.

## Acceptance

Every finding has a supported disposition, severity, and fix direction or evidence gap. Disagreement alone does not dismiss a finding, and round pressure does not lower severity. Keep this disposition in the existing review record.
