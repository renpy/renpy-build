import time
import os
import shutil
import pathlib
import subprocess
import shutil

import jinja2

import renpybuild.run

# Monkeypatch copytree to fix a problem with ignore_dangling_symnlinks.
old_copytree = shutil.copytree


def copytree(*args, ignore_dangling_symlinks=True, **kwargs):
    return old_copytree(*args, ignore_dangling_symlinks=ignore_dangling_symlinks, **kwargs)


shutil.copytree = copytree


class Context:
    """
    This class is passed to the task to represent information about the
    current build.
    """

    def __init__(self, platform, arch, python, root, tmp, pygame_sdl2, renpy, args):

        # The platform. One of "linux", "windows", "mac", "android", "ios", or "emscripten".
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

        self.var("dist", self.renpy)
        self.var("distlib", self.renpy / ("lib" + python))
        self.var("dlpa", "{{distlib}}/{{ platform }}-{{ arch }}")

        self.var("rapt", "{{ renpy }}/rapt")
        self.var("raptver", "{{ rapt }}" + self.python)

        if "arm" in self.arch:
            jni_arch = self.arch.replace("_", "-")
        else:
            jni_arch = self.arch

        self.var("jni_arch", jni_arch)
        self.var("jniLibs", "{{ raptver }}/prototype/renpyandroid/src/main/jniLibs/{{ jni_arch }}")

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

        self.var("hostpython", "{{ install }}/bin/hostpython{{ c.python }}")

        renpybuild.run.build_environment(self)

    def expand(self, s, **kwargs):
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
        the other variables that are define, and writes it out into ``dest``.
        """

        template = self.path(src).read_text()
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

    def chdir(self, d):
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

    def path(self, p):
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
        src = self.path(src)
        dst = self.path(dst)

        if dst.exists():
            shutil.rmtree(dst)

        shutil.copytree(src, dst)

    def rmtree(self, d):
        d = self.path(d)
        if d.exists():
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


class Task:
    """
    A task represents something that can be run to make the build process
    proceed.
    """

    def __init__(self, task, name, *, function=None, kind="arch", always=False, platforms="-web", archs=None, pythons=None):

        self.task = task
        self.name = name
        self.kind = kind
        self.always = always

        def split(v):
            if v is None:
                return v

            if v == "all":
                return None

            if v[0] == "-":
                negative = True
                v = v[1:]
            else:
                negative = False

            rv = { i.strip() for i in v.split(",") }

            if negative:
                rv.add("negative")

            return rv

        self.platforms = split(platforms)
        self.archs = split(archs)
        self.pythons = split(pythons)

        self.function = function

        tasks.append(self)

    def run(self, context):

        def check(wanted, have):
            if wanted is None:
                return True

            if "negative" in wanted:
                return have not in wanted
            else:
                return have in wanted

        if not self.kind == "host":

            if not check(self.platforms, context.platform):
                return

            if not check(self.archs, context.arch):
                return

            if not check(self.pythons, context.python):
                return

        context.set_names(self.kind, self.task, self.name)

        if context.task_name in ran_tasks:
            return

        complete = context.tmp / "complete"
        complete.mkdir(parents=True, exist_ok=True)
        complete /= context.task_name

        if (not self.always) and complete.exists():
            print(f"{context.task_name} already finished.")
            ran_tasks.add(context.task_name)
            return

        for a in annotators:
            a(context)

        print(f"{context.task_name} running in {context.build} ...")

        self.function(context)

        print("")

        ran_tasks.add(context.task_name)

        complete.write_text(str(time.time()))


def task(**kwargs):
    """
    This is a decorator that wraps a function to define a task. The function must
    have a name of the form `task`_`name`. For example, "build_libz" or "unpack_python_38".

    This also takes optional keyword arguments.

    `kind`
        Determines how often this task shold run. One of:

        "platform" - Once per platform.
        "arch" - Once per platform/architecture pair.
        "python" - Once per platform/architecture/python version triple.

        This defaults to "arch"

    `always`
        If True, this task will run even if it has been run as part of a
        previous build.

    `platforms`
        If not None, a string giving a comma-separated list of platforms that
        the task should be run on.

    `archs`
        If not None, a string giving a comma-separated architectures that the
        task should be run on.

    `pythons`
        If not None, a string giving a comma-separated list of python major
        versions the task should run on. ("3", "2", or "3,2")
    """

    def create_task(f):
        task = f.__name__
        name = f.__module__.split(".")[-1]
        Task(task, name, function=f, **kwargs)

        return f

    return create_task


# A list of annotation functions.
annotators = [ ]


def annotator(f):
    """
    Marks this function to be called before each task.
    """

    annotators.append(f)
    return f


# A list of tasks that are known.
tasks = [ ]

# A set of tasks that ran during the current session.
ran_tasks = set()
