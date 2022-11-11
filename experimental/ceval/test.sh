#!/bin/bash

set -e

LONGOPTIONS=build,test
PARSED=$(getopt --options "" --longoptions=$LONGOPTIONS --name "$0" -- "$@")

eval set -- "$PARSED"

BUILD=no
TEST=no

while true; do
    case "$1" in
        --build)
            BUILD=yes
            shift
            ;;
        --test)
            TEST=yes
            shift
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "Internal error!"
            exit 1
            ;;
    esac
done

cd $(dirname $0)

rm -Rf Python-3.11.0
tar xaf ../../source/Python-3.11.0.tgz

./opfunc_transform.py Python-3.11.0/Python/ceval.c

export CC="ccache gcc"
export LD="ccache gcc"

if [ $BUILD = yes ]; then
    pushd Python-3.11.0
    ./configure --cache-file=../config.cache > python.log
    nice make -j$(nproc) >> python.log
    echo "Python build complete."

    if [ $TEST = yes ]; then
        make test
    fi

    popd
fi
