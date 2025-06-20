# Dependency Inversion Principle - Bad Example
# ------------------------------------------------------------------------------
# The Dependency Inversion Principle (DIP) dictates that high level
# modules should not depend on low level ones directly.
#
# This example violates DIP by hard-coding a dependency on a specific
# math implementation instead of using an abstraction.

class Math(object):

        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def subtract(a, b):
            return a - b


class Calculator(object):

    def __init__(self):

        # CODE SMELL: Math object is hard-coded (dependency)
        # and not abstracted (injection)

        self.math = Math()

    def add(self, a, b):
        result = self.math.add(a, b)
        return result

    def subtract(self, a, b):
        result = self.math.subtract(a, b)
        return result
