#!/bin/bash

update () {
    if [ -d "$BASE/$2/.git" ]; then
        pushd "$BASE/$2"
        git reset --hard
        git pull
        popd
    else
        if [ -e "$REFS/$2/.git" ]; then
            git clone $1 "$BASE/$2" --reference "$REFS/$2"
        else
            git clone $1 "$BASE/$2"
        fi
    fi
}

update https://github.com/renpy/renpy-build
update https://github.com/renpy/renpy renpy
update https://github.com/renpy/pygame_sdl2 pygame_sdl2
update https://github.com/renpy/renpyweb renpyweb

rm -Rf "$BASE/renpy/module/gen"
rm -Rf "$BASE/renpy/module/gen3"
rm -Rf "$BASE/renpy/module/gen-static"
rm -Rf "$BASE/renpy/module/gen30-static"

rm -Rf "$BASE/pygame_sdl2/gen"
rm -Rf "$BASE/pygame_sdl2/gen3"
rm -Rf "$BASE/pygame_sdl2/gen-static"
rm -Rf "$BASE/pygame_sdl2/gen3-static"

