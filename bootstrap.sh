#!/usr/bin/env bash
# ==============================================================================
# Script Name: bootstrap.sh
# Description: Convenience wrapper around bootstrap.py. Requires Python 3.
#              All options are forwarded unchanged to bootstrap.py; run
#              ./bootstrap.sh --help for the full option list.
# ==============================================================================

set -euo pipefail

FRAMEWORK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! command -v python3 >/dev/null 2>&1; then
  echo "[ERROR] python3 is required to run the bootstrap." >&2
  exit 1
fi

exec python3 "$FRAMEWORK_DIR/bootstrap.py" "$@"
