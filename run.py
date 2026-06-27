import argparse
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
IMAGE_NAME = "renpy-build"
TMP_VOLUME = "renpy-build-tmp"
TARS_VOLUME = "tars"


def make_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="run.ps1" if os.name == "nt" else "run.sh",
        description="Ren'Py Build System",
    )

    # Mirror the inner __main__.py interface.
    ap.add_argument(
        "--platforms",
        "--platform",
        default="",
        metavar="NAME",
        help="platform(s) to build for",
    )
    ap.add_argument(
        "--archs",
        "--arch",
        default="",
        metavar="NAME",
        help="architecture(s) to build for",
    )
    ap.add_argument(
        "--pythons",
        "--python",
        default="3",
        help=argparse.SUPPRESS,
    )
    ap.add_argument(
        "--nostrip",
        action="store_true",
        help="do not strip binaries",
    )
    ap.add_argument(
        "--sdl",
        action="store_true",
        help="do not clean SDL on rebuild",
    )
    ap.add_argument(
        "--experimental",
        action="store_true",
        help="include experimental platforms",
    )
    ap.add_argument(
        "--stop",
        default=None,
        metavar="TASK",
        help="stop after this task",
    )

    # Image build options.
    ap.add_argument(
        "--tag",
        default="latest",
        help="tag to use for the image",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="print the podman command without running it",
    )
    ap.add_argument(
        "--no-cache",
        action="store_true",
        help="rebuild the container image without cache",
    )

    subparsers = ap.add_subparsers(dest="command")
    subparsers.add_parser("build", help="build Ren'Py (default)")

    sp = subparsers.add_parser("rebuild", help="rebuild specific tasks")
    sp.add_argument("tasks", nargs="+")

    subparsers.add_parser("clean", help="clean build artifacts")

    sp = subparsers.add_parser("export", help="export tmp volume to a tarball")
    sp.add_argument(
        "dest",
        nargs="?",
        default="renpy-build-tmp.tar",
        help="output file (default: renpy-build-tmp.tar)",
    )

    sp = subparsers.add_parser("import", help="import tmp volume from a tarball")
    sp.add_argument("src", help="tarball to import")

    sp = subparsers.add_parser("exec", help="run a command in the build container")
    sp.add_argument("cmd", nargs="*", default=["bash"], help="command to run")

    return ap


def ensure_image(tag: str, *, no_cache: bool) -> None:
    if not no_cache:
        exists_cmd = ["podman", "image", "exists", f"{IMAGE_NAME}:{tag}"]
        if subprocess.run(exists_cmd).returncode == 0:
            return

    compose_cmd = ["podman", "compose", "build"]
    if no_cache:
        compose_cmd += ["--no-cache", "--pull"]
    compose_cmd += [IMAGE_NAME]

    subprocess.run(
        compose_cmd,
        cwd=SCRIPT_DIR,
        env=os.environ | {"TAG": tag},
        check=True,
    )


def volume_export(dest: str) -> None:
    dest_path = Path(dest).resolve()
    with open(dest_path, "wb") as f:
        result = subprocess.run(["podman", "volume", "export", TMP_VOLUME], stdout=f)
    if result.returncode != 0:
        dest_path.unlink(missing_ok=True)
        sys.exit(result.returncode)
    print(f"Exported {TMP_VOLUME} to {dest_path}")


def volume_import(src: str) -> None:
    src_path = Path(src).resolve()
    if not src_path.is_file():
        print(f"Error: '{src}' not found.", file=sys.stderr)
        sys.exit(1)
    with open(src_path, "rb") as f:
        result = subprocess.run(["podman", "volume", "import", TMP_VOLUME], stdin=f)
    if result.returncode != 0:
        sys.exit(result.returncode)
    print(f"Imported {src_path} to {TMP_VOLUME}")


def main() -> None:
    # Check prerequisites.
    for tool in ("podman",):
        if not shutil.which(tool):
            print(f"Error: '{tool}' is not installed.", file=sys.stderr)
            sys.exit(1)

    if not sys.argv[1:]:
        sys.argv.append("--help")

    # Validate build arguments through argparse.
    parser = make_parser()
    args = parser.parse_args()

    # Handle volume subcommands — no container needed.
    if args.command == "export":
        volume_export(args.dest)
        sys.exit(0)
    if args.command == "import":
        volume_import(args.src)
        sys.exit(0)

    # Validate renpy directory.
    renpy_path = SCRIPT_DIR / "renpy"
    if renpy_path.is_symlink():
        renpy_path = renpy_path.resolve()

    if not renpy_path.is_dir():
        print(
            "Error: renpy directory not found. Clone or symlink the Ren'Py repository into renpy-build.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Make sure there is an image with needed tag.
    ensure_image(args.tag, no_cache=args.no_cache)

    # Assemble podman command.
    cmd: list[str] = [
        "podman",
        "run",
        "--rm",
        "--interactive",
        "--tty",
    ]

    cmd += [
        "-v",
        f"{renpy_path}:/build/renpy",
        "-v",
        f"{TMP_VOLUME}:/build/tmp",
        "-v",
        f"{TARS_VOLUME}:/build/tars",
    ]

    # Mount each non-ignored directory in renpy-build as a volume.
    for d in [
        "extensions/",
        "nvlib/",
        "patches/",
        "prebuilt/",
        "rapt/",
        "renios/",
        "renpybuild/",
        "runtime/",
        "source/",
        "specs/",
        "steamapi/",
        "tasks/",
        "tools/",
    ]:
        host_path = SCRIPT_DIR / d
        if host_path.is_dir():
            cmd += ["-v", f"{host_path}:/build/{d}"]

    cmd += [
        # Store venv in a tmp volume, so build system doesn't change venv in
        # renpy directory that could be a link to repository with existing venv.
        # uv sync will make sure installed packages are up to date.
        "-e",
        "UV_PROJECT_ENVIRONMENT=/build/tmp/venv",
        "-e",
        "UV_CACHE_DIR=/build/tmp/uv-cache",
        "-e",
        "RENPY_VIRTUAL_ENV=/build/tmp/venv",
        "-e",
        "CCACHE_DIR=/build/tmp/ccache",
        "-e",
        "PYTHONUNBUFFERED=1",
        "-e",
        "PYTHONHASHSEED=0",
    ]

    cmd += [f"{IMAGE_NAME}:{args.tag}"]

    # Strip wrapper-only flags so the inner script doesn't see them.
    inner_argv = [a for a in sys.argv[1:] if a not in ("--tag", "--dry-run", "--no-cache")]

    if args.command == "exec":
        cmd += args.cmd
    else:
        sub_command = [
            "cd /build",
            "uv --project renpy sync",
            ". /build/tmp/venv/bin/activate",
            'exec uv --project renpy run -m renpybuild "$@"',
        ]
        cmd += ["bash", "-c", " && ".join(sub_command), "--", *inner_argv]

    if args.dry_run:
        print(" \\\n  ".join(shlex.quote(c) for c in cmd))
        sys.exit(0)

    result = subprocess.run(cmd, cwd=SCRIPT_DIR)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
