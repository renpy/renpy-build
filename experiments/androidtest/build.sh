#!/bin/bash

set -ex

./gradlew :app:bundleDebug

rm -f output.apks || true

java -jar bundletool.jar \
    build-apks \
    --bundle=app/build/outputs/bundle/debug/app-debug.aab \
    --output=output.apks \
    --local-testing

java -jar bundletool.jar \
    install-apks \
    --apks=output.apks
    
adb shell monkey -p org.renpy.androidtest 1
