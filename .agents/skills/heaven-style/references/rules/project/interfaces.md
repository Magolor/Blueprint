---
id: interfaces
title: Service interface architecture
enabled: true
blocking: true
order: 135
category: project
keywords: [service architecture, Python SDK, API layer, REST, OpenAPI, async API, parallel requests, CLI, GUI, MCP, TUI, Typer, Click, argparse, Rich, CLIRegistry, Tauri, thin wrapper]
description: Use when a package is provided as a service or exposes SDK, API, CLI, GUI, MCP, TUI, dashboard, or desktop-app surfaces.
---

# Service Interface Architecture

## Core rule

For a package intended to be provided as a service, separate core behavior, the public Python SDK, the service API, and user interfaces into explicit dependency layers:

```text
Python SDK facade ────────────────> core/domain package
CLI / GUI / MCP / TUI ──> api/ ──> core/domain package
```

Core features live inside the package and are exposed through a small, preferably OOP Python SDK. A real `api/` package owns application orchestration, serializable request/response contracts, and service transports. Every CLI, GUI, MCP, TUI, or future interface is a thin adapter over that API boundary. Core code never imports `api/` or an interface package.

In this rule, **SDK** means the public Python import surface over core behavior. The `api/` directory is the service/application boundary; it is not an exposure-only `api.py`, re-export facade, or second SDK.

## Apply when

- A package is deployed, embedded, or consumed as a service.
- Code adds or redesigns a Python SDK, HTTP API, CLI, GUI, dashboard, MCP server, TUI, or desktop app.
- Business rules, validation, persistence, defaults, or orchestration are duplicated across interfaces.
- A Python CLI needs Typer, Click, or argparse support.
- A GUI must choose between a minimal local workbench and a releasable desktop application.

## Layer contract

### Core and Python SDK

- Keep domain rules, storage, providers, execution, and reusable feature behavior in the package's core/feature modules.
- Expose the shortest Python SDK front door from the package facade. Prefer owning objects for identity, state, invariants, and lifecycle; use functions for stateless transforms.
- Keep transport, parser, terminal, browser, and desktop-framework types out of core signatures.
- Do not make CLI, HTTP, GUI, MCP, or TUI imports a prerequisite for importing the SDK.

### `api/` application and service boundary

- Put cross-feature use-case orchestration in `api/`, not in interface callbacks or domain entities.
- Define typed, serializable request, response, pagination, error, and event contracts once. Validate untrusted input at this boundary before calling core behavior.
- Keep application service methods independently testable without HTTP framework objects. HTTP routes should translate transport values to those methods and translate results/errors back.
- Prefer resource-shaped REST routes and publish a current OpenAPI contract. Generate or check the schema from the same request/response definitions instead of maintaining a second endpoint catalog by hand.
- Provide an async client or async service surface for remote/I/O-heavy work. Request handlers must support concurrent requests without process-global request state, blocking the event loop, or sharing unsafe mutable objects.
- Move blocking I/O or CPU work to an owned worker/thread/process/task boundary; define timeouts, cancellation, concurrency limits, idempotency, and cleanup where the operation needs them.
- Keep authentication, authorization, rate limiting, transport security, and exposure policy at the service boundary. A local-only unauthenticated API must bind to loopback and defend against cross-origin/DNS-rebinding access; a network service must not inherit that waiver.

Local interfaces may call the application service in-process. Remote interfaces use the HTTP/OpenAPI client. Both paths must preserve the same request/response behavior and error semantics.

### Thin interfaces

- `cli/`, `gui/`, `mcp/`, and `tui/` own presentation, input collection, output rendering, and interface-specific lifecycle only.
- Interface callbacks call `api/` services or clients. They do not query databases, select providers, resolve domain defaults, or reimplement validation and orchestration.
- Interface-only dependencies load lazily so the core SDK stays importable without GUI, CLI, MCP, or desktop stacks.
- A new interface should be addable without changing core behavior. A new core feature should normally require one API operation plus small interface mappings, not independent implementations.

## Standard package shape

Use this as a service-package template, including only real surfaces:

```text
src/acme/
  __init__.py          # public Python SDK facade
  <domain modules>/    # core features grouped by owner
  api/
    __init__.py        # supported application/service surface
    models.py          # serializable request/response/error contracts
    service.py         # transport-neutral orchestration
    http.py            # REST/OpenAPI/ASGI adapter when shipped
    client.py          # async/sync service client when needed
  cli/
    spec.py            # backend-neutral command declarations
    registry.py        # command/group/alias registry
    backends/
      typer.py
      click.py
      argparse.py
    app.py             # mode selection; Typer default
  gui/                 # web/desktop presentation only
  mcp/                 # tools/resources/prompts mapped to api/
  tui/                 # terminal presentation mapped to api/
```

Do not create empty folders for imagined interfaces. Once a surface exists, keep it in its named package and enforce the dependency direction.

## Python CLI contract

All Python project CLIs must support **Typer, Click, and argparse simultaneously**, with **Typer as the default mode** and **Rich shared across all three** for output, errors, tables, progress, prompts, and consistent terminal styling.

