# Example: Class as decorator for other classes

def Counter(cls=None, start=0):
    """Class decorator for counting instances of a class. """

    def wrap(class_to_decorate):
        class_to_decorate.counter = start
        return class_to_decorate

    # If we're called with parens, return a decorator function.
    if cls is None:
        # We're called with parens.
        return wrap

    # We're called without parens.
    return wrap(cls)


@Counter
class A(object):

    def __init__(self):
        print(self.counter)


A()


@Counter(start=101)
class B(object):
    def __init__(self):
        print(self.counter)


B()
