#!/bin/bash

./build.py --platform ios
./renpy/run.sh ./renpy/launcher ios_populate ./renpy/the_question ./renios/prototype/
