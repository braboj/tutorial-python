# https://cleverdevil.io/2009/python-metaclasses-demystified

import inspect
from six import with_metaclass


class AutoDecorateMeta(type):

    def __init__(cls, name, bases, namespace):
        super(AutoDecorateMeta, cls).__init__(name, bases, namespace)

        deco = namespace.get('decorator', lambda f: f)
        for key, value in namespace.items():

            # skip the decorator and constructor
            if key in ('decorator', '__init__'):
                continue

            # skip objects in the namespace that aren't methods
            if not inspect.isfunction(value):
                continue

            # apply the decorator
            setattr(cls, key, deco(value))


class Person(object, with_metaclass(AutoDecorateMeta)):

    # Decorator selector
    decorator = property

    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last

    # Will be decorated
    def name(self):
        return '%s %s' % (self.first, self.last)

    # Will be decorated
    def full_name(self):
        return '%s %s %s' % (self.first, self.middle, self.last)

    # Will be decorated
    def initials(self):
        return '%s%s%s' % (self.first[0], self.middle[0], self.last[0])


mlk = Person('Martin', 'Luther', 'King')

# Usual way to use name is as method
# mlk.name()
# Auto-decorated class converted method to property

print(mlk.name)
print(mlk.full_name)
print(mlk.initials)
