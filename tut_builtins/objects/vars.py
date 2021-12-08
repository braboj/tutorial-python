"""
The vars() function returns the __dict__ attribute of the given object.

vars(object)

vars() returns the __dict__ attribute of the given object. If the object passed to vars() doesn't have the __dict__
attribute, it raises a TypeError exception. If no argument is passed to vars(), this function acts like locals()
function.

Note: __dict__ is a dictionary or a mapping object. It stores object's (writable) attributes.

"""

from pprint import pprint

class Foo:
    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b


test = Foo()
print(vars(test))

pprint(vars(list))
pprint(vars(str))
pprint(vars(dict))

