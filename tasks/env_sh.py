from renpybuild.context import Context
from renpybuild.task import task

import os

@task(platforms="all", always=True)
def unpack(c: Context):

    with open(c.expand("{{ install }}/env.sh"), "w") as f:

        for k, v in sorted(c.environ.items()):

            old_v = os.environ.get(k, '')

            if v == old_v:
                continue

            if old_v and v.endswith(old_v):
                v = v[:-len(old_v)] + '$' + k

            print(f"export {k}=\"{v}\"", file=f)

        print(f"export PS1=\"(r-b {c.platform}-{c.arch}) $PS1\"", file=f)
