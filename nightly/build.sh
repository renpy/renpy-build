#!/bin/bash

# Symlink in the tars.
if [ $ROOT != $BASE ]; then
    for i in $ROOT/tars/*; do
        i=$(basename $i)

        if [ ! -e $BASE/tars/$i ]; then
            ln -s $ROOT/tars/$i $BASE/tars/$i
        fi
    done
fi

# Build the dependencies.
pushd $BASE
./build.py
popd


link () {
    if [ -e $1 -a ! -L $2 ]; then
        ln -s $1 $2
    fi
}

pushd $BASE/renpy

rm -f lib rapt renios
ln -s lib2 lib
ln -s rapt2 rapt
ln -s renios2 renios

# Update the README.
cp /home/tom/ab/renpy-deps/scripts/README.nightly /home/tom/ab/WWW.nightly/README.txt

# Activate the virtualenv for the prebuild.
. /home/tom/.virtualenvs/nightlyrenpy/bin/activate

# Run the after checkout script.
# ./after_checkout.sh

link $BASE/pygame_sdl2 pygame_sdl2
link $BASE/live2d live2d
link /home/tom/ab/WWW.nightly dl
link /home/tom/ab/renpy/atom atom
link /home/tom/ab/renpy/jedit jedit
link /home/tom/ab/renpy/editra editra

# Figure out a reasonable version name.
REV=$(git rev-parse --short HEAD)
BRANCH=$(git rev-parse --abbrev-ref HEAD)

export RENPY_NIGHTLY="nightly-$(date +%Y-%m-%d)-$REV"

# Generate source.

export RENPY_CYTHON=cython
export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/
export RENPY_SIMPLE_EXCEPTIONS=1

./renpy.sh tutorial quit

# Build the documentation.
# pushd $BASE/renpy/sphinx
# ./build.sh
# popd

# Build the distribution.
./lib/linux-x86_64/python -O distribute.py "$RENPY_NIGHTLY" --pygame $BASE/pygame_sdl2 $DISTRIBUTE_ARGS

popd

