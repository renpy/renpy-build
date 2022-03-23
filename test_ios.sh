#!/bin/bash

set -e

# This modifies the renios/buildlib/creat.py to use the prototype credentials.
export RENPY_TEST_IOS=1

./build.py --platform ios --arch arm64 --python 3 rebuild renios

rm -Rf /tmp/ios-test
./renpy/renpy3.sh ./renpy/launcher ios_create ${1:-./renpy/the_question} /tmp/ios-test

rsync -a --delete --exclude '*.xcodeproj' /tmp/ios-test tom@mary21.local:/Users/tom/ios
