#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
source "${ROOT}/scripts/_env.bash"

MODE="${1:-fast}"
export UV_OFFLINE=1

usage() {
    cat <<'EOF'
Usage: bash scripts/check.bash [fast|full]

Run Blueprint's offline repository-owned validation inventory after the
development environment has been synchronized.

  fast  Deterministic PR and pre-commit gates.
  full  Fast gates plus the complete test suite.
EOF
}

if [[ $# -gt 1 || "${MODE}" != "fast" && "${MODE}" != "full" ]]; then
    usage >&2
    exit 2
fi

run_python scripts/docs.py check
run_python .agents/skills/heaven-style/scripts/index.py --check
if [[ -f ".blueprint-template.yaml" ]]; then
    run_python scripts/template_sync.py check-source
fi
bash scripts/flake.bash --ci

CONTRACT_TESTS=(
    tests/test_docs_contract.py
    tests/test_heaven_style_index.py
    tests/test_heaven_style_scan.py
    tests/test_template_sync.py
)
if [[ -f ".blueprint-template.yaml" ]]; then
    CONTRACT_TESTS+=(tests/test_rename.py)
fi

if [[ "${MODE}" == "full" ]]; then
    bash scripts/test.bash
else
    bash scripts/test.bash "${CONTRACT_TESTS[@]}" -q
fi
