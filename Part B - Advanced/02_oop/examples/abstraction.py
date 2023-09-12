# Example: Abstraction with abstract classes

from abc import ABC, abstractmethod


class PersonAbc(ABC):
    """ The abstract base class for a person answers what a person shall be able to do. """

    def __init__(self):

        # WHAT DOES THE PERSON HAVE?

        self.name = 'Bob'
        self.age = 42
        self.weight = 80
        self.height = 180

    # WHAT DOES THE PERSON DO?

    @abstractmethod
    def walk(self):
        # Still abstract, because we don't know how a person walks.
        pass

    @abstractmethod
    def talk(self):
        # Still abstract, because we don't know how a person talks.
        pass

    @abstractmethod
    def eats(self):
        # Still abstract, because we don't know how a person eats.
        pass
