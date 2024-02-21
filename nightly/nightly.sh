#!/bin/bash

set -e

# Set up the environment variables.

SCRIPTS=$(cd $(dirname $0); pwd)
ROOT="$SCRIPTS/.."
REFS=$ROOT

eval set -- $(getopt -o '' --long clean,upload,nosign,prune -- "$@")

DISTRIBUTE_ARGS=

while true; do
    case $1 in
        --)
            shift
            break
            ;;

        --clean)
            CLEAN=1
            shift
            ;;

        --upload)
            UPLOAD=1
            shift
            ;;

        --nosign)
            DISTRIBUTE_ARGS="$DISTRIBUTE_ARGS --nosign"
            shift
            ;;

        --prune)
            PRUNE=1
            shift
            ;;
    esac
done


if [ -z "$1" ]; then
    echo "usage: $0 <./path/to/nightly-build> <branch>"
    exit
fi

BASE="$1"
VENV="$1/tmp/virtualenv.py3"
BRANCH="${2:-master}"

export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/

. $SCRIPTS/git.sh

mkdir -p "$BASE/tmp"

# Clean, if required.

if [ "$CLEAN" = 1 ]; then
    pushd $BASE
    ./build.py clean
    popd
fi

# Python activates the venv, which is needed for the rest of it.
. $SCRIPTS/python.sh
. $SCRIPTS/rev.sh
. $SCRIPTS/build.sh
. $SCRIPTS/web.sh
