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

Run Blueprint's repository-owned validation inventory.

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
bash scripts/check-skill-sync.bash
resolve_uv
"${UV_BIN}" lock --check
bash scripts/flake.bash --ci

CONTRACT_TESTS=(
    tests/test_docs_contract.py
    tests/test_heaven_style_install.py
    tests/test_heaven_style_index.py
    tests/test_heaven_style_scan.py
    tests/test_skill_sync.py
)

if [[ "${MODE}" == "full" ]]; then
    bash scripts/test.bash
else
    bash scripts/test.bash "${CONTRACT_TESTS[@]}" -q
fi
