import os
import shutil
import pathlib
import subprocess
import shutil

import jinja2

import renpybuild.run

# Monkeypatch copytree to fix a problem with ignore_dangling_symlinks.
old_copytree = shutil.copytree


def copytree(*args, ignore_dangling_symlinks=True, **kwargs):
    return old_copytree(*args, ignore_dangling_symlinks=ignore_dangling_symlinks, **kwargs)


shutil.copytree = copytree


class Context:
    """
    The Context class represents a context in which actions occur. It contains
    fields that have some information about the build easily accessible,
    stores information about the environment commands will be run in, and
    has actions that can be run by tasks.
    """

    def __init__(self, platform, arch, python, root, tmp, pygame_sdl2, renpy, args):

        # The platform. One of "linux", "windows", "mac", "android", "ios", or "web".
        self.platform = platform

        # The architecture. Varies based on the platform.
        self.arch = arch

        # The python version, one of "2" or "3".
        self.python = python

        # The root directory.
        self.root = root

        # The local temporary directory.
        self.tmp = tmp

        # Args.
        self.args = args

        # The environment dictionary.
        self.environ = dict(os.environ)

        # The non-environment variables dictionary.
        self.variables = { }

        self.var("tmp", tmp)

        self.var("platform", platform)
        self.var("arch", arch)
        self.var("python", python)
        self.var("root", root)
        self.var("runtime", self.root / "runtime")
        self.var("source", self.root / "source")
        self.var("tars", self.root / "tars")
        self.var("patches", self.root / "patches")
        self.var("prebuilt", self.root / "prebuilt")

        self.pygame_sdl2 = pygame_sdl2
        self.var("pygame_sdl2", self.pygame_sdl2)

        self.renpy = renpy
        self.var("renpy", self.renpy)

        self.renpyweb = self.root / "renpyweb"
        self.var("renpyweb", self.renpyweb)

        self.var("rapt", "{{ renpy }}/rapt")
        self.var("raptver", "{{ rapt }}" + self.python)

        if "arm" in self.arch:
            jni_arch = self.arch.replace("_", "-")
        else:
            jni_arch = self.arch

        self.var("jni_arch", jni_arch)
        self.var("jniLibs", "{{ raptver }}/prototype/renpyandroid/src/main/jniLibs/{{ jni_arch }}")

        self.var("jni_unstripped", "{{ raptver }}/symbols/{{ jni_arch }}")

        self.var("renios", "{{ renpy }}/renios" + self.python)

        self.var("pytmp", self.tmp / ("py" + python))

    def set_names(self, kind, task, name):
        """
        This is used to past the task-specific names into the context.
        """

        self.kind = kind

        # These store the task and name, just short words that are constant.
        self.task = task
        self.name = name

        # These store the task_name and dir_name, as computed by Task.context.
        self.task_name = ""
        self.dir_name = ""

        host = self.tmp / "host"
        self.var("host", host)

        if self.platform == "android":
            cross = self.tmp / f"cross.{self.platform}"
        else:
            cross = self.tmp / f"cross.{self.platform}-{self.arch}"

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

        self.install = install
        self.var("install", install)

        self.var("linuxinstall", self.tmp / "install.linux-x86_64")

        self.var("hostpython", "{{ install }}/bin/hostpython{{ c.python }}")

        if self.platform == "web":
            self.var("dist", self.install / "dist")
        else:
            self.var("dist", self.renpy)

        self.var("distlib", "{{dist}}/lib")

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

    def generate(self, src, dest, **kwargs):
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


    def env(self, variable, value):
        """
        Adds environment variable `variable` with `value`.
        """

        self.environ[variable] = self.expand(str(value))

    def var(self, variable, value, expand=True):
        """
        Adds a non-environment `variable` with `value`.
        """

        if expand:
            self.variables[variable] = self.expand(str(value))
        else:
            self.variables[variable] = value

    def get(self, variable):
        if variable in self.variables:
            return self.variables[variable]

        raise Exception(f"Unknown variable {variable!r}.")

    def chdir(self, d):
        """
        Changes the directory to `d`.
        """

        self.cwd = self.cwd / self.expand(d)

    def run(self, command, verbose=False, quiet=False):
        """
        Runs `command`, and checks that the result is 0.

        `command`
            Is a string that is interpreted as a jinja2 template. The environment
            variables created with environ and the variables created with var
            are available for substitution into the template.

            Once substitution has occured, the command is split using shlex.split,
            and then is run using popen.
        """

        command = self.expand(command)
        renpybuild.run.run(command, self, verbose, quiet)

    def clean(self, d="{{build}}"):
        """
        Empties the named directory.
        """

        d = self.expand(d)
        if not d:
            raise Exception("Not deleting empty-string directory.")

        d = pathlib.Path(d)
        if d.is_dir():
            shutil.rmtree(d)

        d.mkdir(exist_ok=True, parents=True)

    def path(self, p : str) -> pathlib.Path:
        """
        Returns a path object for `p`.
        """

        return self.cwd / self.expand(p)

    def patch(self, fn, p=1):
        """
        Applies the patch in `fn`.
        """

        fn = self.path("{{ patches }}") / self.expand(fn)

        with open(fn, "rb") as f:
            patch = f.read()

        subprocess.run([ "patch", "-p%d" % p ], input=patch, cwd=self.cwd, check=True)

    def patchdir(self, dn):
        """
        Applies all the patches in `dn`.
        """

        dn = self.path("{{ patches }}") / self.expand(dn)

        patches = list(dn.glob("*.diff")) + list(dn.glob("*.patch"))
        patches.sort()

        for fn in patches:

            print("Applying", fn.name)

            with open(fn, "rb") as f:
                patch = f.read()

            subprocess.run([ "patch", "-p1" ], input=patch, cwd=self.cwd, check=True)

    def copy(self, src, dst):
        """
        Copies `src` to `dst`.
        """

        shutil.copy(self.path(src), self.path(dst))

    def include(self, path):

        if self.kind == "host":
            return

        if self.kind == "cross":
            return

        if self.path(path).exists():
            self.env("CFLAGS", "{{ CFLAGS }} -I" + path)

    def copytree(self, src, dst):
        self.rmtree(dst)

        src = self.path(src)
        dst = self.path(dst)

        if src.is_symlink():
            src = src.readlink()

        shutil.copytree(src, dst)

    def rmtree(self, d):
        d = self.path(d)
        if d.is_symlink():
            d.unlink()
        elif d.exists():
            shutil.rmtree(d)

    def unlink(self, fn):
        fn = self.path(fn)
        if fn.exists():
            fn.unlink()

    def symlink(self, src, dst):
        src = self.path(src)
        dst = self.path(dst)

        dst.symlink_to(src)

    def extension(self, source, cflags=""):

        source = self.path(source)

        self.var("source", source)

        if self.platform == "windows":
            self.var("so", "{{dlpa}}/" + source.stem + ".pyd")
            self.run("{{ CXX }} {{ CFLAGS }} {{ LDFLAGS }} -L{{ dlpa }}  -shared -o {{ so }} {{ source }} -lrenpython -l{{ pythonver }} " + cflags, verbose=True)

        elif self.platform == "ios":
            self.var("name", source.stem)
            self.var("cname", source.stem.replace(".", "_"))
            self.var("o", source.stem + ".o")
            self.var("a", source.stem + ".a")

            self.var("initc", "init_" + source.stem + ".c")
            self.var("inito", "init_" + source.stem + ".o")

            self.run("{{ CXX }} {{ CFLAGS }} {{ LDFLAGS }} -c -o {{ o }} {{ source }} " + cflags, verbose=True)

            with open(self.path("{{ initc }}"), "w") as f:
                f.write(self.expand("""\
#include "Python.h"

PyMODINIT_FUNC init{{ cname }} (void);

static struct _inittab {{cname}}_inittab[]  = {
    { "{{ name }}", init{{ cname }} },
    { NULL, NULL },
};

static void {{ cname }}_constructor() __attribute__((constructor));

static void {{ cname }}_constructor() {
    PyImport_ExtendInittab({{ cname }}_inittab);
}
"""))

            self.run("{{ CXX }} {{ CFLAGS }} {{ LDFLAGS }} -c -o {{ inito }} {{ initc }}", verbose=True)

            self.run("""{{ AR }} -r {{ a }} {{ o }} {{ inito }}""")
            self.run("""install -d {{install}}/lib""")
            self.run("""install {{ a }} {{ install }}/lib""")

        elif self.platform == "android":
            self.var("so", "{{ dlpa }}/" + source.stem + ".so")
            self.run("{{ CXX }} {{ CFLAGS }} {{ LDFLAGS }} -L{{ jniLibs }} -shared -o {{ so }} {{ source }} -lrenpython " + cflags, verbose=True)
        else:

            self.var("so", "{{ dlpa }}/" + source.stem + ".so")
            self.run("{{ CXX  }} {{ CFLAGS }} {{ LDFLAGS }} -L{{ dlpa }} -shared -o {{ so }} {{ source }} -lrenpython " + cflags, verbose=True)
