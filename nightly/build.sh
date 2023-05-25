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

if [ "$CLEAN" = 1 ]; then
    ./build.py clean
fi

./build.py --python 2
./build.py --python 3
popd


link () {
    if [ -e $1 -a ! -L $2 ]; then
        ln -s $1 $2
    fi
}

weblink() {
    rm $2 || true
    ln -s $1 $2
}

pushd $BASE/renpy

rm -f rapt renios
ln -s rapt2 rapt
ln -s renios2 renios

# Update the README.
cp /home/tom/ab/renpy-deps/scripts/README.nightly /home/tom/ab/WWW.nightly/README.txt

link $BASE/pygame_sdl2 pygame_sdl2
link $BASE/live2d live2d
link /home/tom/ab/WWW.nightly dl
link /home/tom/ab/renpy/atom atom
link /home/tom/ab/renpy/jedit jedit
link /home/tom/ab/renpy/editra editra

# Generate source.

export RENPY_CYTHON=cython
export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/
export RENPY_SIMPLE_EXCEPTIONS=1

./renpy.sh tutorial quit

# Build the documentation.
pushd $BASE/renpy/sphinx
./build.sh
popd

# Get the versions.
PY3_VERSION=$(./lib/py3-linux-x86_64/python -O distribute.py --print-version --nightly)
PY2_VERSION=$(./lib/py2-linux-x86_64/python -O distribute.py --print-version --nightly)

if [ -e renpy/dl/$PY3_VERSION/branch.txt -a -e renpy/dl/$PY2_VERSION/branch.txt ]; then
    echo "Already built."
else
    # Build the distribution.
    ./lib/py3-linux-x86_64/python -O distribute.py --pygame $BASE/pygame_sdl2 $DISTRIBUTE_ARGS --nightly
    ./lib/py2-linux-x86_64/python -O distribute.py --pygame $BASE/pygame_sdl2 $DISTRIBUTE_ARGS --nightly

    # Copy VCS data to distribution directories.
    pushd $BASE
    cp tmp/vcs8.json renpy/dl/$PY3_VERSION/vcs.json
    cp tmp/vcs7.json renpy/dl/$PY2_VERSION/vcs.json

    echo $BRANCH > renpy/dl/$PY3_VERSION/branch.txt
    echo $BRANCH > renpy/dl/$PY2_VERSION/branch.txt

    date +%Y-%m-%d > renpy/dl/$PY3_VERSION/date.txt
    date +%Y-%m-%d > renpy/dl/$PY2_VERSION/date.txt

    popd
fi


popd # $BASE/renpy

# Make symlinks.
pushd $BASE/renpy/dl

weblink $PY3_VERSION current-8-$BRANCH
weblink $PY2_VERSION current-7-$BRANCH

if [ $BRANCH = main -o $BRANCH = master ]; then
    weblink $PY3_VERSION current
    weblink $PY3_VERSION current-8
    weblink $PY2_VERSION current-7
fi

popd
