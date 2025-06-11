# Inheritance: deriving behavior from a base class
# -----------------------------------------------------------------------------
#
# Inheritance lets a class reuse and extend the behavior of a base class.
# Derived classes such as `Dog` and `Cat` inherit the methods from `Animal`
# and override them when needed.

class Animal(object):

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")

    def __str__(self):
        return "Animal: {}".format(self.name)


class Dog(Animal):

    def speak(self):
        print("I am a dog")

    def __str__(self):
        return "Dog: {}".format(self.name)


class Cat(Animal):

    def speak(self):
        print("I am a cat")

    def __str__(self):
        return "Cat: {}".format(self.name)


animal = Animal("Animal")
animal.speak()

dog = Dog("Dog")
dog.speak()

cat = Cat("Cat")
cat.speak()
