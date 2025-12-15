#!/bin/bash
# docker-entrypoint.sh

set -e

BASE="/build"
VENV="$BASE/renpy/.venv"

# Ensure PATH includes UV
export PATH="/root/.local/bin:$PATH"
export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/

# If renpy directory is empty, show error
if [ ! -d "$BASE/renpy/.git" ]; then
    echo "ERROR: Ren'Py repository not mounted!"
    echo "Please mount your Ren'Py clone at /build/renpy"
    echo ""
    echo "Example:"
    echo "  docker run -v \$(pwd)/renpy:/build/renpy renpy-build ..."
    exit 1
fi

# Set up Python venv if not exists or is incomplete
setup_venv() {
    echo "Setting up Python virtual environment..."

    pushd "$BASE/renpy" > /dev/null

    # Run uv sync to create/update venv
    uv sync

    # Source the venv
    . "$VENV/bin/activate"

    # Delete generated files (from python.sh)
    rm -Rf renpy/module/gen-static
    rm -Rf renpy/module/gen3-static
    rm -Rf renpy/module/gen
    rm -Rf renpy/module/gen3

    # Run launcher once to generate files
    ./run.sh launcher quit || true

    popd > /dev/null

    echo "Python environment ready"
}

# Check if venv needs setup
if [ ! -f "$VENV/bin/activate" ]; then
    echo "Virtual environment not found, creating..."
    setup_venv
elif [ ! -f "$VENV/pyvenv.cfg" ]; then
    echo "Virtual environment incomplete, recreating..."
    setup_venv
else
    . "$VENV/bin/activate"
fi

case "$1" in
    bash|sh)
        exec "$@"
        ;;

    *)
        cd "$BASE"
        exec ./build.sh "$@"
        ;;
esac
