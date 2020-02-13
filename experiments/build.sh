#!/bin/bash

set -e

cp main.c SDL2-2.0.10/build/org.renpy.sdl2test/app/jni/src/main.c
pushd SDL2-2.0.10/build/org.renpy.sdl2test
./gradlew installDebug
popd

$ANDROID_HOME/platform-tools/adb shell am start org.renpy.sdl2test/.sdl2testActivity
