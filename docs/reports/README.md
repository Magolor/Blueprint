# Reports

Use this folder for durable reports that need an audit trail. Reports preserve evidence, findings, and recommendations; they are not daily status notes.

## Report Families

| Folder | Use |
| --- | --- |
| [reviews](reviews/README.md) | Code, PR, architecture, release, or docs reviews that gate follow-up work. |
| [refactors](refactors/README.md) | Refactor investigations, migration reports, and post-refactor summaries. |
| [surveys](surveys/README.md) | Technical, product, dependency, API, or domain surveys that inform decisions. |

## Naming

Use dated, scoped names:

```text
docs/reports/<family>/YYYY-MM-DD-<scope>-<kind>.md
```

Examples:

```text
docs/reports/reviews/2026-06-27-cli-heaven-style-review.md
docs/reports/refactors/2026-06-27-config-refactor-report.md
docs/reports/surveys/2026-06-27-docs-governance-survey.md
```

## Required Shape

Each report should include:

- Status: Draft | Current | Actioned | Superseded
- Scope and trigger.
- Evidence inspected.
- Findings, recommendations, or decision options.
- Follow-up owner or linked plan/issue.
- Verification or source-quality limits.
- Staleness trigger, such as release boundary, dependency update, or next review date when the project uses one.

Promote durable conclusions into `docs/resources/` or `docs/goals/` after the report is accepted. Keep the report as the evidence trail.

Reports never own task state. In operational mode, actionable follow-up enters the one declared task authority; template maintenance uses a direct request or selected external issue. After action, mark the report `Actioned` or `Superseded` and remove any closed operational task.
