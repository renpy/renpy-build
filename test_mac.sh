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
sync rapt3/ rapt
sync renios3/ renios
sync renpy/ renpy
sync renpy3.app/ renpy.app
sync renpy3.app/ renpy3.app
sync renpy2.app/ renpy2.app
sync renpy.py renpy.py
sync renpy3.sh renpy.sh
sync sdk-fonts/ sdk-fonts
sync the_question/ the_question
sync tutorial/ tutorial
