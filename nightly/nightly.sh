#!/bin/bash

set -e

# Set up the environment variables.

SCRIPTS=$(cd $(dirname $0); pwd)
ROOT="$SCRIPTS/.."
REFS=$ROOT

eval set -- $(getopt -o '' --long upload,nosign,prune -- "$@")

DISTRIBUTE_ARGS=

while true; do
    case $1 in
        --)
            shift
            break
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
    echo "usage: $0 ./path/to/nightly-build"
    exit
fi

BASE="$1"

. $SCRIPTS/git.sh

. $SCRIPTS/rev.sh
. $SCRIPTS/build.sh
. $SCRIPTS/web.sh
