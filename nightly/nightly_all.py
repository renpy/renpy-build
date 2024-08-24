#!/usr/bin/env python3

import os
import sys
import subprocess
import traceback

NIGHTLY_FIX_PATH = "/home/tom/ab/nightly-build-fix/"
NIGHTLY_MASTER_PATH = "/home/tom/ab/nightly-build/"

RB_FIX_PATH="/home/tom/ab/renpy-build-fix/"
RB_MASTER_PATH="/home/tom/ab/renpy-build/"


os.chdir(os.path.dirname(sys.argv[0]))

def build_nightly():

    with open("/tmp/nightly-build-fix.txt", "w+") as f:
        try:
            subprocess.call([ "./nightly.sh", NIGHTLY_FIX_PATH, "fix", "--upload", "--clean" ], stdout=f, stderr=f, cwd=RB_FIX_PATH + "/nightly")
        except Exception as e:
            traceback.print_exc(file=f)

    with open("/tmp/nightly-build-master.txt", "w+") as f:
        try:
            subprocess.call([ "./nightly.sh", NIGHTLY_MASTER_PATH, "master", "--upload", "--prune", "--clean" ], stdout=f, stderr=f, cwd=RB_MASTER_PATH + "/nightly")
        except Exception as e:
            traceback.print_exc(file=f)

if __name__ == "__main__":
    build_nightly()
