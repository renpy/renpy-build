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

pushd $BASE

./all.sh

popd
