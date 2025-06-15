# OOP Pillars

## Abstraction

```python
# Abstraction: hiding details with abstract base classes
# -----------------------------------------------------------------------------
# Abstraction defines a common interface while hiding implementation details.
# Using an abstract base class forces subclasses to implement specific
# behaviours without revealing how they will work.

from abc import ABCMeta, abstractmethod
from six import with_metaclass


class PersonAbc(with_metaclass(ABCMeta)):
    """An abstract base class defining what a person should be able to do."""

    def __init__(self):

        # Some common attributes that every Person has
        self.name = 'Bob'
        self.age = 42
        self.weight = 80
        self.height = 180

    @abstractmethod
    def walk(self):
        # Still abstract, because we don't know how a specific person walks.
        pass

    @abstractmethod
    def talk(self):
        # Still abstract, because we don't know how a specific person talks.
        pass

    @abstractmethod
    def eats(self):
        # Still abstract, because we don't know how a specific person eats.
        pass
```

## Access Modifiers

```python
# Access modifiers and name mangling
# -----------------------------------------------------------------------------
# Public attributes have no leading underscores and can be accessed from
# anywhere.  A single leading underscore marks an attribute as "protected" by
# convention, signalling it should only be used by the class and its
# subclasses.  A double underscore triggers name mangling which makes the
# attribute effectively private to the class.  This prevents accidental
# access from subclasses or external code.

class AccessModifiers(object):

    def __init__(self):

        # Public: Accessible from anywhere
        self.public = "public"

        # Protected: Accessible from the class and subclasses
        self._protected = "protected"

        # Private attribute -- the name will be mangled to _AccessModifiers__private
        # and is intended for use only inside this class
        self.__private = "private"


class AccessModifiersChild(AccessModifiers):

    def __init__(self):
        super(AccessModifiersChild, self).__init__()

        # Public: Accessible from anywhere
        print(self.public)

        # Protected: Accessible from the class and subclasses
        print(self._protected)

        # Private: name is mangled so direct access fails in the child class
        try:
            print(self.__private)

        except AttributeError as e:
            print(e)


test = AccessModifiersChild()
```

## Aggregation

```python
# Aggregation: objects hold references to independent parts
# -----------------------------------------------------------------------------
# Aggregation occurs when one object keeps references to other, independent
# objects.  The referenced parts can exist on their own and are not owned by
# the aggregator.  Here the `Rocket` receives an `Engine` instance that can
# outlive the rocket itself.

class Engine(object):

    def __init__(self, engine_type, engine_model):
        self.engine_type = engine_type
        self.engine_model = engine_model

    def start(self):
        print("{} engine started".format(self.engine_type))

    def stop(self):
        print("{} engine stopped".format(self.engine_type))


class SolidFuelEngine(Engine):

    def __init__(self, engine_model):
        super(SolidFuelEngine, self).__init__("solid fuel", engine_model)


class LiquidFuelEngine(Engine):

    def __init__(self, engine_model):
        super(LiquidFuelEngine, self).__init__("liquid fuel", engine_model)


class Rocket(object):

    def __init__(self, engine):
        # This is aggregation: the Rocket keeps a reference to an Engine
        # that was created outside. The engine is not owned by the Rocket
        # and could be reused elsewhere or exist on its own.
        self.engine = engine

    def launch(self):
        self.engine.start()


rocket1 = Rocket(SolidFuelEngine("model 1"))
rocket1.launch()

rocket2 = Rocket(LiquidFuelEngine("model 2"))
rocket2.launch()
```

## Association

```python
# Association: cooperating without ownership
# -----------------------------------------------------------------------------
# Association is a loose coupling between otherwise independent objects. They
# collaborate to accomplish a task but neither owns the lifetime of the other.
# In this example the `Calculator` uses a `Battery`, a `Display`, and the
# utility class `Math` without being responsible for their existence.

class Math(object):

    @staticmethod
    def add(a, b):
        return a + b


class Battery(object):

    def __init__(self, model):
        self.model = model

    def charge(self):
        print("Battery {} charging".format(self.model))

    def discharge(self):
        print("Battery {} discharging".format(self.model))


class FourLineDisplay(object):

    def __init__(self, model):
        self.model = model

    def display(self):
        print("Display {} displaying".format(self.model))

    def turn_off(self):
        print("Display {} turning off".format(self.model))

    def turn_on(self):
        print("Display {} turning on".format(self.model))


class Calculator(object):

    def __init__(self, display):
        self.display = display
        self.battery = Battery("default")

    def add(self, a, b):
        # The Calculator is associated with Math only to perform this
        # calculation.  Neither object owns the other.
        result = Math.add(a, b)
        return result

    def replace_battery(self, battery):
        self.battery = battery


calc = Calculator(display=FourLineDisplay(model="EL-W506T"))
calc.add(1, 1)
```

## Composition

```python
# Composition: owned components live and die with the owner
# -----------------------------------------------------------------------------
# Composition means that an object is made up of other objects which it
# owns completely.  When the container is destroyed so are its parts.
# The `Rocket` creates and manages its own `FuelTank`, which does not exist
# independently.

class FuelTank(object):

    def __init__(self, level=100):
        # Start the tank with a given fuel level
        self.level = level

    def fill(self, level):
        self.level = level

    def empty(self):
        self.level = 0


class Rocket(object):

    def __init__(self, fuel_level):
        # This is composition: the Rocket creates and owns the FuelTank.
        # When the rocket is destroyed the tank goes with it.
        self.tank = FuelTank(fuel_level)

    def launch(self):
        if self.tank.level == 100:
            print("Fuel tank is full")
        else:
            raise ValueError("Fuel tank is not full")

    def refill(self, level):
        self.tank.fill(level)
```

## Dependency

```python
# Dependency: relying on other classes to get work done
# -----------------------------------------------------------------------------
# A dependency is when a class uses another class to get its job done. The
# dependent class doesn't own the other object, it simply relies on it at
# runtime. Here the `Calculator` depends on the `Math` helper to perform the
# actual addition.

class Math(object):

    @staticmethod
    def add(a, b):
        return a + b


class Calculator(object):

    def __init__(self, model="default"):
        self.model = model

    def add(self, a, b):

        # Dependency relationship
        result = Math.add(a, b)
        return result


calc = Calculator()
calc.add(1, 1)
```

## Encapsulation

```python
# Encapsulation: guarding internal state with getters and setters
# -----------------------------------------------------------------------------
# Encapsulation hides internal state behind methods.  Properties provide a
# controlled interface so that validation logic in setters and getters can
# protect the data from invalid values or direct manipulation.

class Person(object):
    """Represents a person with controlled access to internal state."""

    def __init__(self, name, age):

        # Modify the access to the internal state
        self.__name = name
        self.__age = age

    @property
    def name(self):
        """ The getter for the name """
        return self.__name

    @name.setter
    def name(self, name):
        """ The setter for the name """

        # Protection logic
        if name is None:
            raise ValueError("name cannot be None")

        self.__name = name

    @property
    def age(self):
        """ The getter for the age """

        return self.__age

    @age.setter
    def age(self, age):
        """ The setter for the age """

        # Protection logic
        if age is None:
            raise ValueError("age cannot be None")

        elif age < 0:
            raise ValueError("age cannot be negative")

        elif age > 150:
            raise ValueError("age cannot be greater than 150")

        self.__age = age


person = Person("John", 30)
print(person.name)
print(person.age)
```

## Inheritance

```python
# Inheritance: deriving behavior from a base class
# -----------------------------------------------------------------------------
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
```

## Polymorphism

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
