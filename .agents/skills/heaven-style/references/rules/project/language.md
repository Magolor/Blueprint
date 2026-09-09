---
name: project-language
description: Read before writing prose, chat updates, or final task responses.
---

# Language and responses

## Summary

Use short, direct, natural language in documentation and conversation. Lead with what the reader needs to know, then give enough context and evidence to act. Follow the user’s language preference and the repository’s artifact conventions.

## Shared language

Use a non-certified, ASD-STE100-inspired editorial pass for authored English prose. This is a clarity discipline; it does not claim standards compliance or impose a controlled dictionary.

- Name the actor and action when ambiguity can change behavior. Prefer active voice when the actor matters.
- Use one stable term for each concept. Prefer direct verbs over nominalizations, vague phrasal verbs, and rotating synonyms.
- Use logical quotation punctuation: place periods and commas outside closing quotation marks unless they are part of the quoted material, while otherwise following American English conventions.
- Put one instruction in each sentence. Use a list for several steps or conditions, split long clause chains, and keep each paragraph on one topic.
- Remove unsupported quality adjectives and stacked hedges. Preserve every `must`, `may`, `never`, condition, exception, number, timing constraint, and degree of uncertainty.
- Keep a longer sentence when splitting it would hide a relationship or reduce precision. Professional technical prose must remain natural, respectful, and exact. Do not shorten sentences mechanically.

Apply the same clarity goals in other languages using native grammar and terminology. Do not force English sentence patterns into translations. Preserve identifiers and executable syntax.

## Chat updates and final responses

Answer the question or state the result first. For completed work, explain the meaningful outcome, relevant verification, and any material gap or next action. Mention changed files only when the location helps the reader. Distinguish completed work, proposals, and unverified claims.

Scale detail to the task. A small change may need one paragraph; a complex result may need a short list or comparison. Use headings only when they help navigation. Chat needs neither YAML nor an explicit Summary heading, and has no fixed word limit.

Omit command transcripts, repeated plans, ceremonial reassurance, and unsupported quality claims. Explain a technical name through its role before relying on it. Include implementation detail only when it helps the reader assess behavior, a decision, or a limitation. Report relevant checks without claiming broader coverage than they provide. Do not invent a risk or next step to fill a section.

Progress updates report new evidence, decisions, or blockers. Final responses stand alone; the reader should not need to recover earlier updates. In discussion, preserve enough reasoning to answer the actual question rather than compressing everything into a completion notice.

## Pattern and Anti-pattern

- **Pattern:** “The CLI now preserves quoted arguments. Parser tests pass.”
- **Anti-pattern:** “Successfully leveraged a robust refactoring of `parseInput` to enhance parsing.”

Name the observable result and evidence; omit praise and unexplained internals. This is an illustrative example, not a product claim.

## References

Use [authoring](../../tasks/docs/write.md) for artifact structure, [claim verification](docs/prose.md) for evidence, and [work boundaries](work.md#communicate-the-result) for handoff and publication scope. API comments and docstrings retain their native language and repository rules.
