#!/bin/bash

update () {

    if [ -d "$BASE/$2/.git" ]; then
        pushd "$BASE/$2"
        git reset --hard
        git pull
        popd
    else
        git clone $1 "$BASE/$2" --reference "$REFS/$2"
    fi
}

update https://github.com/renpy/renpy-build

update https://github.com/renpy/renpy renpy

update https://github.com/renpy/pygame_sdl2 pygame_sdl2

update https://github.com/renpytom/live2dexperiment live2d


