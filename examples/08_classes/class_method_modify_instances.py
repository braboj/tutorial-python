# Class method used to modify existing instances of the class
# --------------------------------------------------------------------------------
# Class methods can operate on a collection of instances maintained by the
# class. The method updates every stored object in a single call. Centralizing
# the logic keeps modifications consistent across all instances.

class Person(object):

    NAME_PREFIX = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_prefix(cls, prefix):
        cls.NAME_PREFIX = prefix

    @classmethod
    def add_prefix(cls, person):
        person.name = "{} {}".format(cls.NAME_PREFIX, person.name)


p = Person("John")
Person.set_prefix("Dr.")
Person.add_prefix(p)
print(p.name)
