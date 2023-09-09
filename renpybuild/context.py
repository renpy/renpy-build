import os
import shutil
from pathlib import Path
import subprocess
import shutil

import jinja2

import renpybuild.run

from typing import Any

# Monkeypatch copytree to fix a problem with ignore_dangling_symlinks.
old_copytree = shutil.copytree


def copytree(*args, **kwargs):
    if len(args) < 6:
        kwargs.setdefault("ignore_dangling_symlinks", True)

    return old_copytree(*args, **kwargs)


shutil.copytree = copytree


class Context:
    """
    The Context class represents a context in which actions occur. It contains
    fields that have some information about the build easily accessible,
    stores information about the environment commands will be run in, and
    has actions that can be run by tasks.
    """

    # The platform. One of "linux", "windows", "mac", "android", "ios", or "web".
    platform : str

    # The architecture. Varies based on the platform.
    arch : str

    # The version of Python, one of "2" or "3"
    python : str

    # The root directory of the build.
    root : Path

    # The arguments passed to the build by argparse.
    args : Any

    # Maps containing the environment and non-environment variables. Environment
    # variables are passed to subprocesses, while non-environment variables are
    # only used for expansion.
    environ : dict[str, str]
    variables : dict[str, str]

    # The local temporary directory.
    tmp : Path

    # The kind of task.
    kind : str

    # The name of the function that the task is defined in.
    task : str

    # The name of the module that the task is defined in.
    name : str

    # A unique name for this the task being executed.
    task_name : str

    # The name of the directory the task will run in.
    dir_name : str

    # The path to the directory builds will be placed in.
    build : Path

    # The current directory the task will run in.
    cwd : Path

    # The place to install to.
    install : Path

    # More paths.
    renpy: Path
    pygame_sdl2: Path
    renpyweb: Path

    def __init__(self, platform : str, arch : str, python : str, root : Path, args : Any):

        self.platform = platform
        self.arch = arch
        self.python = python
        self.root = root
        self.args = args

        self.environ = dict(os.environ)
        self.variables = { }

        # The local temporary directory.
        self.tmp = self.root / "tmp"

        self.var("tmp", self.tmp)

        self.var("platform", platform)
        self.var("arch", arch)
        self.var("python", python)
        self.var("root", root)

        # Paths relative to root.
        self.var("runtime", self.root / "runtime")
        self.var("source", self.root / "source")
        self.var("tars", self.root / "tars")
        self.var("patches", self.root / "patches")
        self.var("prebuilt", self.root / "prebuilt")

        # Paths to subprojects.
        self.pygame_sdl2 = self.root / "pygame_sdl2"
        self.var("pygame_sdl2", self.pygame_sdl2)

        self.renpy = self.root / "renpy"
        self.var("renpy", self.renpy)

        self.renpyweb = self.root / "renpyweb"
        self.var("renpyweb", self.renpyweb)

        self.var("rapt", "{{ renpy }}/rapt")
        self.var("raptver", "{{ rapt }}" + self.python)

        #
        if "arm" in self.arch:
            jni_arch = self.arch.replace("_", "-")
        else:
            jni_arch = self.arch

        self.var("jni_arch", jni_arch)
        self.var("jniLibs", "{{ raptver }}/prototype/renpyandroid/src/main/jniLibs/{{ jni_arch }}")

        self.var("jni_unstripped", "{{ raptver }}/symbols/{{ jni_arch }}")

        self.var("renios", "{{ renpy }}/renios" + self.python)

        # Python version specific storage.
        self.var("pytmp", self.tmp / ("py" + python))


    def set_names(self, kind : str, task : str, name : str):
        """
        This is used to past the task-specific names into the context.
        """

        self.kind = kind
        self.task = task
        self.name = name

        # These store the task_name and dir_name, as computed by Task.context.
        self.task_name = ""
        self.dir_name = ""

        # The path to binaries common to all builds.
        host = self.tmp / "host"
        self.var("host", host)

        if self.platform == "android":
            cross = self.tmp / f"cross.{self.platform}"
        else:
            cross = self.tmp / f"cross.{self.platform}-{self.arch}"

        # The path to the cross compiler.
        self.var("cross", cross)

        per_python = False

        if kind == "host":
            self.dir_name = f"{self.name}.host"
        elif kind == "host-python":
            self.dir_name = f"{self.name}.py{self.python}"
        elif kind == "cross":
            self.dir_name = f"{self.name}.cross-{self.platform}-{self.arch}"
        elif kind == "platform":
            self.dir_name = f"{self.name}.{self.platform}"
        elif kind == "platform-python":
            self.dir_name = f"{self.name}.{self.platform}"
            per_python = True
        elif kind == "arch":
            self.dir_name = f"{self.name}.{self.platform}-{self.arch}"
        elif kind == "arch-python":
            self.dir_name = f"{self.name}.{self.platform}-{self.arch}"
            per_python = True
        elif kind == "python":
            self.dir_name = f"{self.name}.{self.platform}-{self.arch}-py{self.python}"

        self.task_name = f"{self.task}-{self.dir_name}"

        if per_python:
            self.task_name += "-py" + self.python

        build = self.tmp / "build" / self.dir_name
        build.mkdir(parents=True, exist_ok=True)

        # The build directory.
        self.build = build
        self.cwd = build
        self.var("build", build)

        if kind == "host":
            install = host
        elif kind == "cross":
            install = cross
        else:
            install = self.tmp / f"install.{self.platform}-{self.arch}"

        install.mkdir(parents=True, exist_ok=True)

        # The place to install files.
        self.install = install
        self.var("install", install)

        # The install for linux-x86_64, used to find file from any python isntall.
        self.var("linuxinstall", self.tmp / "install.linux-x86_64")

        # The path to a version of Python comp
        self.var("hostpython", "{{ install }}/bin/hostpython{{ c.python }}")

        # Final installation paths.
        if self.platform == "web":
            self.var("dist", self.install / "dist")
        else:
            self.var("dist", self.renpy)

        self.var("distlib", "{{dist}}/lib")

        # renpy/lib/py3-linux-x86_64 and friends. ({{dist}}/lib/py-platform-arch)
        if self.platform == "mac":
            self.var("dlpa", "{{distlib}}/py{{ python }}-{{ platform }}-universal")
        else:
            self.var("dlpa", "{{distlib}}/py{{ python }}-{{ platform }}-{{ arch }}")

        renpybuild.run.build_environment(self)

    def expand(self, s : str, **kwargs) -> str:
        """
        Expands `s` as a jinja template.
        """

        template = jinja2.Template(s)

        variables = dict()
        variables.update(self.environ)
        variables.update(self.variables)
        variables.update({ "c" : self })
        variables.update(kwargs)

        return template.render(**variables)

    def generate(self, src : str, dest : str, **kwargs):
        """
        Loads in `src`, a template file, substitutes in ``kwargs`` and all
        the other variables that are defined, and writes it out into ``dest``.
        """

        template = self.path(src).read_text()
        text = self.expand(template, **kwargs)

        if not text.endswith("\n"):
            text = text + "\n"

        self.path(dest).write_text(text)

    def generate_text(self, template, dest, **kwargs):
        """
        This uses `template` as a template, and writes it out to `dest`,
        substituting in ``kwargs`` and all the other variables that are defined.
        """

        text = self.expand(template, **kwargs)

        if not text.endswith("\n"):
            text = text + "\n"

        self.path(dest).write_text(text)


    def env(self, variable : str, value : str|Path):
        """
        Adds environment variable `variable` with `value`.
        """

        self.environ[variable] = self.expand(str(value))

    def var(self, variable : str, value : str|Path, expand=True):
        """
        Adds a non-environment `variable` with `value`.
        """

        if expand:
            self.variables[variable] = self.expand(str(value))
        else:
            self.variables[variable] = str(value)

    def get(self, variable : str) -> str:
        """
        Returns the value of `variable`.
        """

        if variable in self.variables:
            return self.variables[variable]

        raise Exception(f"Unknown variable {variable!r}.")

    def chdir(self, d : str):
        """
        Changes the directory to `d`.
        """

        self.cwd = self.cwd / self.expand(d)

    def run(self, command : str, verbose : bool=False, quiet : bool=False, **kwargs):
        """
        Runs `command`, and checks that the result is 0.

        `command`
            Is a string that is interpreted as a jinja2 template. The environment
            variables created with environ and the variables created with var
            are available for substitution into the template.

            Once substitution has occured, the command is split using shlex.split,
            and then is run using popen.
        """

        command = self.expand(command, **kwargs)
        renpybuild.run.run(command, self, verbose, quiet)

    def run_group(self):
        """
        Creates a run_group. This is a context manager with a run method,
        that allows multiple commands to be run in parallel.
        """

        return renpybuild.run.RunGroup(self)

    def clean(self, d : str="{{build}}"):
        """
        Empties the named directory.
        """

        d = self.expand(d)
        if not d:
            raise Exception("Not deleting empty-string directory.")

        p = Path(d)
        if p.is_dir():
            shutil.rmtree(d)

        p.mkdir(exist_ok=True, parents=True)

    def path(self, p : str) -> Path:
        """
        Returns a path object for `p`.
        """

        return self.cwd / self.expand(p)

    def patch(self, fn : str, p : int=1):
        """
        Applies the patch in `fn`.

        `p`
            The -p argument to patch. Defaults to 1.
        """

        fpath = self.path("{{ patches }}") / self.expand(fn)

        with open(fpath, "rb") as f:
            patch = f.read()

        subprocess.run([ "patch", "-p%d" % p ], input=patch, cwd=self.cwd, check=True)

    def patchdir(self, dn : str):
        """
        Applies all the patches in `dn`.
        """

        dpath = self.path("{{ patches }}") / self.expand(dn)

        patches = list(dpath.glob("*.diff")) + list(dpath.glob("*.patch"))
        patches.sort()

        for fn in patches:

            print("Applying", fn.name)

            with open(fn, "rb") as f:
                patch = f.read()

            subprocess.run([ "patch", "-p1" ], input=patch, cwd=self.cwd, check=True)

    def copy(self, src : str, dst : str):
        """
        Copies `src` to `dst`.
        """

        shutil.copy(self.path(src), self.path(dst))

    def include(self, path : str):
        """
        Adds an include to the C compiler include path.
        """

        if self.kind == "host":
            return

        if self.kind == "cross":
            return

        if self.path(path).exists():
            self.env("CFLAGS", "{{ CFLAGS }} -I" + path)

    def copytree(self, src : str, dst : str):
        """
        Copies the directory `src` to `dst`. If `dst` exists, it is removed.
        """

        self.rmtree(dst)

        srcpath = self.path(src)
        dstpath = self.path(dst)

        if srcpath.is_symlink():
            srcpath = srcpath.readlink()

        shutil.copytree(srcpath, dstpath)

    def rmtree(self, d : str):
        """
        Removes the directory `d`.
        """

        dpath = self.path(d)

        if dpath.is_symlink():
            dpath.unlink()
        elif dpath.exists():
            shutil.rmtree(dpath)

    def unlink(self, fn : str):
        """
        Removes the file `fn`.
        """

        fnpath = self.path(fn)
        if fnpath.exists():
            fnpath.unlink()

    def symlink(self, src : str, dst : str):
        """
        Creates a symlink from `src` to `dst`.
        """

        srcpath = self.path(src)
        dstpath = self.path(dst)

        dstpath.symlink_to(srcpath)
