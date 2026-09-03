#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
source "${ROOT}/scripts/_env.bash"

if [[ "$(git branch --show-current)" != "python" ]]; then
    echo "error: releases must start from the python branch" >&2
    exit 1
fi
if [[ -n "$(git status --porcelain)" ]]; then
    echo "error: working tree must be clean" >&2
    exit 1
fi

uv sync --all-extras --frozen
bash scripts/check.bash full
uv build
git push origin python
gh workflow run release.yml --ref python -f publish=true
echo "Triggered the verified PyPI release workflow from python."
