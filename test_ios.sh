#!/bin/bash

set -e

# This modifies the renios/buildlib/create.py to use the prototype credentials.
export RENPY_TEST_IOS=1

./build.sh --platform ios --python 3 rebuild renios

rm -Rf /tmp/ios-test

rm renpy/renios || true
ln -s renios3 renpy/renios

./renpy/renpy3.sh ./renpy/launcher ios_create ${1:-./renpy/the_question} /tmp/ios-test

# rsync -a --delete --exclude \*.xcodeproj /tmp/ios-test tom@mary21.local:/Users/tom/ios
rsync -a --delete /tmp/ios-test tom@mary21.local:/Users/tom/ios
rsync -a --delete /tmp/ios-test tom@mary12.local:/Users/tom/ios
