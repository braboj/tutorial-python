# Abstract class in python 3+
# ------------------------------------------------------------------------------
# Python 3 provides native support for abstract base classes. The ABC and
# abstractmethod decorators ensure that child classes implement required
# behavior. Instances cannot be created until the abstract methods are
# overridden.

from abc import ABC, abstractmethod


class CalculatorAbc(ABC):

    def __init__(self, mode="basic"):
        self.mode = mode

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def subtract(self, *args, **kwargs):
        raise NotImplementedError


class Calculator(CalculatorAbc):

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(calc.add(1, 2))
print(calc.mode)
