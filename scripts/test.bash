#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
source "${ROOT}/scripts/_env.bash"

PYTEST_ARGS=()

usage() {
    cat <<'EOF'
Usage: bash scripts/test.bash [OPTIONS] [PYTEST_ARGS...]

Run pytest through uv.

Options:
  -h, --help             Show this help message.

Examples:
  rtk bash scripts/test.bash
  rtk bash scripts/test.bash -m "fast and not full" -q
  rtk bash scripts/test.bash -m full
  rtk bash scripts/test.bash tests/test_scripts.py -q
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            usage
            exit 0
            ;;
        *)
            PYTEST_ARGS+=("$1")
            shift
            ;;
    esac
done

if [[ "${#PYTEST_ARGS[@]}" -eq 0 ]]; then
    if [[ ! -d tests ]] || ! find tests -type f -name 'test_*.py' -print -quit | grep -q .; then
        echo "[test] no tests found"
        exit 0
    fi
    PYTEST_ARGS=(tests -q)
fi

resolve_uv
"${UV_BIN}" run pytest "${PYTEST_ARGS[@]}"
