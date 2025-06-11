# Dependency: relying on other classes to get work done
# -----------------------------------------------------------------------------
#
# A dependency is when a class uses another class to get its job done. The
# dependent class doesn't own the other object, it simply relies on it at
# runtime. Here the `Calculator` depends on the `Math` helper to perform the
# actual addition.

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
