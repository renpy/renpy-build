#!/bin/bash

set -e

# This modifies the renios/buildlib/create.py to use the prototype credentials.
export RENPY_TEST_IOS=1

./build.sh --platform ios rebuild renios

rm -Rf /tmp/ios-test

./renpy/renpy.sh ./renpy/launcher ios_create ${1:-./renpy/the_question} /tmp/ios-test

# rsync -a --delete --exclude \*.xcodeproj /tmp/ios-test tom@mary21.local:/Users/tom/ios
rsync -a --delete /tmp/ios-test tom@mary21.local:/Users/tom/ios
# rsync -a --delete /tmp/ios-test tom@mary12.local:/Users/tom/ios
