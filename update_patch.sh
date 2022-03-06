#!/bin/bash

NAME="$(basename $PWD)"
ROOT="$(dirname $0)"

stg export -e diff -d "$ROOT/patches/$NAME"

cat "$ROOT/patches/$NAME/series"