#!/bin/bash

set -e

pushd $BASE/renpy

uv sync

. $VENV/bin/activate

# Delete the generated files.
rm -Rf renpy/module/gen-static
rm -Rf renpy/module/gen3-static
rm -Rf renpy/module/gen
rm -Rf renpy/module/gen3

./run.sh launcher quit
popd
