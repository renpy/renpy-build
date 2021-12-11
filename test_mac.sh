#!/bin/bash

# Copy the files needed to run a project to a mac.

set -ex

mac=$1
path = $2

if [ -z "$mac" -o -z "$path" ]; then
    echo "Usage: $0 <mac> <path>"
    exit 1
fi

sync() {
    rsync -a /home/tom/ab/renpy-build/renpy/$1 $mac:$path/$2
}

sync launcher/ launcher
sync lib2/ lib
sync rapt2/ rapt
sync renios2/ renios
sync renpy/ renpy
sync renpy.app/ renpy.app
sync renpy.py renpy.py
sync renpy.sh renpy.sh
sync the_question/ the_question
sync tutorial/ tutorial
