#!/bin/bash

update () {
    if [ -d "$BASE/$2/.git" ]; then
        pushd "$BASE/$2"
        git reset --hard
        git checkout $BRANCH
        git pull
        popd
    else
        if [ -e "$REFS/$2/.git" ]; then
            if [ $REFS = $BASE ]; then
                git reset --hard
                git pull
            else
                git clone $1 "$BASE/$2" --reference "$REFS/$2"
            fi

            pushd "$BASE/$2"
            git checkout $BRANCH
            popd

        else
            git clone $1 "$BASE/$2"
            pushd "$BASE/$2"
            git checkout $BRANCH
            popd
        fi
    fi
}

update $(git remote get-url origin)
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
