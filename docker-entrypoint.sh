#!/bin/bash

set -e

BASE="/build"

if [ ! -d "$BASE/renpy/.git" ]; then
    echo "ERROR: Ren'Py repository not mounted!"
    echo "Please mount your Ren'Py clone at /build/renpy"
    exit 1
fi

pushd "$BASE/renpy" > /dev/null

uv sync

./run.sh launcher quit

popd > /dev/null

cd "$BASE"
exec uv --project renpy run -m renpybuild "$@"
