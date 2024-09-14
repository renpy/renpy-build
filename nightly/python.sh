#!/bin/bash

set -e

if [ ! -e $VENV/bin ]; then
    python3 -m venv $VENV
fi

. $VENV/bin/activate

pip install -r $ROOT/requirements.txt

pushd $BASE/renpy

if [ ! -e pygame_sdl2 ]; then
    ln -s $BASE/pygame_sdl2 .
fi

# Delete the generated files.
rm -Rf renpy/module/gen-static
rm -Rf renpy/module/gen3-static
rm -Rf renpy/module/gen
rm -Rf renpy/module/gen3

rm -Rf pygame_sdl2/gen-static
rm -Rf pygame_sdl2/gen3-static
rm -Rf pygame_sdl2/gen
rm -Rf pygame_sdl2/gen3

./run.sh launcher quit
popd
