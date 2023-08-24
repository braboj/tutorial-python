# Example: Abstract class using the six library for Python 2

from six import with_metaclass
from abc import ABCMeta, abstractmethod


class CalculatorAbc(with_metaclass(ABCMeta)):

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
