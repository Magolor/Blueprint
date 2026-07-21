# Refactors

Use this folder for durable refactor reports: investigations, migration summaries, dependency cleanup findings, and post-refactor closeouts.

Executable refactor plans belong in `docs/plans/`. Stable architecture conclusions belong in `docs/resources/`. A refactor report is the evidence trail that explains why the refactor happened, what changed, and what remains.

## Refactor Report Requirements

- Trigger and change pressure.
- Before/after map of modules, public imports, data flow, or ownership.
- Invariants that had to remain true.
- Risks, waivers, and compatibility decisions.
- Verification performed.
- Remaining follow-up linked to one concrete-project task or one Blueprint direct/external maintenance reference and, when needed, a plan.

Use this naming pattern:

```text
docs/reports/refactors/YYYY-MM-DD-<scope>-refactor-report.md
```
