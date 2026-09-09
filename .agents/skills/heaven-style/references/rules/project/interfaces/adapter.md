---
name: project-interfaces-adapter
description: Read before adding CLI, GUI, MCP, TUI, or HTTP adapters.
---

# Interface adapters

## Summary

Keep CLI, GUI, protocol, and automation adapters thin while owning their interface lifecycle and presentation.

## CLI contract

- Use one repository-declared parser/framework by default.
- Keep parser definitions and handlers feature-local, then compose them at one explicit entry point.
- Handlers accept parsed/validated values, call application use cases or a client, and render results.
- Keep exit codes, stdout/stderr ownership, cancellation, and signal-driven teardown explicit and tested.
- Test the built or packed command entry when it is published.

If a repository explicitly promises multiple CLI-framework backends, define one parser-neutral command model. Compile that model to those backends. That compatibility profile needs named consumers and parity tests. It is not a default for ordinary CLIs.

## GUI and desktop contract

- Prefer TypeScript for a new browser UI unless repository evidence favors another frontend language.
- Keep UI state/presentation separate from the application service and transport client.
- Place a distinct frontend/desktop toolchain under an app root such as `apps/desktop/` or the repository's convention. Package-local placement is fine when it truly shares package tooling and distribution.
- Choose browser delivery, a system WebView, an existing desktop framework, or another native host from distribution, security, accessibility, update, binary-size, platform, and team evidence. A thin system WebView is a good option for a local tool, not a universal mandate.
- A host owns window/process lifecycle, secure navigation/origin policy, application packaging, and teardown. It does not become a second domain implementation.
- Keep framework and host dependencies off the core SDK path.

See [local GUI layout](../../../examples/code/gui.md) for cohesive and workspace examples, and [GUI style](../../../design/gui/style.md) for visual and interaction criteria.

## Other interface contracts

- **MCP:** map tools, resources, and prompts to application operations. Keep schemas generated from or checked against the same admitted contracts when practical.
- **TUI:** reuse application use cases or a client; terminal widgets do not bypass orchestration.
- **Automation/agents:** call a documented SDK or protocol contract and preserve stable machine-readable errors rather than scraping human CLI output.
- **REST/OpenAPI:** use it when HTTP clients and interoperability justify it; do not introduce HTTP merely to mediate two modules in one process.
