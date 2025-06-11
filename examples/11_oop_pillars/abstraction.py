# Abstraction: hiding details with abstract base classes
# -----------------------------------------------------------------------------
#
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
