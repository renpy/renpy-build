#!/bin/bash

set -e

uv sync

. $RENPY_VIRTUAL_ENV/bin/activate

# Delete the generated files.
rm -Rf renpy/module/gen3-static
rm -Rf renpy/module/gen3

./renpy/run.sh renpy/launcher quit
