---
name: workflow-extensive-review
description: Use for repeated independent review, issue validation, fixes, and convergence.
---

# Extensive Review

## Summary

Review a concrete candidate, validate each finding, fix material issues, and repeat until the result converges or the round budget ends. Preserve independence and evidence throughout the loop.

## Inputs and budget

State scope, comparison base, candidate revision, required checks, fix authority, and the reviewer/implementer owners. Use an independent reviewer when authorized and available; provide the exact candidate and linked context. The same author rereading their work is self-review, not independent review. If independence is required but unavailable, report that gap and complete useful checks without claiming the requirement passed.

Use the user’s or repository’s round limit. Otherwise default to **three rounds**; use **five** for broad scope when justified at the start. This is a manual execution budget, not a validator or background schedule. One round includes review, triage, fixes, and verification. Use one review record; preserve dispositions rather than creating a new report for each round.

## Round

1. **Review:** run the [review task](../tasks/review.md) against the candidate. The independent reviewer inspects code and evidence, applies P1–P5 severity, and reports material findings and verification gaps.
2. **Validate:** [triage](../tasks/triage.md) every finding. Confirm a real supported failure or recurring cost; distinguish duplicates, speculative defenses, and optional style. Judge the finding separately from its proposed fix. A rare but severe supported failure still matters. Record rejection evidence and unresolved uncertainty.
3. **Fix:** [address](../tasks/address.md) confirmed P1–P3 issues within authority. Use a general correction at the owning boundary with minimal coherent changes. Do not add a special case or speculative scaffolding merely to satisfy a review comment. P4/P5 changes are optional and must justify their cost.
4. **Verify and align:** have the reviewer verify fixes. Run affected checks and required gates. [Sync](../tasks/sync/README.md) canonical docs and devlog evidence; use [Document](document.md) when needed. Integrate or rebase only when necessary under repository policy, then verify the resulting candidate.
5. **Decide:** apply the [completion rule](../rules/project/review.md#repeated-review-completion). If material changes or findings remain, start the next round against the updated revision within the budget. Reuse unchanged evidence; do not repeat unrelated expensive checks without cause.

## Acceptance and stopping

Converge when agreed coverage and required checks are complete and only P4/P5 suggestions remain, with explicit authorized waivers recorded under policy. Stop early once this holds. Do not invent cleanup to reach zero findings or downgrade issues to end the loop.

At the round limit, stop the loop and report the actual state: completed if acceptance holds, otherwise incomplete with remaining severity, evidence gaps, and a concrete next decision or task. Do not silently extend the limit or treat exhaustion as a pass. For review-only authority, deliver findings and the proposed fix scope rather than editing. Material changes after convergence reopen only the affected review scope.

For example, a passing build does not close a finding about the installed application's behavior. Verify that path or retain the evidence gap. Conversely, one P4 wording suggestion after complete coverage does not require another round. State which uncertainty another pass would resolve before repeating it.
