# Inspect function attributes
# --------------------------------------------------------------------------------
# Python stores a variety of metadata about functions on the function object
# itself. Attributes such as ``__name__``, ``__doc__`` and ``__code__`` can be
# inspected at runtime to learn more about a function's definition. This
# introspection ability is useful for debugging and for frameworks that
# manipulate functions.

def foo(a, b=10, c=20, *args, **kwargs):
    """This is 'foo' function that does nothing."""

    pi = 3.14

    def bar(a=1, b=2, c=3, *args, **kwargs):
        """This is 'bar' function that does nothing."""

        print(pi)

        introspections = {
            '__globals__': bar.__globals__,
            '__name__': bar.__name__,
            '__doc__': bar.__doc__,
            '__code__': bar.__code__,
            '__defaults__': bar.__defaults__,
            '__closure__': bar.__closure__,
            '__dict__': bar.__dict__,
        }

        # A function has a name
        test = introspections['__name__']
        print("Getting function attribute __name__ -> {} ".format(test))

        # A function has a docstring
        test = introspections['__doc__']
        print("Getting function attribute __doc__ -> {} ".format(test))

        # A function has default arguments
        test = introspections['__defaults__']
        print("Getting function attribute __defaults__ -> {} ".format(test))

        # A function has access to the global namespace
        test = introspections['__globals__']
        print("Getting function attribute __globals__ -> {} ".format(test))

        # A function has a closure
        test = introspections['__closure__']
        print("Getting function attribute __closure__ -> {} ".format(test))

        # A function has a variables dictionary
        test = introspections['__dict__']
        print("Getting function attribute __dict__ -> {} ".format(test))

        # A function has a code object
        test = introspections['__code__']
        print("Getting function attribute __code__ -> {} ".format(test))

        # A code object has name
        print(test.co_name)

    bar()


# foo(1, 2, 3, 4, 5, c=30, d=40, e=50)
foo(a=1, d=40, e=50)
