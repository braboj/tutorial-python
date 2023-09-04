# Example : A good example that follows the Dependency Inversion Principle

class MathAbc(object):
    # GOOD: MathAbc is an abstraction that defines the contract for Math and
    # Calculator. It has no implementation details.

    @staticmethod
    def add(a, b):
        raise NotImplementedError()

    @staticmethod
    def subtract(a, b):
        raise NotImplementedError()


class Math(MathAbc):
    # GOOD: Both Math and Calculator depend on abstraction (MathAbc)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


class Calculator(object):
    # GOOD: Both Math and Calculator depend on abstraction (MathAbc)

    def __init__(self, math: MathAbc):
        self.math = math

    def add(self, a, b):
        result = self.math.add(a, b)
        return result

    def subtract(self, a, b):
        result = self.math.subtract(a, b)
        return result

