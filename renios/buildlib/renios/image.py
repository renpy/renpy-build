
from __future__ import division, absolute_import, with_statement, print_function, unicode_literals
from renpy.compat import PY2, basestring, bchr, bord, chr, open, pystr, range, str, tobytes, unicode # *

import pygame_sdl2
import os
import argparse
import json

def smoothscale(surf, size):

    while True:
        w, h = surf.get_size()

        if (w == size[0]) and (h == size[1]):
            break

        w = max(w // 2, size[0])
        h = max(h // 2, size[1])

        surf = pygame_sdl2.transform.smoothscale(surf, (w, h))

    return surf


def generate(source, destination, scale):

    if not os.path.exists(source):
        return

    src = pygame_sdl2.image.load(source).convert_alpha()
    sw, sh = src.get_size()

    with open(os.path.join(destination, "Contents.json"), "r") as f:
        contents = json.load(f)

    for i in contents["images"]:

        if "filename" not in i:
            continue

        dfn = os.path.join(destination, i['filename'])

        dst = pygame_sdl2.image.load(dfn)
        dst.convert_alpha()

        w, h = dst.get_size()

        if scale:

            dst = smoothscale(src, (w, h))

        else:

            dst.fill(dst.get_at((0, 0)))

            xo = int(w / 2) - int(sw / 2)
            yo = int(h / 2) - int(sh / 2)

            dst.blit(src, (xo, yo))

        pygame_sdl2.image.save(dst, dfn)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("destination")
    ap.add_argument("--scale", action="store_true")

    args = ap.parse_args()

    pygame_sdl2.display.init()
    pygame_sdl2.display.set_mode((640, 480))
    pygame_sdl2.event.pump()

    generate(args.source, args.destination, args.scale)


if __name__ == "__main__":
    main()
