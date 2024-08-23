#!/usr/bin/env python3

import os
import sys
import subprocess
import traceback

FIX_PATH = "/home/tom/ab/nightly-build-fix/"
MASTER_PATH = "/home/tom/ab/nightly-build/"

os.chdir(os.path.dirname(sys.argv[0]))

def build_nightly():

    with open("/tmp/nightly-build-fix.txt", "w+") as f:
        try:
            subprocess.call([ "./nightly.sh", FIX_PATH, "fix", "--upload", "--clean" ], stdout=f, stderr=f, cwd=FIX_PATH)
        except Exception as e:
            traceback.print_exc(file=f)

    with open("/tmp/nightly-build-master.txt", "w+") as f:
        try:
            subprocess.call([ "./nightly.sh", MASTER_PATH, "master", "--upload", "--prune", "--clean" ], stdout=f, stderr=f, cwd=MASTER_PATH)
        except Exception as e:
            traceback.print_exc(file=f)

if __name__ == "__main__":
    build_nightly()
