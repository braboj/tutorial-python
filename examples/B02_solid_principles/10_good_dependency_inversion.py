# Dependency Inversion Principle - Good Example
# ------------------------------------------------------------------------------
# The Dependency Inversion Principle (DIP) encourages depending on
# abstractions rather than concrete classes.
#
# This example demonstrates a simple math class that adheres to DIP. It defines
# an interface (IMath) that specifies the contract for math operations,
# allowing different implementations to be used without changing the
# dependent code (Calculator).


class IMath(object):
    """ Simplified interface for a math class """

    # GOOD: IMath is an abstraction that defines the contract for Math and
    # Calculator (the interface). It has no implementation details.

    @staticmethod
    def add(a, b):
        raise NotImplementedError()

    @staticmethod
    def subtract(a, b):
        raise NotImplementedError()


class Math(IMath):
    # GOOD: Both Math and Calculator depend on abstraction (MathAbc)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


class Calculator(object):
    """A simple calculator class

    Args:
        math (IMath): An object that implements the IMath interface

    """

    def __init__(self, math):
        # GOOD: Both Math and Calculator depend on abstraction (MathAbc)
        self.math = math

    def add(self, a, b):
        result = self.math.add(a, b)
        return result

    def subtract(self, a, b):
        result = self.math.subtract(a, b)
        return result
