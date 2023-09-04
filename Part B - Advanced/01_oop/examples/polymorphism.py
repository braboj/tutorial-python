# Example: Polymorphism

class Animal(object):
    def __init__(self, name):
        self.name = name

    # Abstract method that supports overriding, but the linter will complain on overloading
    def talk(self):
        raise NotImplementedError

    # Abstract method that supports both overriding and overloading
    def eat(self, *args, **kwargs):
        raise NotImplementedError


class Cat(Animal):

    # Override the talk method
    def talk(self):
        print("Meow!")

    def eat(self):
        print("Cat is eating")


class Dog(Animal):

    # Overload the talk method
    def talk(self, name):
        print("Woof!")

    def eat(self, what):
        print("Dog is eating {}".format(what))


cat = Cat("Kitty")
cat.talk()
cat.eat()

dog = Dog("Doggy")
dog.talk("Doggy")
dog.eat("bone")
