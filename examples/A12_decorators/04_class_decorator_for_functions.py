# Class as a decorator for functions and methods
# ------------------------------------------------------------------------------
# Defining the __call__ method allows a class to wrap functions or methods.
# The decorator can maintain state between invocations and perform actions
# before or after calling the original function.


class Counter(object):

    def __init__(self, init_value=0):
        """ Initialize counter."""
        self._counter = init_value

    def __call__(self, function):
        """ Wrapping call to original function. """

        def wrapper(*args, **kwargs):
            """ Wrapper function."""
            try:
                self._counter += 1
                print("{}".format(self._counter))
                return function(*args, **kwargs)

            except Exception as e:
                print(e)

        return wrapper


def f():
    print("Hello World")


@Counter(0)
def g():
    print("Hello World")


print("#" * 80)

# Use the explicit decorator syntax
f = Counter(0)(f)

# Call the decorated functions
for _ in range(10):
    f()

print("#" * 80)

# Use Python's decorator syntax
for _ in range(10):
    g()
