import time
import os

import jinja2

import renpybuild.run


class Context:
    """
    This class is passed to the task to represent information about the
    current build.
    """

    def __init__(self, platform, arch, python, root, tmp):

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

        # The environment dictionary.
        self.environ = dict(os.environ)

        # The non-environment variables dictionary.
        self.variables = { }

        self.var("platform", platform)
        self.var("arch", arch)
        self.var("source", self.root / "source")

        install = self.tmp / f"install.{platform}-{arch}"
        install.mkdir(parents=True, exist_ok=True)

        self.install = install
        self.var("install", install)

    def set_names(self, kind, task, name):
        """
        This is used to past the task-specific names into the context.

        """

        # These store the task and name, just short words that are constant.
        self.task = task
        self.name = name

        # These store the task_name and dir_name, as computed by Task.context.
        self.task_name = ""
        self.dir_name = ""

        if kind == "platform":
            self.dir_name = f"{self.name}.{self.platform}"
        elif kind == "arch":
            self.dir_name = f"{self.name}.{self.platform}-{self.arch}"
        elif kind == "python":
            self.dir_name = f"{self.name}.{self.platform}-{self.arch}-py{self.python}"

        self.task_name = f"{self.task}-{self.dir_name}"

        build = self.tmp / "build" / self.dir_name
        build.mkdir(parents=True, exist_ok=True)

        self.build = build
        self.cwd = build
        self.var("build", build)

        renpybuild.run.build_environment(self)

    def expand(self, s):
        """
        Expands `s` as a jinja template.
        """

        template = jinja2.Template(s)

        kwargs = dict()
        kwargs.update(self.environ)
        kwargs.update(self.variables)

        return template.render(**kwargs)

    def env(self, variable, value):
        """
        Adds environment variable `variable` with `value`.
        """

        self.environ[variable] = self.expand(str(value))

    def var(self, variable, value):
        """
        Adds a non-environment `variable` with `value`.
        """

        self.variables[variable] = self.expand(str(value))

    def chdir(self, d):
        self.cwd = self.cwd / self.expand(d)

    def run(self, command):
        """
        Runs `command`, and checks that the result is 0.

        `command`
            Is a string that is interpreted as a jinja2 template. The environment
            variables created with environ and the variables created with var
            are available for substitution into the template.

            Once substitution has occured, the command is split using shlex.split,
            and then is run using popen.
        """

        renpybuild.run.run(self.expand(command), self)


class Task:
    """
    A task represents something that can be run to make the build process
    proceed.
    """

    def __init__(self, task, name, *, function=None, kind="arch", always=False, platforms=None, archs=None, pythons=None):

        self.task = task
        self.name = name
        self.kind = kind
        self.always = always

        def split(v):
            if v is None:
                return v

            return { i.strip() for i in v.split(",") }

        self.platforms = split(platforms)
        self.archs = split(archs)
        self.pythons = split(pythons)

        self.function = function

        tasks.append(self)

    def context_name(self, context):
        """
        Returns a task_name, dir_name tuple.
        """

    def run(self, context):
        if (self.platforms is not None) and (context.platform not in self.platforms):
            return

        if (self.archs is not None) and (context.archs not in self.archs):
            return

        if (self.pythons is not None) and (context.python not in self.pythons):
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

        print(f"{context.task_name} running...")

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
        task, _, name = f.__name__.partition("_")
        Task(task, name, function=f, **kwargs)

        return f

    return create_task


# A list of tasks that are known.
tasks = [ ]

# A set of tasks that ran during the current session.
ran_tasks = set()
