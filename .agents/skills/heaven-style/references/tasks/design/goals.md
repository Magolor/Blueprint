---
name: workflow-design-goals
description: Read before updating goals or linked planning trackers.
---

# Goals and tracker alignment

## Summary

Align goal horizons and authorized tracker updates with current evidence and owned work.

## Goals update procedure

Align `docs/goals/` (or project equivalent) with evidence from discovery.

### Short term (weeks)

- Tie each item to the current outcome and canonical task owner; link an external issue only when the repository uses one.
- Mark completed items with date; summarize closure in the development log and rely on Git for execution history.
- Prefer coherence and doc/code alignment before new features.

### Mid term (1–3 months)

- Routing depth, persistence gaps, docs-site milestones, template/skill alignment — themes, not ticket dumps.
- Each theme states dependency on short-term items when order matters.

### Long term (3+ months)

- Train candidates (`0.2` etc.), architectural bets, explicit **non-goals** that prevent over-engineering.

### Standing non-goals

- Keep a short permanent non-goal list when recurring architectural regressions need an explicit guard, but do not copy another repository's list.

Deliverable: a **goals diff** — proposed edits to `roadmap.md`, `current.md`, or `docs/goals/README.md` with rationale per bullet.

## Linear and GitHub alignment

When the design ties to an external tracker and updates are authorized:

1. Update the existing issue when the tracker owns it, or link the canonical task when it is a mirror. Do not copy a second writable acceptance list.
2. Link related issues; avoid duplicating milestones already tracked.
3. For continuous design issues, edit **one rolling status comment** with plan version, open questions, and slice progress — do not spam routine updates.
4. If the plan gates a PR series, note suggested branch naming and review order in the issue.
5. Do not set issues to `Done` unless the user explicitly authorizes it.
