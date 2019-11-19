# A list of platforms.
import time


class Context:
    """
    This class is passed to the task to represent information about the
    current build.
    """

    def __init__(self, platform, arch, python, tmp):

        # The platform. One of "linux", "windows", "mac", "android", "ios", or "emscripten".
        self.platform = platform

        # The architecture. Varies based on the platform.
        self.arch = arch

        # The python version, one of "2" or "3".
        self.python = python

        # The path to where completed work is stored.
        self.built = tmp / "built"
        self.built.mkdir(parents=True, exist_ok=True)


class Task:
    """
    A task represents something that can be run to make the build process
    proceed.
    """

    def __init__(self, name, kind="arch", always=False):
        """
        `name`
            A unique name for this task.

        `kind`
            How often should the task run?
            "platform" - Once per platform.
            "arch" - Once per per platform, architecture pair.
            "python" - Once per (platform, architecture, python) triple.

        `always`
            If true, the task is always run during the current session.
            If false, only run if the task has not been run during prior
            sessions.
        """

        self.name = name
        self.kind = kind
        self.always = always

        tasks.append(self)

    def context_name(self, context):
        if self.kind == "platform":
            return f"{self.name}.{context.platform}"
        elif self.kind == "arch":
            return f"{self.name}.{context.platform}-{context.arch}"
        elif self.kind == "python":
            return f"{self.name}.{context.platform}-{context.arch}-py{context.python}"

    def run_task(self, context):
        name = self.context_name(context)

        if name in ran_tasks:
            return

        if (context.built / name).exists():
            return

        print("")
        print(f"Running {name}.")
        print("")

        self.run(context)

        ran_tasks.add(name)
        (context.built / name).write_text(str(time.time()))

    def run(self, context):
        return


# A list of tasks that are known.
tasks = [ ]

# A set of tasks that ran during the current session.
ran_tasks = set()
