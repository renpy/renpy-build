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

rm -Rf Python-3.12.8-build

if [ ! -e Python-3.12.8 ]; then
    tar xaf ../../source/Python-3.12.8.tar.xz
fi

cp -a Python-3.12.8 Python-3.12.8-build

./opfunc_transform.py Python-3.12.8-build/Python/ceval.c

export CC="ccache clang"
export LD="ccache clang"

if [ $BUILD = yes ]; then
    pushd Python-3.12.8-build
    ./configure --with-pydebug --cache-file=../config.cache > python.log
    nice make -j$(nproc) >> python.log
    echo "Python build complete."

    if [ $TEST = yes ]; then
        make test
    fi

    popd
fi
