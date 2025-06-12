# Class method used to modify the class itself
# --------------------------------------------------------------------------------
# Because class methods receive the class as the first argument, they can change
# class-level attributes. This file modifies a shared value that affects all
# future instances.

class Person(object):

    NAME_PREFIX = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_prefix(cls, prefix):
        cls.NAME_PREFIX = prefix


p = Person("John")
Person.set_prefix("Dr.")
print(p.NAME_PREFIX)
