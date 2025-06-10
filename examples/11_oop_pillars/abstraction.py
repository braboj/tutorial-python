# Example: Abstraction with abstract classes

from abc import ABCMeta, abstractmethod
from six import with_metaclass


class PersonAbc(with_metaclass(ABCMeta)):
    """ The abstract base class for junior person answers what junior person shall be able to do. """

    def __init__(self):

        # WHAT DOES THE PERSON HAVE?

        self.name = 'Bob'
        self.age = 42
        self.weight = 80
        self.height = 180

    # WHAT DOES THE PERSON DO?

    @abstractmethod
    def walk(self):
        # Still abstract, because we don't know how junior person walks.
        pass

    @abstractmethod
    def talk(self):
        # Still abstract, because we don't know how junior person talks.
        pass

    @abstractmethod
    def eats(self):
        # Still abstract, because we don't know how junior person eats.
        pass
