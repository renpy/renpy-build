#!/usr/bin/env python3

import sys
import argparse
import shutil
from pathlib import Path

sys.path.insert(1, Path(__file__).parent / 'deps')

import renpybuild.model
import tasks as _

known_platforms = [ ]

# Platform Registry ############################################################


class Platform:

    def __init__(self, platform, arch):
        self.platform = platform
        self.arch = arch

        known_platforms.append(self)


Platform("linux", "x86_64")
Platform("linux", "i686")
Platform("linux", "armv7l")

Platform("windows", "x86_64")
Platform("windows", "i686")

Platform("mac", "x86_64")

Platform("android", "x86_64")
Platform("android", "arm64_v8a")
Platform("android", "armeabi_v7a")

Platform("ios", "arm64")
Platform("ios", "armv6s")

# Python Registry ##############################################################

known_pythons = [ ]


class Python:

    def __init__(self, python):
        self.python = python
        known_pythons.append(self)


Python("2")


def build(args):
    platforms = set(i.strip() for i in args.platforms.split(",") if i)
    archs = set(i.strip() for i in args.archs.split(",") if i)
    pythons = set(i.strip() for i in args.pythons.split(",") if i)

    # Check that the platforms, archs, and pythons are known.

    for i in platforms:
        if i not in { j.platform for j in known_platforms }:
            print("Platform", i, "is not known.", file=sys.stderr)
            sys.exit(1)

    for i in archs:
        if i not in { j.arch for j in known_platforms }:
            print("Architecture", i, "is not known.", file=sys.stderr)
            sys.exit(1)

    for i in pythons:
        if i not in { j.python for j in known_pythons }:
            print("Python", i, "is not known.", file=sys.stderr)
            sys.exit(1)

    # Actually build everything.

    for task in renpybuild.model.tasks:
        for p in known_platforms:

            if platforms and (p.platform not in platforms):
                continue

            if archs and (p.arch not in archs):
                continue

            platform = p.platform
            arch = p.arch

            for py in known_pythons:

                if pythons and (py.python not in pythons):
                    continue

                python = py.python

                context = renpybuild.model.Context(
                    platform, arch, python,
                    root,
                    tmp,
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
    ap.add_argument("--pygame_sdl2", default="pygame_sdl2")
    ap.add_argument("--renpy", default="renpy")

    ap.add_argument("--platforms", "--platform", default="")
    ap.add_argument("--archs", "--arch", default="")
    ap.add_argument("--pythons", "--python", default="")

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
    global pygame_sdl2
    global renpy

    args = ap.parse_args()

    tmp = Path(args.tmp).resolve()
    root = Path(__file__).parent.resolve()

    pygame_sdl2 = Path(args.pygame_sdl2).resolve()
    renpy = Path(args.renpy).resolve()

    args.function(args)


if __name__ == "__main__":
    main()
