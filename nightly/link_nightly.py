#!/usr/bin/env python3

from pathlib import Path

import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to nightly directory")

    args = ap.parse_args()

    path = Path(args.path)

    def link(glob, target):
        print(list(sorted(path.glob(glob))))

        source = max(path.glob(glob))
        target = path / target

        try:
            target.unlink()
        except FileNotFoundError:
            pass

        target.symlink_to(source.relative_to(path))

    link("8-nightly-*", "current")
    link("8-nightly-*", "current-8")
    link("7-nightly-*", "current-7")

    link("current/*-sdk.zip", "renpy-nightly-sdk.zip")
    link("current/*-sdk.tar.bz2", "renpy-nightly-sdk.tar.bz2")



if __name__ == "__main__":
    main()
