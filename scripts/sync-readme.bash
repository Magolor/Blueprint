#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
source "${ROOT}/scripts/_env.bash"

CHECK=0
SOURCE="README.en.md"
TARGETS=(README.md "src/blueprint/resources/README.md")

usage() {
    cat <<'EOF'
Usage: bash scripts/sync-readme.bash [OPTIONS]

Copy README.en.md to README.md, src/blueprint/resources/README.md, and optional extra targets.
README.en.md is the canonical README source.

Options:
  --check                  Verify targets match README.en.md without writing.
  --target PATH            Also sync/check README.en.md to PATH.
  --resource-target IMPORT Also sync/check src/IMPORT/resources/README.md.
  -h, --help               Show this help message.

Examples:
  rtk bash scripts/sync-readme.bash
  rtk bash scripts/sync-readme.bash --check --resource-target heavenbase
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --check)
            CHECK=1
            shift
            ;;
        --target)
            if [[ $# -lt 2 ]]; then
                echo "error: --target requires a value" >&2
                exit 1
            fi
            TARGETS+=("$2")
            shift 2
            ;;
        --resource-target)
            if [[ $# -lt 2 ]]; then
                echo "error: --resource-target requires a value" >&2
                exit 1
            fi
            TARGETS+=("src/$2/resources/README.md")
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "error: unknown option: $1" >&2
            usage
            exit 1
            ;;
    esac
done

if [[ ! -f "${SOURCE}" ]]; then
    echo "error: ${SOURCE} not found" >&2
    exit 1
fi

if [[ "${CHECK}" -eq 1 ]]; then
    run_python - "${SOURCE}" "${TARGETS[@]}" <<'PY'
from pathlib import Path
import sys

source = Path(sys.argv[1])
targets = [Path(item) for item in sys.argv[2:]]
source_bytes = source.read_bytes()
outdated = [str(target) for target in targets if not target.exists() or target.read_bytes() != source_bytes]
if outdated:
    for target in outdated:
        print(f"error: {target} is out of date; run rtk bash scripts/sync-readme.bash", file=sys.stderr)
    sys.exit(1)
PY
    echo "[readme] ${#TARGETS[@]} target(s) current"
    exit 0
fi

run_python - "${SOURCE}" "${TARGETS[@]}" <<'PY'
from pathlib import Path
import sys

source = Path(sys.argv[1])
targets = [Path(item) for item in sys.argv[2:]]
source_bytes = source.read_bytes()
for target in targets:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source_bytes)
PY
echo "[readme] copied ${SOURCE} to ${#TARGETS[@]} target(s)"
