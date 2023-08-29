# Example: Initialization and validation

class Person(object):

        def __init__(self, name, age):
            self.name = name
            self.age = age

            if not isinstance(self.name, str):
                raise TypeError("Name must be a string")

            if not isinstance(self.age, int):
                raise TypeError("Age must be an integer")

            if self.age < 0:
                raise ValueError("Age must be a positive integer")

        def say_hello(self):
            print("Hello, my name is {} and my age is {}".format(self.name, self.age))


John = Person("John", 32)
John.say_hello()
