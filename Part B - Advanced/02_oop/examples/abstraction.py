# Example: Abstraction with abstract classes

from abc import ABC, abstractmethod


class PersonAbc(ABC):
    """ The abstract base class for a person answers what a person shall be able to do. """

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass