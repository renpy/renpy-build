#!/bin/sh

SCRIPT="$0"

# Resolve the chain of symlinks leading to this script.
while [ -L "$SCRIPT" ] ; do
    LINK=$(readlink "$SCRIPT")

    case "$LINK" in
        /*)
            SCRIPT="$LINK"
            ;;
        *)
            SCRIPT="$(dirname "$SCRIPT")/$LINK"
            ;;
    esac
done

# The directory containing this shell script - an absolute path.
ROOT=$(dirname "$SCRIPT")
ROOT=$(cd "$ROOT"; pwd)

# The name of this shell script without the .sh on the end.
BASEFILE=$(basename "$SCRIPT" .sh)

if [ -z "$RENPY_PLATFORM" ] ; then
    RENPY_PLATFORM="$(uname -s)-$(uname -m)"

    case "$RENPY_PLATFORM" in
        Darwin-*|mac-*)
            RENPY_PLATFORM="mac-x86_64"
            ;;
        *-x86_64|amd64)
            RENPY_PLATFORM="linux-x86_64"
            ;;
        *-i*86)
            RENPY_PLATFORM="linux-i686"
            ;;
        Linux-*)
            RENPY_PLATFORM="linux-$(uname -m)"
            ;;
        *)
            ;;
    esac
fi

LIB="$ROOT/lib/$RENPY_PLATFORM"

if ! test -d "$LIB"; then
    echo "Ren'Py platform files not found in:"
    echo
    echo "$ROOT/lib/$RENPY_PLATFORM"
    echo
    echo "Please compile the platform files using the instructions in README.md"
    echo "or point them to an existing installation using ./after_checkout.sh <path>."
    echo
    echo "Alternatively, please set RENPY_PLATFORM to a different platform."
    exit 1
fi

exec $RENPY_GDB "$LIB/$BASEFILE" "$@"
