# Class method used to modify the class itself
# --------------------------------------------------------------------------------
# Demonstrates class method used to modify the class itself.

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
