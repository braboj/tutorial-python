# A class instance is as concrete realization of a class
# ------------------------------------------------------------------------------
# The code creates an instance of the Person class as a tangible object.
# The constructor assigns initial values to the instance. After creation, the
# object can call its methods and access stored data.

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, I am {} and my age is {}".format(self.name, self.age))


person = Person("John", 32)

# Access to the instance attributes
print(person.name)
print(person.age)
# Output:
# John
# 32

# Call the instance method
person.say_hello()
# Output:
# Hello, I am John and my age is 32
