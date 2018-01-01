import threading
import renpybuild.task
import traceback
import time


# A map from a platform to the machine that runs that platform.
machines = { }


class Machine:

    def __init__(self, platform):
        if not isinstance(platform, list):
            platform = [ platform ]

        for i in platform:
            machines[i] = self

        self.busy = False
        self.failed = False

    def run_task(self, task):
        print("Running", task)
        time.sleep(.5)
        return True

    def run_task_wrapper(self, task):
        try:
            success = self.run_task(task)

            if not success:
                print("Running {!r} failed.".format(task))
                self.failed = True

        except:
            traceback.print_exc()
            self.failed = True

        self.busy = False

        renpybuild.task.queue.notify()

    def run(self, task):

        self.busy = True
        threading.Thread(target=self.run_task_wrapper, args=(task,)).start()


def all_platforms():
    """
    Returns a set of all the platforms we know about.
    """

    return set(machines.keys())


def busy_platforms():
    """
    Returns a set of all platforms that are currently busy.
    """

    rv = set()

    for p, m in machines.items():
        if m.busy:
            rv.add(p)

    return rv


def all_idle():
    """
    Returns true if all machines are idle.
    """

    for i in machines.values():
        if i.busy:
            return False

    return True


def any_failed():
    """
    Returns true if any machine has failed.
    """

    for i in machines.values():
        if i.failed:
            return True

    return False


def find(platform):
    """
    Find a machine that can run tasks for `platform`.
    """

    m = machines.get(platform, None)

    if m is None:
        raise Exception("Could not find machine for {}.".format(platform))

    return m
