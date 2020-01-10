#!/usr/bin/env python3

import sys
import argparse
import shutil
from pathlib import Path

sys.path.insert(1, Path(__file__).parent / 'deps')

import renpybuild.model
import tasks as _


def build(args):
    platforms = [ i.strip() for i in args.platforms.split(",")  ]
    archs = [ i.strip() for i in args.archs.split(",") ]
    pythons = [ i.strip() for i in args.pythons.split(",") ]

    for task in renpybuild.model.tasks:
        for platform in platforms:
            for arch in archs:
                for python in pythons:

                    context = renpybuild.model.Context(
                        platform, arch, python,
                        root,
                        tmp,
                        dist,
                        pygame_sdl2,
                        renpy)
                    task.run(context)

    print("")
    print("Build finished successfully.")


def remove_complete(args):

    complete = tmp / "complete"

    if not complete.is_dir():
        return

    for fn in complete.iterdir():
        name = fn.name.split(".")[0]
        taskname = name.rpartition("-")[2]

        if (name in args.tasks) or (taskname in args.tasks):
            fn.unlink()


def rebuild(args):

    remove_complete(args)
    build(args)


def clean(args):
    shutil.rmtree(tmp / "build")
    shutil.rmtree(tmp / "complete")

    for i in tmp.glob("install.*"):
        shutil.rmtree(i)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tmp", default="tmp")
    ap.add_argument("--dist", default="dist")
    ap.add_argument("--pygame_sdl2", default="pygame_sdl2")
    ap.add_argument("--renpy", default="renpy")

    ap.add_argument("--platforms", "--platform", default="linux")
    ap.add_argument("--archs", "--arch", default="x86_64")
    ap.add_argument("--pythons", "--python", default="2")
    ap.set_defaults(function=build)

    subparsers = ap.add_subparsers()

    sp = subparsers.add_parser("build")
    sp.set_defaults(function=build)

    sp = subparsers.add_parser("rebuild")
    sp.add_argument("tasks", nargs='+')
    sp.set_defaults(function=rebuild)

    sp = subparsers.add_parser("clean")
    sp.set_defaults(function=clean)

    global tmp
    global root
    global dist
    global pygame_sdl2
    global renpy

    args = ap.parse_args()

    tmp = Path(args.tmp).resolve()
    root = Path(__file__).parent.resolve()

    dist = Path(args.dist).resolve()
    pygame_sdl2 = Path(args.pygame_sdl2).resolve()
    renpy = Path(args.renpy).resolve()

    args.function(args)


if __name__ == "__main__":
    main()
