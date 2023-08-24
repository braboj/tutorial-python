# Example: Class method used to modify the class itself

class Person(object):

    name_prefix = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_prefix(cls, prefix):
        cls.name_prefix = prefix


p = Person("John")
Person.set_prefix("Dr.")
print(p.name_prefix)
