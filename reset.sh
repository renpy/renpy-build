#!/bin/bash

set -x

BASE=$(cd $(dirname $0); pwd)

sudo rm -Rf "$BASE/tmp"
sudo cp -a "$BASE/tmp.initial" "$BASE/tmp"
