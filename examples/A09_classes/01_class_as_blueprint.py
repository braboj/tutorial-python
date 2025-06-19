# Class as blueprint to create objects
# --------------------------------------------------------------------------------
# A class can act as a template from which many objects are built. This file
# defines a Person blueprint containing attributes and methods that every
# instance MUST have when created. Each instance of the Person class
# will have its own unique values for these attributes.

class Person(object):
    """The Person class serves as a blueprint for creating person objects."""

    # Person has what?
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Person can do what?
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create concrete instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.say_hello()
# Output: Hello, my name is Alice and I am 30 years old.

person2.say_hello()
# Output: Hello, my name is Bob and I am 25 years old.
