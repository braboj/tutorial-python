# polymorphism

```python
# Polymorphism: shared interface, different implementations
# -----------------------------------------------------------------------------
# Polymorphism lets different classes implement the same interface in
# their own way.  Subclasses of `Animal` provide specific versions of
# `talk` and `eat` while client code can treat them uniformly.

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
```
