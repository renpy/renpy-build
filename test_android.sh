#!/bin/bash

set -e


ROOT="$(dirname $(readlink -f $0))"

pushd "$ROOT"
./build.py --platform android --arch x86_64
popd

rm -f "$ROOT/renpy/rapt/Sdk"
ln -s "/home/tom/ab/android/Sdk" "$ROOT/renpy/rapt/Sdk"
mkdir -p "$ROOT/renpy/rapt/project"
cp -a /home/tom/ab/android/local.properties "$ROOT/renpy/rapt/project"

pushd "$ROOT/renpy/rapt"
export PGS4A_NO_TERMS=1
python android.py installsdk
popd

rm -Rf "$ROOT/renpy/rapt/prototype/renpyandroid/src/main/java" || true
cp -aL rapt/prototype/renpyandroid/src/main/java $ROOT/renpy/rapt/prototype/renpyandroid/src/main/

if [ "$1" != "" ]; then
    $ROOT/renpy/renpy.sh $ROOT/renpy/launcher android_build "$1" installDebug --launch
fi