- Declare commands, groups, aliases, arguments, options, help, and callbacks once in parser-neutral specs and a modular registry, following HeavenBase's `CLIRegistry` pattern.
- Compile the same registry into Typer, Click, and argparse backends. Do not maintain three command trees or put framework branches inside command callbacks.
- Keep command groups feature-local and register them into one root registry. A package or plugin may contribute a group without editing unrelated groups.
- Command callbacks accept a CLI context plus parsed values, call the API layer, and render the result. They do not parse `sys.argv`, construct provider/storage services, or contain business logic.
- Expose an explicit programmatic mode selector such as `create_cli(mode="typer")`; config or environment may override it, but the installed default entry point uses Typer.
- Use Rich directly or a compatible integration such as `rich-argparse` where a backend needs help rendering. Backend-native parsing semantics must not change API behavior.
- Run command, alias, help, success, validation-error, and exit-code parity tests against all three backends. A command is incomplete until every backend compiles it.

## GUI contract

### Minimal Python GUI

Prefer the HeavenBase dashboard pattern for a small local workbench:

- a transport-neutral Python API service;
- a thin Starlette-compatible ASGI route layer served by Uvicorn;
- a zero-build frontend made from vanilla JavaScript ES modules, HTML, and CSS;
- static assets packaged in the wheel;
- browser launch or Chromium app-window mode for desktop-like use;
- no Node/Vite build chain unless the interface has outgrown the minimal tier.

The frontend talks only to the JSON API. The server adapter and browser code own no core storage, planning, or configuration implementation. Follow [GUI style](../../design/gui-style.md) for visual and interaction rules.

### Releasable desktop application

For a serious distributable desktop app, use **React with TypeScript** for the frontend and **Tauri v2 with Rust** for native packaging and the desktop shell.

- React consumes the REST/OpenAPI client; generate a typed client when the contract and toolchain support it.
- Tauri/Rust owns packaging, windows, permissions, updates, and narrow native integrations. It does not become a second domain implementation.
- Keep Tauri capabilities and commands allowlisted and minimal. Prefer the service API over broad shell, filesystem, or process access.
- Follow the repository's checked TypeScript toolchain and the `ts-*` rules; a new unspecified repo uses the skill's normal Bun-first baseline when compatible with the selected Tauri toolchain.

## Other interface contracts

- **MCP:** map tools, resources, and prompts to API operations; keep MCP schemas generated from or checked against the same request/response models.
- **TUI:** reuse the API client and Rich presentation primitives; terminal widgets do not bypass application orchestration.
- **Automation or agents:** call the same documented API contract and preserve stable error codes rather than scraping human-facing CLI output.

## Avoid

- CLI callbacks, GUI routes, MCP tools, or TUI screens that import storage/backend internals directly.
- A separate business-logic implementation for each interface.
- `api.py` or `api/` used only to re-export package symbols.
- HTTP request objects leaking into application services or domain methods.
- Sync-only network clients or handlers that serialize unrelated requests without a documented constraint.
- Three manually maintained Python command trees with different flags or behavior.
- A Streamlit/NiceGUI/browser prototype promoted into a serious packaged desktop app without an explicit architecture decision.
- React, Tauri, Rust, Node, or desktop dependencies on the core Python SDK import path.

## Review checks

- Can the package's core features be used through the Python SDK without importing an interface stack?
- Is `api/` real orchestration with typed contracts rather than a facade?
- Do dependencies flow from interfaces to API to core, never upward?
- Are REST resources and the OpenAPI contract derived from one source of truth?
- Can I/O-heavy operations run concurrently with explicit ownership, limits, cancellation, and cleanup?
- Do CLI, GUI, MCP, and TUI contain presentation code only?
- Does one CLI registry compile and pass parity tests under Typer, Click, and argparse, with Typer as default and Rich shared?
- Does the GUI tier match the product: zero-build local workbench for minimal scope, React/TypeScript plus Tauri v2 for a releasable desktop app?
- Can a new interface be added without changing core behavior?

## Sources

- [HeavenBase `CLIRegistry` implementation](https://github.com/Magolor/HeavenBase/tree/master/src/heavenbase/cli)
- [HeavenBase dashboard branch](https://github.com/Magolor/HeavenBase/tree/feat/dashboard)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Typer documentation](https://typer.tiangolo.com/)
- [Click documentation](https://click.palletsprojects.com/)
- [Python `argparse` documentation](https://docs.python.org/3/library/argparse.html)
- [Rich documentation](https://rich.readthedocs.io/)
- [Tauri v2 frontend configuration](https://v2.tauri.app/start/frontend/)

## Related rules

For Python, also apply [mental model](../code/python/model.md), [OOP vocabulary](../code/python/oop.md), [file organization](../code/python/files.md), and [docstrings](../code/python/docstring.md). For TypeScript/React, apply [architecture](../code/typescript/architecture.md), [modules](../code/typescript/modules.md), [async](../code/typescript/async.md), [docs](../code/typescript/docs.md), and [environment](../code/typescript/environment.md). Apply [extension points](extension.md), [tests](test.md), [docs](docs.md), and [GUI style](../../design/gui-style.md) as the surface requires.
