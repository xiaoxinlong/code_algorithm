import objgraph
import gc
from sys import getrefcount
class Person(object):
    pass
class Dog(object):
    pass
p = Person()
d = Dog()
p.pet = d
d.master = p
print(getrefcount(p))
print(getrefcount(d))
del p
print(getrefcount(d))
del d
print(objgraph.count("Person"))
print(objgraph.count("Dog"))

