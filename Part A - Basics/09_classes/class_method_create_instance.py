# Example: Class method used to create instances

class Person(object):

    name_prefix = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, name):
        return cls(name)


p = Person.from_string("John")
print(p.name)
