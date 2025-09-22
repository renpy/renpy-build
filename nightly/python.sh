#!/bin/bash

set -e

uv sync

. $VENV/bin/activate

# Delete the generated files.
rm -Rf renpy/module/gen3-static
rm -Rf renpy/module/gen3

./renpy/run.sh launcher quit
