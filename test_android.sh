#!/bin/bash

set -e

PY=$(python -c 'import sys; print(sys.version[0])')


ROOT="$(dirname $(readlink -f $0))"

pushd "$ROOT"
./build.py --python $PY --platform android rebuild rapt rapt-sdl2
popd

rm "$ROOT/renpy/rapt"
ln -s "rapt$PY" "$ROOT/renpy/rapt"

export PYTHONPATH="$ROOT/renpy"


rm -Rf "$ROOT/renpy/rapt/Sdk"
ln -s "/home/tom/ab/android/Sdk" "$ROOT/renpy/rapt/Sdk"
mkdir -p "$ROOT/renpy/rapt/project"
cp -a /home/tom/ab/keys/local.properties "$ROOT/renpy/rapt/project"
cp -a /home/tom/ab/keys/bundle.properties "$ROOT/renpy/rapt/project"

pushd "$ROOT/renpy/rapt"
export RAPT_NO_TERMS=1
python android.py installsdk
popd

adb shell input keyevent KEYCODE_HOME || true

if [ "$1" != "" ]; then
    $ROOT/renpy/renpy3.sh $ROOT/renpy/launcher android_build "$1" --bundle --launch
fi


# ## This tests app switching.
#
# sleep 5
# adb shell input keyevent KEYCODE_HOME || true
# sleep 1
# adb shell input keyevent KEYCODE_APP_SWITCH || true
# sleep 1
# adb shell input tap 500 500 || true
