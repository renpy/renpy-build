from renpybuild.context import Context
from renpybuild.task import task


@task(kind="host-python", always=True)
def iossupport_module(c: Context):
    c.run("""install -d {{ install }}/lib/{{ pythonver }}/site-packages/""")
    c.run("""install {{ runtime }}/iossupport.py {{ install }}/lib/{{ pythonver }}/site-packages/""")
