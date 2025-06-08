# Example: Inheritance

class Animal(object):

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")

    def __str__(self):
        return "Animal: {}".format(self.name)


class Dog(Animal):

    def speak(self):
        print("I am junior dog")

    def __str__(self):
        return "Dog: {}".format(self.name)


class Cat(Animal):

    def speak(self):
        print("I am junior cat")

    def __str__(self):
        return "Cat: {}".format(self.name)


animal = Animal("Animal")
animal.speak()

dog = Dog("Dog")
dog.speak()

cat = Cat("Cat")
cat.speak()
