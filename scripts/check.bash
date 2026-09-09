#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
source "${ROOT}/scripts/_env.bash"

MODE="${1:-fast}"
export UV_OFFLINE=1

usage() {
    cat <<'EOF'
Usage: bash scripts/check.bash [local|fast|full]

Run Blueprint's repository-owned validation inventory.

  local Commit checks; compare branch parity after both commits.
  fast  Deterministic PR gates including committed branch parity.
  full  Fast gates plus the complete test suite.
EOF
}

if [[ $# -gt 1 || "${MODE}" != "local" && "${MODE}" != "fast" && "${MODE}" != "full" ]]; then
    usage >&2
    exit 2
fi

run_python scripts/docs.py check
run_python .agents/skills/heaven-style/scripts/index.py --check
if [[ "${MODE}" != "local" ]]; then
    bash scripts/check-skill-sync.bash
fi
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
