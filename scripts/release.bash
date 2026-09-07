#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"

if [[ "$(git branch --show-current)" != "typescript" ]]; then
    echo "error: releases must start from the typescript branch" >&2
    exit 1
fi
if [[ -n "$(git status --porcelain)" ]]; then
    echo "error: working tree must be clean" >&2
    exit 1
fi

pnpm check
git push origin typescript
gh workflow run release.yml --ref typescript -f publish=true
echo "Triggered the verified npm release workflow from typescript."
