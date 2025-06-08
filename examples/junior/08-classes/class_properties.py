# Example: Property used to encapsulate an instance variable

class Person(object):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected junior string")
        self.__name = value


p = Person("John")
print(p.name)
