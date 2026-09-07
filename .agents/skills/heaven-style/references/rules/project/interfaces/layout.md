---
id: project-interfaces-layout
title: Service layouts
description: Read for service layouts.
---

# Service layouts

## Physical layouts

### Cohesive package

Use one package while the roles change and ship together:

```text
src/
  index.ts | __init__.py       # supported SDK facade
  domain/                      # business behavior and ports
  application/                 # transport-neutral use cases
  adapters/
    http/                      # optional protocol adapter/client
  interfaces/
    cli/                       # optional thin interface
    mcp/                       # optional thin interface
```

Names are illustrative. Feature-local folders are equally valid when they preserve the same dependency direction.

### Earned workspace packages

Use packages when the boundary has concrete pressure:

```text
packages/
  core/                        # embeddable domain/public SDK
  application/                 # portable application contract/client
  server/                      # service implementation + transports
  testkit/                     # only when external conformance needs it
apps/
  cli/                         # private composition root
  server/                      # process/listener root
  desktop/                     # distinct UI/host toolchain
```

Do not copy these names mechanically. A package must answer at least one of these questions:

- Who consumes it independently?
- Which runtime, dependency set, or security boundary does it isolate?
- Which compatibility or release contract does it own?
- Which clean packed-consumer or extraction check proves the boundary?

If the answers are “nobody” and “none”, keep a folder inside the cohesive owner.

## TypeScript and Python

TypeScript and Python are equal language-native surfaces. Use the repository's declared language and preserve coherent shipped behavior. For greenfield service work, TypeScript is a strong default when the runtime, browser, package, or future Node integration benefits from one type system; Python remains fully appropriate when its ecosystem and existing domain ownership are the better fit.

When both languages exist, avoid implementing the same core twice by default. Prefer one authoritative service/application contract with an idiomatic client in the other language, unless offline embedding or performance evidence genuinely requires two implementations. Cross-language parity belongs to protocol and behavior tests, not mirrored internal folder names.
