import jinja2
import shlex
import subprocess
import sys


def run(command, context):
    args = shlex.split(command)

    p = subprocess.run(args, cwd=context.cwd, env=context.environ)

    if p.returncode != 0:
        print(f"{context.task_name}: process failed with {p.returncode}.")
        print("args:", args)
        sys.exit(1)

