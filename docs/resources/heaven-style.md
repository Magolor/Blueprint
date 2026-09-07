# Heaven Style Maintenance

Blueprint owns `.agents/skills/heaven-style/`. The `typescript` and `python`
product branches contain the same tracked skill tree. Repository policy owns
branch synchronization and verification commands.

## Reading structure

[SKILL.md](../../.agents/skills/heaven-style/SKILL.md) contains required reading and core design decisions. Every code task requires the complete applicable language and shared project rule trees, including nested pages. Code and architecture also require the shared design philosophy. Architecture adds all design workflows and comparisons; GUI work adds the complete GUI tree. The generated index alone does not satisfy reading. The [rule map](../../.agents/skills/heaven-style/references/rules/overview.md) pairs Python and TypeScript topics. Details belong to the rule that owns them.

API documentation and implementation comments have separate `doc.md` and `comment.md` owners in both languages. Python retains full Google-style sections and annotations; TypeScript uses semantic TSDoc, explicit public return types, and native tags. Shared vocabulary follows domain meaning with native language spelling and protocols.

[GUI style](../../.agents/skills/heaven-style/references/design/gui/style.md) routes to layout, elements, spacing, motion, theme behavior, stack decisions, and review. Six files under `gui/theme/` preserve the exact palette declarations. Durable interfaces still support all six themes.

Maintain the skill with a small entry, short maps, and focused pages with explicit reading prerequisites. The [editor guide](../../.agents/skills/heaven-style/references/workflows/editor.md) owns the size targets and maintenance procedure. These targets apply to the skill, not every repository it advises. Renames preserve rule IDs where the owner survives; removed routing-only aliases do not need compatibility stubs.

## Documentation contract

The skill's [documentation rule](../../.agents/skills/heaven-style/references/rules/project/docs/prose.md#controlled-technical-english)
owns its non-certified ASD-STE100-inspired English standard. Use direct verbs,
explicit actors, stable terms, and separate instructions. Preserve modality,
conditions, exceptions, numbers, examples, identifiers, and links during edits.
Retain precise longer sentences where splitting them would obscure a relationship.

Compare changed prose with the original. Check fenced examples, theme values,
headings, frontmatter identities, local links, and numeric constraints separately.
These mechanical checks support semantic review; they do not prove semantic
completeness or standards certification.

## Environment authority

The user-selected machine setup is `~/Developer/Setup`. Its provisioning,
maintenance, machine profiles, shell assets, package manifests, and Docker
controller own machine settings. The skill's [asset map](../../.agents/skills/heaven-style/assets/REFERENCE.md)
routes to that owner and describes recovery when the setup or facts are missing.

The environment consolidation used Setup revision
`b5bf034223d00dc2ea7daa6c4bdbb1be3dc97442` on 2026-09-07. This identifies the
inspected source, not a runtime dependency or a promise that every machine uses
that revision. Re-read the actual setup before maintenance. Setup itself was
not changed by the consolidation.

Reviewed non-secret instance notes are tracked. Machine identity, capacity, and
executable paths are observations, not proof about a later session. Credentials,
private device identifiers, and transient probe output remain outside the skill.
The reporter defaults to `~/.config/heaven-style/machine.md`; an explicit
`--output` selects a repository snapshot. Legacy installed `*.local.md` notes
remain preserved but are not the current environment authority.

The old assets added a hardware/path snapshot and duplicated maintenance and
Docker instructions. They did not define another required settings layer.
Current stack inventories and command flags belong to Setup. The skill retains
portable project/host boundaries, stateful-upgrade cautions, and missing-fact
recovery. A machine's Bun-first local-tool default does not override a project's
manager or Heaven Style's Bun/pnpm selection criteria.

## Design philosophy evidence

The shared [design philosophy](../../.agents/skills/heaven-style/references/design/philosophy.md)
combines the existing language API, SOLID, file, helper, interface, extension,
and documentation rules with legacy Python HeavenBase's
`docs/resources/architecture/design-philosophy.md` and `mental-model.md` at
commit `adf98c7ad9e95b16baf0b42bf33b7398ce6937ab`, inspected on 2026-09-07.
The source repository is `https://github.com/Magolor/HeavenBase`.
The inspected checkout is local reference evidence, not a shipped dependency.

Retained principles are a small public OOP surface, separate user and extension-author
contracts, decoupled internal responsibilities, one policy owner, explicit
composition and lifecycle, extension parity, and observable execution. Project-specific
classes, storage catalogs, and directory topology are not universal requirements.
The entry now names eight rule groups and seven common workflows directly;
these summaries do not replace complete required reading.
