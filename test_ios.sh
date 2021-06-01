#!/bin/bash

set -e

./build.py --platform ios
./renpy/run.sh ./renpy/launcher ios_populate ${1:-./renpy/the_question} ./renios/prototype/

rsync -a renios/prototype tom@mary21.local:/Users/tom/ios
