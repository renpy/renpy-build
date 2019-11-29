#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path

sys.path.insert(1, Path(__file__).parent / 'deps')

import renpybuild.model

# The tasks to run, in order.
__import__("tasks.sysroot")
__import__("tasks.zlib")
__import__("tasks.bzip2")
__import__("tasks.openssl")
__import__("tasks.nasm")


def build(args):
    platforms = [ i.strip() for i in args.platforms.split(",")  ]
    archs = [ i.strip() for i in args.archs.split(",") ]
    pythons = [ i.strip() for i in args.pythons.split(",") ]

    for task in renpybuild.model.tasks:
        for platform in platforms:
            for arch in archs:
                for python in pythons:
                    context = renpybuild.model.Context(platform, arch, python, root, tmp)
                    task.run(context)


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tmp", default="tmp")
    ap.add_argument("--platforms", "--platform", default="linux")
    ap.add_argument("--archs", "--arch", default="x86_64")
    ap.add_argument("--pythons", "--python", default="3,2")

    subparsers = ap.add_subparsers()

    sp = subparsers.add_parser("build")
    sp.set_defaults(function=build)

    sp = subparsers.add_parser("rebuild")
    sp.add_argument("tasks", nargs='+')
    sp.set_defaults(function=rebuild)

    global tmp
    global root

    args = ap.parse_args()

    tmp = Path(args.tmp).resolve()
    root = Path(__file__).parent.resolve()

    args.function(args)


if __name__ == "__main__":
    main()

