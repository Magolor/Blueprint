---
id: workflow-design-goals
title: Goals and tracker alignment
description: Read for goals and tracker alignment.
---

# Goals and tracker alignment

## Goals update workflow

Align `docs/goals/` (or project equivalent) with evidence from discovery.

### Short term (weeks)

- Bullet items tied to **current train** work; each item links to a Linear issue or names an owner slice.
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

When the design ties to tracked work:

1. Create or update a Linear issue with acceptance criteria copied from the plan summary.
2. Link related issues; avoid duplicating milestones already tracked.
3. For continuous design issues, edit **one rolling status comment** with plan version, open questions, and slice progress — do not spam routine updates.
4. If the plan gates a PR series, note suggested branch naming and review order in the issue.
5. Do not set issues to `Done` unless the user explicitly authorizes it.
