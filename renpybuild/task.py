from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import threading
import renpybuild.machine
import collections
import os

# The list of tasks that need to be run to build a project.
queue = [ ]


BUILT = os.path.join(renpybuild.BASE, "built")


class Join:
    """
    A special 'task' that causes processing to block until all prior tasks
    have been completed.
    """

    def __init__(self, blocked=None, blocks=None):
        self.blocked = blocked
        self.blocks = blocks

        self.name = None
        self.deps = None
        self.once = False

        queue.append(self)


default_platform = "master"


def Platform(platform):
    """
    Sets the platform for the next batch of tasks.
    """

    global default_platform
    default_platform = platform


class Task:
    """
    Represents a task that must be completed to build Ren'Py.
    """

    def __init__(self, name=None, deps=None, once=False, platform=None):

        if platform is None:
            platform = default_platform

        if platform != "master":

            if name is not None:
                if "." not in name:
                    name = name + "." + platform

            if deps is not None:
                new_deps = set()

                for i in deps:
                    if "." not in i:
                        new_deps.add(i + "." + platform)
                    else:
                        new_deps.add(i)

                deps = new_deps

        self.platform = platform
        self.name = name
        self.deps = deps
        self.once = once

        if self.deps and self.name is None:
            raise Exception("deps require name")

        if self.once and self.name is None:
            raise Exception("once requires name")

        if self.name:
            self.built_filename = os.path.join(BUILT, name)

        queue.append(self)

    def __repr__(self):
        return "<Task {}>".format(self.name or '')

    def should_build(self):
        if self.once and os.path.exists(self.built_filename):
            return False

        return True

    def mark_built(self):
        if not self.once:
            return

        with open(self.built_filename, "w"):
            pass

    def mark_unbuilt(self):
        if not self.once:
            return

        if os.path.exists(self.built_filename):
            os.unlink(self.built_filename)


class NamedTask(Task):
    def __init__(self, name, platform):
        super().__init__(platform=platform, name=name)

    def __repr__(self):
        return "Task {} on {}".format(self.name, self.platform)


class Queue:

    def __init__(self):

        self.task = { }
        self.task_revdeps = collections.defaultdict(set)

        self.queue = [ ]
        self.lock = threading.Condition()

    def append(self, task):
        self.queue.append(task)

        if task.name:
            self.task[task.name] = task

        if task.deps:
            for i in task.deps:
                self.task_revdeps[i].add(task)

    def finish(self, task, update_deps=True):
        with self.lock:
            self.lock.notify()

            if update_deps:

                task.mark_built()

                for i in self.task_revdeps[task.name]:
                    i.mark_unbuilt()

    def run(self):

        with self.lock:

            while True:

                if (not self.queue) or renpybuild.machine.any_failed():
                    if renpybuild.machine.all_idle():
                        break

                busy = renpybuild.machine.busy_platforms()

                wait = True

                for task in self.queue:

                    if isinstance(task, Join):
                        blocked = task.blocked or renpybuild.machine.all_platforms()
                        blocks = task.blocks or renpybuild.machine.all_platforms()
                        blocks = blocked | blocks

                        if not (busy & blocked):
                            wait = False
                            self.queue.remove(task)
                            break

                        else:
                            busy = busy | blocks

                        continue

                    if task.platform not in busy:

                        m = renpybuild.machine.find(task.platform)
                        if not m.busy:

                            wait = False
                            self.queue.remove(task)

                            if task.should_build():
                                m.run(task)
                                busy = busy | renpybuild.machine.busy_platforms()

                                break

                if wait:
                    self.lock.wait()


queue = Queue()


def run():
    if not os.path.exists(BUILT):
        os.mkdir(BUILT, 0o777)

    queue.run()
