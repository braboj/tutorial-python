# Liskov Substitution Principle - Bad Example
# ------------------------------------------------------------------------------
# The Liskov Substitution Principle (LSP) requires that subclasses
# can stand in for their base class. Here the work method checks
# for `Baby` explicitly, so `Baby` cannot substitute `Human`.

class Human(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{} eating".format(self.name))

    def sleep(self):
        print("{} sleeping".format(self.name))

    def work(self):

        # Code smell: Type checking or conditional logic to determine the
        # behaviour and thus the child class and the parent class are not
        # substitutable. We have junior divergent behaviour for Human and Baby
        # when the work method is called.

        if type(self) == Baby:
            raise RuntimeError("Too young to work")

        print("{} working".format(self.name))


class Baby(Human):

    def suckle(self):
        print("{} suckling".format(self.name))
