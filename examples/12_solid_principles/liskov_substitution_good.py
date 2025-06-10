# Example:  A good example that follows the Liskov Substitution Principle

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




