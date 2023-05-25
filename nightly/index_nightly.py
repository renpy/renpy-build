#!/usr/bin/env python

import datetime
import os.path
import argparse
import re
import json
from collections import namedtuple, defaultdict
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    autoescape=select_autoescape(['html', 'xml']),
)

gh = 'https://github.com/renpy'
src = namedtuple('Source', 'text url')


def directory(name, full):

    sdk = [ ]
    other = [ ]
    vcs = [ ]

    dirtime = 0

    branch = "master"

    for i in os.listdir(full):

        if i in [ ".build_cache", "updates.json", "updates.json.sig", "index.html", "date.txt" ]:
            continue

        if i.endswith(".update.gz"):
            continue

        if i.endswith("update.json"):
            continue

        if i.endswith(".sums"):
            continue

        if i.endswith(".zsync"):
            continue

        if i == "vcs.json":
            with open(os.path.join(full, i)) as f:
                vcs = [ src(f'{repo}@{rev}', f'{gh}/{repo}/commits/{sha}')
                        for repo, sha, rev in json.load(f) ]
            continue

        if i == "branch.txt":
            with open(os.path.join(full, i)) as f:
                branch = f.read().strip()
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
        return None

    if not sdk:
        return None

    dt = datetime.datetime.fromtimestamp(dirtime)

    sdk.sort()
    other.sort()

    tmpl = env.get_template("nightly.html")
    html = tmpl.render(date=date, name=name, sdk=sdk, other=other, vcs=vcs, branch=branch)

    with open(os.path.join(full, "index.html"), "w") as f:
        f.write(html)

    os.utime(os.path.join(full, "index.html"), (dirtime, dirtime))

    return dt


def sort_key(name):
    """
    Given a version name, return a tuple that can be used to sort it.
    """

    name = name.partition("+")[0]
    name = name.rstrip("n")

    return tuple(int(i) for i in name.split("."))

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("nightly")
    args = ap.parse_args()

    dirs = defaultdict(list)
    dates = set()

    for i in os.listdir(args.nightly):
        if i[0] in "78":
            full = os.path.join(args.nightly, i)

            dt = directory(i, full)

            if dt is None:
                continue

            date = dt.date()
            name = i.rpartition("-")[2]

            branch = "main"

            try:
                with open(os.path.join(full, "branch.txt")) as f:
                    branch = f.read().strip()
            except FileNotFoundError:
                pass

            if branch == "master":
                branch = "main"

            python = int(i[0])

            dates.add(date)
            dirs[date, python, branch].append((name, i))


    dates = list(dates)
    dates.sort(reverse=True)

    rows = [ ]

    def col(date, python, branch):
        l = dirs[date, python, branch]
        l.sort(key=lambda x: sort_key(x[0]), reverse=True)
        return l

    for d in dates:

        date = d.strftime("%A, %B %d, %Y" )

        rows.append(
            (date, [
                col(d, 8, "main"),
                col(d, 8, "fix"),
                col(d, 7, "main"),
                col(d, 7, "fix"),
            ]))

    tmpl = env.get_template("root.html")
    html = tmpl.render(rows=rows)

    with open(os.path.join(args.nightly, "index.html"), "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
