from renpybuild.task import Task, Join, Platform, run
from renpybuild.machine import Machine

Machine([ "linux", "android" ])
Machine([ "mac" ])


for p in [ "linux", "mac", "android" ]:
    Platform(p)
    Task("a", once=True)
    Task("b", once=True)

Join()

for p in [ "linux", "mac", "android" ]:
    Platform(p)
    Task("c", deps={"a", "b"}, once=True)


run()
