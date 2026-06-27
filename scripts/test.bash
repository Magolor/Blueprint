#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
source "${ROOT}/scripts/_env.bash"

PYTEST_ARGS=()
PARALLEL=0

usage() {
    cat <<'EOF'
Usage: bash scripts/test.bash [OPTIONS] [PYTEST_ARGS...]

Run pytest through uv.

Options:
  --parallel             Run with pytest-xdist using -n auto.
  --asyncio-mode MODE    Forward pytest asyncio mode, e.g. auto or strict.
  -h, --help             Show this help message.

Examples:
  rtk bash scripts/test.bash
  rtk bash scripts/test.bash -m "fast and not full" -q
  rtk bash scripts/test.bash -m full
  rtk bash scripts/test.bash --parallel
  rtk bash scripts/test.bash tests/test_scripts.py -q
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --parallel)
            PARALLEL=1
            shift
            ;;
        --asyncio-mode)
            if [[ $# -lt 2 ]]; then
                echo "error: --asyncio-mode requires a value" >&2
                exit 1
            fi
            PYTEST_ARGS+=(-o "asyncio_mode=$2")
            shift 2
            ;;
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

if [[ "${PARALLEL}" -eq 1 ]]; then
    if [[ $(array_len PYTEST_ARGS) -gt 0 ]]; then
        PYTEST_ARGS=(-n auto "${PYTEST_ARGS[@]}")
    else
        PYTEST_ARGS=(-n auto)
    fi
fi

if [[ "${#PYTEST_ARGS[@]}" -eq 0 ]]; then
    if [[ ! -d tests ]] || ! find tests -type f -name 'test_*.py' -print -quit | grep -q .; then
        echo "[test] no tests found"
        exit 0
    fi
    PYTEST_ARGS=(tests -q)
fi

resolve_uv
"${UV_BIN}" run pytest "${PYTEST_ARGS[@]}"
