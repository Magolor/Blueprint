---
id: workflow-developer
title: Developer workflow
audience: developer
description: Implement ordered slices or resolve shared-contract tradeoffs.
---

# Broad implementation

Use this page when implementation spans shared contracts or ordered slices. Design-only work uses [design](../tasks/design.md).

Read repository policy, the accepted plan or issue, public contracts, configuration owners, nearby code, and relevant tests. Complete [required reading](read.md) for the full applicable language and shared project trees before implementation. The [rule map](../rules/overview.md) helps check coverage.

Keep one plan linked to the canonical task. Record the outcome, acceptance conditions, public/data boundaries, compatibility policy, ordered slices, verification, docs impact, non-goals, and any waiver. Map disputed decisions to the owning rule. Keep runtime and package verification aligned with repository metadata.

For each slice, implement the smallest coherent change, exercise its behavior, review the diff, and run focused checks. Broaden to the repository gate at integration or closeout. Preserve behavior unless the task changes it. Update owned callers and remove obsolete paths together.

For a linked Linear milestone, read prior comments and review artifacts. Keep routine progress in one authorized rolling status comment. Separate decisions, blockers, and handoffs may need distinct records. [Work boundaries](work.md) govern external updates.

When rules conflict, repository authority wins. Otherwise choose the smallest testable design that satisfies the verified need. A new abstraction must own real policy, variation, identity, or lifecycle.
