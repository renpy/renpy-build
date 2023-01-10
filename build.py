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

    def __init__(self, platform, arch, python, experimental=False):
        self.platform = platform
        self.arch = arch
        self.python = python
        self.experimental = experimental

        known_platforms.append(self)


# Python 2

Platform("linux", "x86_64", "2")
Platform("linux", "i686", "2")
Platform("linux", "aarch64", "2")
Platform("linux", "armv7l", "2")

Platform("windows", "x86_64", "2")
Platform("windows", "i686", "2")

Platform("mac", "x86_64", "2")
Platform("mac", "arm64", "2")

Platform("android", "x86_64", "2")
Platform("android", "arm64_v8a", "2")
Platform("android", "armeabi_v7a", "2")

Platform("ios", "arm64", "2")
Platform("ios", "sim-x86_64", "2")
Platform("ios", "sim-arm64", "2")

Platform("web", "wasm", "2")

# Python 3

Platform("linux", "x86_64", "3")
Platform("linux", "aarch64", "3")
Platform("linux", "armv7l", "3")

Platform("windows", "x86_64", "3")

Platform("mac", "x86_64", "3")
Platform("mac", "arm64", "3")

Platform("android", "x86_64", "3")
Platform("android", "arm64_v8a", "3")
Platform("android", "armeabi_v7a", "3")

Platform("ios", "arm64", "3")
Platform("ios", "sim-x86_64", "3")
Platform("ios", "sim-arm64", "3")

Platform("web", "wasm", "3")

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
        if i not in { j.python for j in known_platforms }:
            print("Python", i, "is not known.", file=sys.stderr)
            sys.exit(1)

    # Actually build everything.

    for task in renpybuild.model.tasks:
        for p in known_platforms:

            if platforms and (p.platform not in platforms):
                continue

            if archs and (p.arch not in archs):
                continue

            if pythons and (p.python not in pythons):
                continue

            platform = p.platform
            arch = p.arch
            python = p.python

            context = renpybuild.model.Context(
                p.platform,
                p.arch,
                p.python,
                root,
                tmp,
                pygame_sdl2,
                renpy,
                args)

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
    shutil.rmtree(tmp / "host")

    try:
        shutil.rmtree(tmp / "source")
    except:
        pass

    for i in tmp.glob("install.*"):
        shutil.rmtree(i)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tmp", default="tmp")
    ap.add_argument("--pygame_sdl2", default="pygame_sdl2")
    ap.add_argument("--renpy", default="renpy")

    ap.add_argument("--platforms", "--platform", default="")
    ap.add_argument("--archs", "--arch", default="")
    ap.add_argument("--pythons", "--python", default="3")

    ap.add_argument("--nostrip", action="store_true", default=False)
    ap.add_argument("--sdl", action="store_true", default=False, help="Do not clean SDL on rebuild.")

    ap.add_argument("--experimental", action="store_true", default=False)

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

    if not args.experimental:
        known_platforms[:] = [ i for i in known_platforms if not i.experimental ]

    tmp = Path(args.tmp).resolve()
    root = Path(__file__).parent.resolve()

    pygame_sdl2 = Path(args.pygame_sdl2).resolve()
    renpy = Path(args.renpy).resolve()

    args.function(args)


if __name__ == "__main__":
    main()
