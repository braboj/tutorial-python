# Class instance with instance methods
# --------------------------------------------------------------------------------
# Demonstrates class instance with instance methods.

class Person(object):

    def do_something(self):
        print("{} is doing something".format(self))

    def do_something_with(self, something, someone):
        print("{} is doing {} with {}".format(self, something, someone))


# Create the instance
p = Person()
p.do_something()
p.do_something_with("nothing", "no one")
