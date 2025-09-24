#!/bin/bash

set -e

ROOT="$(dirname $(realpath $0))"
cd $ROOT

exec uv --project renpy run -m renpybuild "$@"
