# Example: Class as template

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is {} and my age is {}".format(self.name, self.age))
