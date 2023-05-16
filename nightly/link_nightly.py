#!/usr/bin/env python3

from pathlib import Path

import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to nightly directory")

    args = ap.parse_args()

    path = Path(args.path)

    def link(glob, target):

        source = max(i for i in path.glob(glob) if "-nightly-" not in i.name)
        target = path / target

        try:
            target.unlink()
        except FileNotFoundError:
            pass

        target.symlink_to(source.relative_to(path))

    link("8*", "current")
    link("8*", "current-8")
    link("7*", "current-7")
    link("8*/*-sdk.zip", "renpy-nightly-sdk.zip")
    link("8*/*-sdk.tar.bz2", "renpy-nightly-sdk.tar.bz2")

if __name__ == "__main__":
    main()
