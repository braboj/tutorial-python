"""
repr(obj)
Printable representation of an object
"""


class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name )


print(repr(Person()))
