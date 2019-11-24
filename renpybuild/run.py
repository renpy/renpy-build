import jinja2
import shlex
import subprocess
import sys


def build_environment(c):
    """
    Sets up the build environment inside the context.
    """

    c.var("sysroot", c.tmp / f"sysroot.{c.platform}-{c.arch}")

    if (c.platform == "linux") and (c.arch == "x86_64"):

        c.env("CC", "ccache gcc -O3 --sysroot {{ sysroot }}")
        c.env("CXX", "ccache g++ -O3 --sysroot {{ sysroot }}")
        c.env("LD", "{{ CC }}")
        c.env("LDXX", "{{ CXX }}")

    elif (c.platform == "linux") and (c.arch == "i686"):

        c.env("CC", "ccache gcc -m32 -O3 --sysroot {{ sysroot }}")
        c.env("CXX", "ccache g++ -m32 -O3 --sysroot {{ sysroot }}")
        c.env("LD", "{{ CC }}")
        c.env("LDXX", "{{ CXX }}")


def run(command, context):
    args = shlex.split(command)

    p = subprocess.run(args, cwd=context.cwd, env=context.environ)

    if p.returncode != 0:
        print(f"{context.task_name}: process failed with {p.returncode}.")
        print("args:", args)
        sys.exit(1)

