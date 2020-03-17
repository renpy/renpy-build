#!/bin/bash

set -e

./build.py --platform ios rebuild renios pyobjus
./renpy/run.sh ./renpy/launcher ios_populate ./renpy/the_question ./renios/prototype/
ssh tom@mary12 -t /Volumes/shared/ab/renpy-build/run_ios.sh
