#!/usr/bin/env bash

# Run the Dash test suite inside the project virtual environment.
# Exit 0 when all tests pass, 1 otherwise (for CI integration).

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

activate_venv() {
    if [ -f "venv/bin/activate" ]; then
        # shellcheck source=/dev/null
        source "venv/bin/activate"
    elif [ -f "venv/Scripts/activate" ]; then
        # shellcheck source=/dev/null
        source "venv/Scripts/activate"
    elif [ -f ".venv/bin/activate" ]; then
        # shellcheck source=/dev/null
        source ".venv/bin/activate"
    elif [ -f ".venv/Scripts/activate" ]; then
        # shellcheck source=/dev/null
        source ".venv/Scripts/activate"
    else
        echo "Error: virtual environment not found." >&2
        echo "Create one with: python -m venv venv && pip install -r requirements.txt" >&2
        return 1
    fi
}

if ! activate_venv; then
    exit 1
fi

if pytest test_app.py -v; then
    exit 0
else
    exit 1
fi
