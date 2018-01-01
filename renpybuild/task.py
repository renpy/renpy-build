import os
import sys
import inspect
import enum
import threading

from renpybuild import BASE
import renpybuild.machine

# The list of tasks that need to be run to build a project.
queue = [ ]


class Join:
    """
    A special 'task' that causes processing to block until all prior tasks
    have been completed.
    """

    def __init__(self, blocked=None, blocks=None):
        self.blocked = blocked
        self.blocks = blocks

        queue.append(self)


class Task:
    """
    Represents a task that must be completed to build Ren'Py.
    """

    def __init__(self, platform):
        self.platform = platform
        queue.append(self)


class NamedTask(Task):
    def __init__(self, name, platform):
        super().__init__(platform)

        self.name = name

    def __repr__(self):
        return "Task {} on {}".format(self.name, self.platform)


class Queue:

    def __init__(self):

        self.queue = [ ]
        self.lock = threading.Condition()

    def append(self, task):
        self.queue.append(task)

    def notify(self):
        with self.lock:
            self.lock.notify()

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
                            m.run(task)

                            busy = busy | renpybuild.machine.busy_platforms()

                            break

                if wait:
                    self.lock.wait()


queue = Queue()


def run():
    queue.run()
