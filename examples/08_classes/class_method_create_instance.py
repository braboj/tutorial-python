# Class method used to create instances
# --------------------------------------------------------------------------------
# A class method can serve as an alternative constructor. It receives the class
# as the first argument and builds a new instance from provided data. This
# approach collects creation logic in one place.

class Person(object):

    NAME_PREFIX = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, name):
        return cls(name)


p = Person.from_string("John")
print(p.name)
