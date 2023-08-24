# Example: Class method used to modify existing instances of the class

class Person(object):

    name_prefix = "Mr."

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_prefix(cls, prefix):
        cls.name_prefix = prefix

    @classmethod
    def add_prefix(cls, person):
        person.name = "{} {}".format(cls.name_prefix, person.name)


p = Person("John")
Person.set_prefix("Dr.")
Person.add_prefix(p)
print(p.name)
