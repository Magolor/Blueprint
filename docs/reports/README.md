# Reports

Reports preserve evidence, findings, and recommendations. They do not own task state.

| Folder | Use |
| --- | --- |
| [reviews](reviews/README.md) | Code, architecture, release, or documentation reviews. |
| [refactors](refactors/README.md) | Refactor investigations and migration results. |
| [surveys](surveys/README.md) | Technical, product, dependency, API, or domain research. |

Use this file name:

```text
docs/reports/<family>/YYYY-MM-DD-<scope>-<kind>.md
```

Each report must state its status, scope, trigger, evidence, findings, limits, follow-up owner, and staleness trigger.

Use `Draft`, `Current`, `Actioned`, or `Superseded`. Put actionable follow-up in one queue task. Keep reports non-normative until an authority accepts their conclusions.
