# Example: Class as decorator for functions


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


@Counter(0)
def f():
    print("Hello World")


for _ in range(10):
    f()