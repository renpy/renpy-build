#!/bin/bash

set -e

if [ ! -e $VENV/bin ]; then
    python2 -m virtualenv $VENV
fi

. $VENV/bin/activate

pip install -r $ROOT/requirements.txt

pushd $BASE/pygame_sdl2
python2 ./fix_virtualenv.py || true
popd

pushd $BASE/pygame_sdl2
python setup.py install_headers
popd

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
