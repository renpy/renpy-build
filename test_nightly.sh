#!/usr/bin/env bash

# Tests the nightly build of the project.

set -ex

nightly=${NIGHTLY:-/home/tom/ab/nightly-build}


rm -Rf $nightly/tasks
cp -a tasks $nightly/tasks

rm -Rf $nightly/renpybuild
cp -a renpybuild $nightly/

rm -Rf $nightly/nightly
cp -a nightly $nightly/nightly

cd $nightly/
nice -n 10 ./nightly/nightly.sh $nightly master --nopull
