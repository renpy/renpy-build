#!/bin/bash

set -e

if [ ! -e $VENV/bin ]; then
    python2 -m virtualenv $VENV
fi

. $VENV/bin/activate

pip install -r $ROOT/requirements.txt

if [ -L $VENV/local/include/python2.7 ] ; then
    pushd $BASE/pygame_sdl2
    python2 ./fix_virtualenv.py
    popd
fi

pushd $BASE/pygame_sdl2
python setup.py install_headers
popd

pushd $BASE/renpy
./run.sh launcher quit
popd
