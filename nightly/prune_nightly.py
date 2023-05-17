#!/usr/bin/env python3

import argparse
import datetime
import shutil
from pathlib import Path

import re


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to nightly directory")
    args = ap.parse_args()

    path = Path(args.path)

    for dn in path.iterdir():

        if not dn.is_dir():
            continue

        m = re.search('20(\d{2})-(\d{2})-(\d{2})', dn.name)

        if not m:
            m = re.search('\d+\.(\d{2})(\d{2})(\d{2})', dn.name)
            continue

        date = datetime.date(2000 + int(m.group(1)), int(m.group(2)), int(m.group(3)))
        age = datetime.date.today() - date

        if age.days < 30:
            continue
        if age.days < 180 and date.weekday() == 0:
            continue

        shutil.rmtree(dn)

if __name__ == "__main__":
    main()
