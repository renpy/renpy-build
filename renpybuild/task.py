import time


class Task:
    """
    A task represents something that can be run to make the build process
    proceed.
    """

    def __init__(self, task, name, function, *, kind="arch", always=False, platforms="-web", archs=None):

        if kind not in ("arch", "platform", "host", "cross"):
            raise Exception(f"Unknown kind {kind!r}.")

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

            rv = {i.strip() for i in v.split(",")}

            if negative:
                rv.add("negative")

            return rv

        self.platforms = split(platforms)
        self.archs = split(archs)

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

        if not check(self.platforms, context.platform):
            return

        if not check(self.archs, context.arch):
            return

        if self.kind == "host":
            context.platform = "host"
            context.arch = "host"

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

        print()

        ran_tasks.add(context.task_name)

        complete.write_text(str(time.time()))


def task(
    kind: str = "arch",
    always: bool = False,
    platforms: str = "-web",
    archs: str | None = None,
):
    """
    This is a decorator that wraps a function to define a task. The function must
    have a name of the form `task`_`name`. For example, "build_libz" or "unpack_python_38".

    This also takes optional keyword arguments.

    `kind`
        Determines how often this task shold run. One of:

        "arch" - Once per platform/architecture pair.
        "platform" - Once per platform.
        "host" - Only runs, compiling for the host.
        "cross" - Once per platform/architecture pair, compiling for the host, and targeting the "{{cross}}" directory for installs.

        This defaults to "arch".

    `always`
        If True, this task will run even if it has been run as part of a
        previous build.

    `platforms`
        If not None, a string giving a comma-separated list of platforms that
        the task should be run on.

    `archs`
        If not None, a string giving a comma-separated architectures that the
        task should be run on.
    """

    def create_task(f):
        task = f.__name__
        name = f.__module__.split(".")[-1]
        Task(task, name, f, kind=kind, always=always, platforms=platforms, archs=archs)

        return f

    return create_task


# A list of annotation functions.
annotators = []


def annotator(f):
    """
    Marks this function to be called before each task.
    """

    annotators.append(f)
    return f


# A list of tasks that are known.
tasks = []

# A set of tasks that ran during the current session.
ran_tasks = set()
