---
name: ts-env-compiler
description: Read before changing TypeScript compiler or module profiles.
---

# TypeScript compiler profiles

## Summary

Align strict compiler checks with the actual runtime, module resolver, and emitted artifact.

## Compiler baseline

Keep these semantic checks enabled unless a concrete tool/target incompatibility is recorded:

```jsonc
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true,
    "verbatimModuleSyntax": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

- Add only the host libraries the package supports; do not add DOM types to make accidental browser globals compile in server code.
- Use `import type`/`export type` where runtime-edge visibility matters.
- Keep typecheck and emit responsibilities explicit. A library often needs a no-emit check config plus a build config.
- Treat `skipLibCheck: true`, broad assertions, and lint suppressions as recorded compatibility debt, not silent defaults.

## Runtime and module modes

- **Bun-native app/tool:** use the compiler/module profile supported by Bun or the selected bundler; test the real entry path.
- **Unbundled Node library:** use modern Node ESM/`NodeNext`, emit JavaScript and declarations, write runtime-valid specifiers, and test supported Node releases.
- **Bundled app/browser package:** use the actual bundler/target profile and keep browser/shared code free of unsupported server-runtime imports.
- **Published source package:** document the required consumer tooling and validate a packed external consumer; do not assume Node executes TypeScript source.
- **Workspace:** import other packages by their public package names, declare workspace dependencies, and reject sibling source-path coupling unless it is an explicitly private source plane.

Never mix modes opportunistically within one package. Runtime, resolver, emit, exports, and consumer expectations must agree.
