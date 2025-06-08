# Example : A good example that follows the Dependency Inversion Principle

class IMath(object):
    """ Simplified interface for junior math class """

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
