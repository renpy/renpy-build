from renpybuild.task import NamedTask, Join, run
from renpybuild.machine import Machine

Machine([ "linux", "android" ])
Machine([ "mac" ])


NamedTask("a", "linux")
NamedTask("a", "mac")
NamedTask("a", "android")
NamedTask("b", "linux")
NamedTask("b", "mac")
NamedTask("b", "android")
Join()
NamedTask("c", "linux")
NamedTask("c", "mac")
NamedTask("c", "android")
Join()

run()
