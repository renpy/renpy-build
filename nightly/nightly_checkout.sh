#!/bin/bash

set -e

root=$(cd $(dirname $0)/..; pwd)
base=$1
reference=${2:-$root}

echo $root
echo $reference

if [ -z "$base" ]; then
    echo usage: $0 "<directory for nightly builds> <directory for references>"
    exit 1
fi

clone() {
    url=$1
    dir=$2

    if [ ! -d "$base/$dir" ]; then
        git clone $url "$base/$dir" --reference "$reference/$dir"
    fi
}

clone https://github.com/renpy/renpy-build
clone https://github.com/renpy/renpy renpy
clone https://github.com/renpy/pygame_sdl2 pygame_sdl2



