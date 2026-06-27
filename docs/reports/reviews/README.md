# Reviews

Use this folder for durable review reports when findings need an audit trail, gate a PR or issue, or create follow-up work.

Quick read-only reviews can stay inline in the agent response. Save a report when the review must be resumed, annotated, tracked, or cited later.

## Review Report Requirements

- Scope and comparison base.
- Evidence inspected, including commands, files, docs, issues, and PRs.
- Findings first, ordered by severity.
- File and line references when available.
- User annotation fields for findings that need human triage.
- Verification gaps and residual risk.
- Acceptance criteria for confirmed follow-up work.

Use this naming pattern:

```text
docs/reports/reviews/YYYY-MM-DD-<scope>-review.md
```

For Heaven-style code reviews, prefer:

```text
docs/reports/reviews/YYYY-MM-DD-<scope>-heaven-style-review.md
```
