#!/bin/bash

set -e

# Set up the environment variables.

SCRIPTS=$(cd $(dirname $0); pwd)
ROOT="$SCRIPTS/.."
BASE=${1:-$ROOT}
REFS=${2:-$ROOT}

# Run git twice, as it could be updated by the pull.
. $SCRIPTS/git.sh
. $SCRIPTS/git.sh

. $SCRIPTS/build.sh
