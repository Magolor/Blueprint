# Surveys

Use this folder for durable research and survey reports that may guide future decisions.

Surveys should preserve enough source and method context for a later agent to judge whether the result is still valid.

## Survey Report Requirements

- Question or decision the survey supports.
- Scope, exclusions, and time sensitivity.
- Sources inspected and source-quality limits.
- Findings and options.
- Recommendation or decision criteria.
- Staleness trigger, such as dependency release, pricing change, API change, or date-based review.
- Follow-up links to one concrete-project task or one Blueprint direct/external maintenance reference, plus plans or resources when useful.

Use this naming pattern:

```text
docs/reports/surveys/YYYY-MM-DD-<scope>-survey.md
```

<!-- blueprint-template-only:start -->
## Current Blueprint Research

- [CDASE workflow comparison](2026-07-21-cdase-workflow-comparison-survey.md) summarizes the reference workflow and compares its enforceable lessons with Blueprint, HeavenBase, and DeepSeek Harness.
- [Heaven-style improvement proposal](2026-07-21-heaven-style-improvement-proposal.md) records the actioned Pareto portfolio, remaining recommendations, design conflicts, and implementation criteria.
<!-- blueprint-template-only:end -->
