#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
BRANCH="$(git branch --show-current)"
if [[ "${BRANCH}" != "typescript" && "${BRANCH}" != "python" ]]; then
    echo "error: prepare a release from typescript or python" >&2
    exit 1
fi
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "error: commit tracked changes before preparing a release" >&2
    exit 1
fi
if [[ "${BRANCH}" == "typescript" ]]; then
    pnpm check
else
    uv sync --all-extras --frozen
    bash scripts/check.bash full
    uv build
    WHEEL="${ROOT}/dist/blueprint-0.2.0a1-py3-none-any.whl"
    uv run --isolated --no-project --with "${WHEEL}" python -c 'import blueprint; assert blueprint.__version__ == "0.2.0a1"; assert blueprint.get_project_info().name == "Blueprint"'
    uv run --isolated --no-project --with "${WHEEL}" bp --version
fi
VERSION="0.2.0-alpha.1"
OUTPUT="${ROOT}/.temp/release"
NAME="blueprint-${VERSION}-${BRANCH}"
mkdir -p "${OUTPUT}"
git archive --format=tar.gz --prefix="${NAME}/" --output="${OUTPUT}/${NAME}.tar.gz" HEAD
(cd "${OUTPUT}" && shasum -a 256 "${NAME}.tar.gz" > "${NAME}.sha256")
echo "Prepared ${OUTPUT}/${NAME}.tar.gz from $(git rev-parse HEAD). No remote changes were made."
