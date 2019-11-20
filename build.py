#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path

sys.path.insert(1, Path(__file__).parent / 'deps')

from renpybuild.model import task
import renpybuild.model


@task()
def unpack_python(c):
    print("Test.")


@task(kind="python")
def build_python(c):
    print("Build.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("platform")
    ap.add_argument("arch")
    ap.add_argument("python")
    ap.add_argument("--tmp", default="/tmp/renpy-build")

    args = ap.parse_args()

    tmp = Path(args.tmp)

    platforms = [ i.strip() for i in args.platform.split(",")  ]
    archs = [ i.strip() for i in args.arch.split(",") ]
    pythons = [ i.strip() for i in args.python.split(",") ]

    for task in renpybuild.model.tasks:
        for platform in platforms:
            for arch in archs:
                for python in pythons:
                    context = renpybuild.model.Context(platform, arch, python, tmp)
                    task.run(context)


if __name__ == "__main__":
    main()

