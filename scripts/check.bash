#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"

MODE="${1:-fast}"
if [[ $# -gt 1 || "${MODE}" != "fast" && "${MODE}" != "full" ]]; then
    echo "Usage: bash scripts/check.bash [fast|full]" >&2
    exit 2
fi

if [[ "${MODE}" == "full" ]]; then
    pnpm check
else
    pnpm check:fast
fi
