# Liskov Substitution Principle - Good Example
# ------------------------------------------------------------------------------
# The Liskov Substitution Principle (LSP) means that objects of a
# superclass should be replaceable with objects of its subclasses
# without breaking the program. Each subclass here simply extends
# Human without special checks.

class Human(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{} eating".format(self.name))

    def sleep(self):
        print("{} sleeping".format(self.name))


class Adult(Human):

    # GOOD: Adult can be substituted for Human because it implements all the
    # methods of the Human class and it does not violate the Liskov
    # Substitution Principle.

    def work(self):
        print("{} working".format(self.name))


class Baby(Human):

    # GOOD: Baby can be substituted for Human because it implements all the
    # methods of the Human class and it does not violate the Liskov
    # Substitution Principle.

    def suckle(self):
        print("{} suckling".format(self.name))




