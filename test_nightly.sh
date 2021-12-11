#!/usr/bin/env bash

# Tests the nightly build of the project.

set -e

nightly=${$1:-/home/tom/ab/nightly-build}


rm -Rf $nightly/tasks
cp -a tasks $nightly/tasks

rm -Rf $nightly/renpybuild
cp -a renpybuild $nightly/

cd $nightly/
. tmp/virtualenv.py2/bin/activate
exec ./build.py "$@"
