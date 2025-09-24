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
python -m renpybuild --python 3
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
ln -s rapt3 rapt
ln -s renios3 renios

# Update the README.
cp /home/tom/ab/renpy-deps/scripts/README.nightly /home/tom/ab/WWW.nightly/README.txt

link $BASE/live2d live2d
link /home/tom/ab/WWW.nightly dl
link /home/tom/ab/renpy/atom atom
link /home/tom/ab/renpy/jedit jedit
link /home/tom/ab/renpy/editra editra
link /home/tom/ab/keys/update.pem update.pem

# Generate source.

export RENPY_CYTHON=cython
export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/
export RENPY_SIMPLE_EXCEPTIONS=1

./renpy3.sh tutorial quit

# Build the documentation.
pushd $BASE/renpy/sphinx
./build.sh
popd

# Get the versions.
PY3_VERSION=$(./lib/py3-linux-x86_64/python -O distribute.py --print-version --nightly)

if [ -e renpy/dl/$PY3_VERSION/branch.txt ]; then
    echo "Already built."
else
    # Build the distribution.
    ./lib/py3-linux-x86_64/python -O distribute.py $DISTRIBUTE_ARGS --nightly

    # Copy VCS data to distribution directories.
    pushd $BASE
    cp tmp/vcs8.json renpy/dl/$PY3_VERSION/vcs.json

    cp -a renpy/doc-web renpy/dl/$PY3_VERSION/doc

    echo $BRANCH > renpy/dl/$PY3_VERSION/branch.txt

    date "+%s" > renpy/dl/$PY3_VERSION/timestamp.txt

    popd
fi


popd # $BASE/renpy

# Make symlinks.
pushd $BASE/renpy/dl

weblink $PY3_VERSION current-8-$BRANCH

if [ $BRANCH = main -o $BRANCH = master ]; then
    weblink $PY3_VERSION current
    weblink $PY3_VERSION current-8
fi

popd
