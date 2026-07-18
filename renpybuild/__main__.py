import argparse
import shutil
import sys
from pathlib import Path

import renpybuild.task
from renpybuild.context import Context

import tasks as tasks

known_platforms = []

# Platform Registry ############################################################


class Platform:
    def __init__(self, platform, arch, experimental=False):
        self.platform = platform
        self.arch = arch
        self.experimental = experimental

        known_platforms.append(self)


Platform("linux", "x86_64")
Platform("linux", "aarch64")

Platform("windows", "x86_64")

Platform("mac", "x86_64")
Platform("mac", "arm64")

Platform("android", "x86_64")
Platform("android", "arm64_v8a")
Platform("android", "armeabi_v7a")

Platform("ios", "arm64")
Platform("ios", "sim-x86_64")
Platform("ios", "sim-arm64")

Platform("web", "wasm")


def build(args):

    platforms = set(i.strip() for i in args.platforms.split(",") if i)
    archs = set(i.strip() for i in args.archs.split(",") if i)

    # Check that the platforms, archs are known.

    for i in platforms:
        if i not in {j.platform for j in known_platforms}:
            print("Platform", i, "is not known.", file=sys.stderr)
            sys.exit(1)

    for i in archs:
        if i not in {j.arch for j in known_platforms}:
            print("Architecture", i, "is not known.", file=sys.stderr)
            sys.exit(1)

    # Actually build everything.

    last_task = None

    if args.stop:
        for task in renpybuild.task.tasks:
            if task.name == args.stop:
                last_task = task

    for task in renpybuild.task.tasks:
        for p in known_platforms:
            if platforms and (p.platform not in platforms):
                continue

            if archs and (p.arch not in archs):
                continue

            context = Context(p.platform, p.arch, root, args)

            task.run(context)

        if task is last_task:
            break

    print("")
    print("Build finished successfully.")


def remove_complete(args):

    tmp = root / os.environ.get("RENPY_BUILD_TMP", "tmp")
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

    def rmtree(p: Path):
        if p.exists():
            shutil.rmtree(p)

    tmp = root / os.environ.get("RENPY_BUILD_TMP", "tmp")

    rmtree(tmp / "build")
    rmtree(tmp / "complete")
    rmtree(tmp / "host")
    rmtree(tmp / "source")

    for i in tmp.glob("install.*"):
        rmtree(i)

    rmtree(root / "renpy" / "tmp" / "gen3")
    rmtree(root / "renpy" / "tmp" / "gen3-static")

    rmtree(root / "renpy" / "web")
    rmtree(root / "renpy" / "renios")
    rmtree(root / "renpy" / "rapt")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--platforms", "--platform", default="")
    ap.add_argument("--archs", "--arch", default="")

    ap.add_argument("--nostrip", action="store_true", default=False)
    ap.add_argument("--sdl", action="store_true", default=False, help="Do not clean SDL on rebuild.")

    ap.add_argument("--experimental", action="store_true", default=False)

    ap.add_argument("--stop", default=None, help="Stop after this task.")

    ap.set_defaults(function=build)

    subparsers = ap.add_subparsers()

    sp = subparsers.add_parser("build")
    sp.set_defaults(function=build)

    sp = subparsers.add_parser("rebuild")
    sp.add_argument("tasks", nargs="+")
    sp.set_defaults(function=rebuild)

    sp = subparsers.add_parser("clean")
    sp.set_defaults(function=clean)

    global root

    args = ap.parse_args()

    if not args.experimental:
        known_platforms[:] = [i for i in known_platforms if not i.experimental]

    root = Path(__file__).parent.parent.resolve()

    args.function(args)


if __name__ == "__main__":
    import os

    if os.environ.get("PYTHONHASHSEED") is None:
        os.environ["PYTHONHASHSEED"] = "0"
        os.execv(sys.executable, sys.orig_argv)
        # script will now re-execute with new hash seed

    main()
