#!/usr/bin/env python3

import os
import sys
import subprocess
import traceback

os.chdir(os.path.dirname(sys.argv[0]))

def build_nightly():

    with open("/tmp/nightly-build-fix.txt", "w+") as f:
        try:
            subprocess.call([ "./nightly.sh", '/home/tom/ab/nightly-build-fix/', "fix", "--clean" ], stdout=f, stderr=f)
        except Exception as e:
            traceback.print_exc(file=f)

    with open("/tmp/nightly-build-master.txt", "w+") as f:
        try:
            subprocess.call([ "./nightly.sh", '/home/tom/ab/nightly-build/', "master", "--upload", "--prune", "--clean" ], stdout=f, stderr=f)
        except Exception as e:
            traceback.print_exc(file=f)

if __name__ == "__main__":
    build_nightly()
