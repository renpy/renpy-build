from renpybuild.model import task


@task(kind="host-python", always=True)
def iossupport_module(c):
    c.run("""install -d {{ install }}/lib/{{ pythonver }}/site-packages/""")
    c.run("""install {{ runtime }}/iossupport.py {{ install }}/lib/{{ pythonver }}/site-packages/""")
