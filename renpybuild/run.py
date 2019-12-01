import jinja2
import shlex
import subprocess
import sys
import sysconfig


def build_environment(c):
    """
    Sets up the build environment inside the context.
    """

    c.var("sysroot", c.tmp / f"sysroot.{c.platform}-{c.arch}")
    c.var("build_platform", sysconfig.get_config_var("HOST_GNU_TYPE"))

    c.env("CFLAGS", "-I{{ install }}/include")
    c.env("LDFLAGS", "-L{{ install }}/lib")

    if (c.platform == "linux") and (c.arch == "x86_64"):

        c.var("host_platform", "x86_64-pc-linux-gnu")

        c.env("CC", "ccache gcc -O3 -fPIC --sysroot {{ sysroot }}")
        c.env("CXX", "ccache g++ -O3 -fPIC --sysroot {{ sysroot }}")
        c.env("LD", "{{ CC }}")
        c.env("LDXX", "{{ CXX }}")

    elif (c.platform == "linux") and (c.arch == "i686"):

        c.var("host_platform", "i686-pc-linux-gnu")

        c.env("CC", "ccache gcc -m32 -fPIC -O3 --sysroot {{ sysroot }}")
        c.env("CXX", "ccache g++ -m32 -fPIC -O3 --sysroot {{ sysroot }}")
        c.env("LD", "{{ CC }}")
        c.env("LDXX", "{{ CXX }}")

    c.var("cross_config", "--host={{ host_platform }} --build={{ build_platform }}")


def run(command, context):
    args = shlex.split(command)

    p = subprocess.run(args, cwd=context.cwd, env=context.environ)

    if p.returncode != 0:
        print(f"{context.task_name}: process failed with {p.returncode}.")
        print("args:", args)
        sys.exit(1)

