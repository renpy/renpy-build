#!/bin/bash

set -e


ROOT="$(dirname $(readlink -f $0))"

pushd "$ROOT"
./build.py --platform android rebuild rapt rapt-sdl2
popd


rm -Rf "$ROOT/renpy/rapt/Sdk"
ln -s "/home/tom/ab/android/Sdk" "$ROOT/renpy/rapt/Sdk"
mkdir -p "$ROOT/renpy/rapt/project"
cp -a /home/tom/ab/android/local.properties "$ROOT/renpy/rapt/project"

pushd "$ROOT/renpy/rapt"
export RAPT_NO_TERMS=1
python android.py installsdk
popd

adb shell input keyevent KEYCODE_HOME || true

if [ "$1" != "" ]; then
    $ROOT/renpy/renpy.sh $ROOT/renpy/launcher android_build "$1" --bundle --launch
fi

