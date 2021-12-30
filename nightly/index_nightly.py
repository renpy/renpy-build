#!/usr/bin/env python

import datetime
import os.path
import argparse
import re
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    autoescape=select_autoescape(['html', 'xml']),
)


def directory(name, full):

    sdk = [ ]
    other = [ ]

    dirtime = 0

    for i in os.listdir(full):

        if i in [ ".build_cache", "updates.json", "updates.json.sig", "index.html" ]:
            continue

        if i.endswith(".update.gz"):
            continue

        if i.endswith("update.json"):
            continue

        if i.endswith(".sums"):
            continue

        if i.endswith(".zsync"):
            continue

        mtime = os.path.getmtime(os.path.join(full, i))
        dirtime = max(dirtime, mtime)

        dt = datetime.datetime.fromtimestamp(mtime)
        date = dt.strftime("%A, %B %d, %H:%M" )

        record = (
            i,
            round(os.path.getsize(os.path.join(full, i)) / 1024.0 / 1024, 1),
            date,
            )

        if "-sdk." in i:
            sdk.append(record)
        else:
            other.append(record)

    if not dirtime:
        return 0, None

    if not sdk:
        return 0, None

    dt = datetime.datetime.fromtimestamp(dirtime)
    date = dt.strftime("%A, %B %d, %Y")

    sdk.sort()
    other.sort()

    tmpl = env.get_template("nightly.html")
    html = tmpl.render(date=date, name=name, sdk=sdk, other=other)

    with open(os.path.join(full, "index.html"), "w") as f:
        f.write(html)

    os.utime(os.path.join(full, "index.html"), (dirtime, dirtime))

    return dirtime, date


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("nightly")
    args = ap.parse_args()

    dirs_7 = [ ]
    dirs_8 = [ ]

    for i in os.listdir(args.nightly):
        if re.match(r"(\d+-)?nightly-", i):
            full = os.path.join(args.nightly, i)
            dirtime, name = directory(i, full)

            if name is None:
                continue

            if i.startswith("8-"):
                dirs_8.append((dirtime, i, name))
            else:
                dirs_7.append((dirtime, i, name))

    dirs_7.sort()
    dirs_7.reverse()

    dirs_8.sort()
    dirs_8.reverse()

    tmpl = env.get_template("root.html")
    html = tmpl.render(dirs_7=dirs_7, dirs_8=dirs_8)

    with open(os.path.join(args.nightly, "index.html"), "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
