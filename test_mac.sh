#!/bin/bash

# Copy the files needed to run a project to a mac.

set -ex

mac=$1
path=$2

if [ -z "$mac" -o -z "$path" ]; then
    echo "Usage: $0 <mac> <path>"
    exit 1
fi

sync() {
    rsync -a /home/tom/ab/renpy-build/renpy/$1 $mac:$path/$2
}

rpy build --platform mac

sync launcher/ launcher
sync lib/ lib
sync rapt/ rapt
sync renios/ renios
sync renpy/ renpy
sync renpy.app/ renpy.app
sync renpy.py renpy.py
sync renpy.sh renpy.sh
sync sdk-fonts/ sdk-fonts
sync the_question/ the_question
sync tutorial/ tutorial
