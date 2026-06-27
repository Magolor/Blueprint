# Docs

This file is the project docs menu and authority map. Keep it short, current, and project-specific after initializing Blueprint. Agents should use it before creating or changing docs artifacts.

## Core Areas

| Area | Purpose |
| --- | --- |
| [Goals](goals/README.md) | Long-, mid-, and short-term outcomes that guide implementation. |
| [Plans](plans/README.md) | Multi-slice designs and execution plans with checklist progress and verification gates. |
| [Resources](resources/README.md) | Stable references, architecture background, specifications, inventories, and source-of-truth notes. |
| [Reports](reports/README.md) | Durable review, refactor, and survey reports that need an audit trail. |
| [Progress](progress/README.md) | Append-only daily progress summaries, decisions, verification, blockers, and handoff notes. |

## Authority Order

When docs disagree, resolve in this order:

1. Shipped code, tests, generated artifacts, and release configuration.
2. Canonical English docs sources such as `README.en.md` and project-owned docs generators.
3. Stable resources under `docs/resources/`.
4. Current goals under `docs/goals/`.
5. Active plans under `docs/plans/`.
6. Durable reports under `docs/reports/`.
7. Dated progress notes under `docs/progress/`.

Progress notes explain what happened. They do not become long-term truth until the durable conclusion is promoted into goals, resources, shipped docs, or code.

## Initialization

When creating a project from Blueprint:

1. Replace this menu with the real project docs map.
2. Link the current short-term goal, active plan, latest progress day, and main source-of-truth references.
3. Keep only artifact families that the project will actively maintain.
4. Add project-specific docs only when they have an owner, lifecycle, and clear purpose.

## Agent Docs Check

Before major feature, refactor, review, survey, release, or docs-sync work, agents should check:

- Current goals: `docs/goals/` or the project-specific replacement.
- Current progress: the latest `docs/progress/YYYY-MM-DD/README.md`.
- Active or recently closed plans: `docs/plans/`.
- Relevant durable reports: `docs/reports/`.
- Feature requests and issue tracker: `AGENTS.md`, Linear/GitHub links, or the project-specific docs map.
- Stable references: `docs/resources/` and linked source-of-truth material.
- Canonical docs source, generated docs, and translation status.

If one of these locations is missing or ambiguous, choose the narrowest existing location that matches the artifact lifecycle. Ask before creating broad new docs folders.

## Update Triggers

- Major feature or public behavior change: update or create a plan when the work has multiple slices, update user-facing docs when behavior ships, and append the daily progress note.
- Architecture or cross-module refactor: create or update a plan before implementation, save a refactor report when findings or migration decisions need an audit trail, update stable architecture resources when the mental model changes, and append progress.
- Code or architecture review: return quick findings inline for small read-only reviews; save durable reviews under `docs/reports/reviews/` when the review gates a PR/issue or follow-up work.
- Survey or research task: save durable evidence under `docs/reports/surveys/` when the answer may guide future decisions; promote stable conclusions into `docs/resources/`.
- Release, docs sweep, or generated-doc sync: update canonical English sources and generated artifacts through repo scripts, append progress, and call out stale translations for the translation workflow.

## Closeout Gate

Before declaring docs-impacting work done:

- The relevant plan/report status is current or explicitly not needed.
- The daily progress note links the changed files, issue/plan/report, verification, decisions, and next step.
- Stable conclusions are promoted out of dated progress notes.
- Generated README/docs artifacts are synced through repo wrappers.
- Translation staleness is reported instead of mixed into ordinary English doc sync.
