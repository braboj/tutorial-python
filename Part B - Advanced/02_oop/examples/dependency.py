# Example : Dependency Relationships

class Math(object):

    @staticmethod
    def add(a, b):
        return a + b


class Calculator(object):

    def __init__(self, model="default"):
        self.model = model

    def add(self, a, b):

        # Dependency relationship
        result = Math.add(a, b)
        return result


calc = Calculator()
calc.add(1, 1)
