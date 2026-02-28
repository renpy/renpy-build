#!/bin/bash

set -euo pipefail

BASE="/build"
cd "$BASE"

case "$1" in
    exec)
        shift
        exec "$@"
        ;;
    *)
        pushd "$BASE/renpy" > /dev/null

        uv sync

        popd > /dev/null

        uv --project renpy run -m renpybuild "$@"
        ;;
esac
