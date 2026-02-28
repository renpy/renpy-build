#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

IMAGE_NAME="renpy-build"
BRANCH="$(git rev-parse --abbrev-ref HEAD | tr '/' '-')"
SHA="$(git rev-parse --short=7 HEAD)"
TAG="${BRANCH}-${SHA}"

show_usage() {
    cat <<EOF
Usage: run.sh <mode> [args...]

Modes:
  build   Run container in production mode, tagging the image with the current
          commit hash of renpy-build.
  dev     Run container in dev mode, mounting the renpy-build directory so that
          changes to the source are reflected in the container.

Examples:
  ./run.sh build --platform linux build
  ./run.sh dev clean
EOF
}

assert_image() {
    local image_tag="$1"
    if ! podman image exists "${IMAGE_NAME}:${image_tag}" 2>/dev/null; then
        TAG="${image_tag}" podman compose build "$IMAGE_NAME"
    fi
}

assert_renpy() {
    RENPY_PATH="$(readlink -f ./renpy 2>/dev/null || true)"
    if [[ -z "$RENPY_PATH" || ! -d "$RENPY_PATH" ]]; then
        echo "Renpy path not found. Please link or clone Ren'Py repository into renpy-build." >&2
        exit 1
    fi
}

if [[ $# -lt 1 ]]; then
    show_usage
    exit 1
fi

MODE="$1"
shift

common_env=(
    -e "UV_PROJECT_ENVIRONMENT=/cache/venv"
    -e "RENPY_VIRTUAL_ENV=/cache/venv"
    -e "PYTHONUNBUFFERED=1"
    -e "PYTHONHASHSEED=0"
    -e "RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/"
)

case "$MODE" in
    dev)
        assert_renpy

        volumes=(
            -v "${RENPY_PATH}:/build/renpy"
            # Store venv in a volume, so build system doesn't change venv in renpy
            # directory that could be a link to repository with existing venv.
            # uv sync will make sure installed packages are up to date.
            -v "renpy-build-venv:/cache/venv"
            # Add tmp dir as a volume, to keep its content for incremental builds.
            -v "renpy-build-dev-tmp:/build/tmp"
        )

        assert_image "dev"

        # In dev mode, mount each non-ignored directory in renpy-build as a
        # volume shadowing files in the container that could be stale.
        dev_volumes=(
            -v "${SCRIPT_DIR}/docker-entrypoint.sh:/build/docker-entrypoint.sh"
        )
        while IFS= read -r entry; do
            host_path="${SCRIPT_DIR}/${entry}"
            if [[ -d "$host_path" ]]; then
                dev_volumes+=(-v "${host_path}:/build/${entry}")
            fi
        done < <(git ls-tree --name-only HEAD)

        podman run --rm -it \
            "${dev_volumes[@]}" \
            "${volumes[@]}" \
            "${common_env[@]}" \
            "${IMAGE_NAME}:dev" \
            "$@"
        ;;

    build)
        assert_renpy

        volumes=(
            -v "${RENPY_PATH}:/build/renpy"
            -v "renpy-build-venv:/cache/venv"
        )

        if [[ -n "$(git status --porcelain)" ]]; then
            echo "Error: renpy-build working tree is dirty. Commit or stash changes before building." >&2
            exit 1
        fi

        assert_image "${TAG}"

        podman run --rm \
            "${volumes[@]}" \
            "${common_env[@]}" \
            "${IMAGE_NAME}:${TAG}" \
            "$@"
        ;;

    *)
        show_usage
        exit 1
        ;;
esac
