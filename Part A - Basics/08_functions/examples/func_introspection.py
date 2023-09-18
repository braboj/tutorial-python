def foo(a, b=10, *args, c=20, **kwargs):
    """This is a function that does nothing."""

    pi = 3.14

    def bar(a=1, b=2, *args, c=3, **kwargs):
        """This is a function that does nothing."""

        print(pi)

        introspections = {
            '__globals__': bar.__globals__,
            '__name__': bar.__name__,
            '__doc__': bar.__doc__,
            '__code__': bar.__code__,
            '__defaults__': bar.__defaults__,
            '__kwdefaults__': bar.__kwdefaults__,
            '__closure__': bar.__closure__,
            '__annotations__': bar.__annotations__,
            '__dict__': bar.__dict__,
        }

        # A function has a name
        test = introspections['__name__']
        print(test)

        # A function has a docstring
        test = introspections['__doc__']
        print(test)

        # A function has default arguments
        test = introspections['__defaults__']
        print(test)

        # A function has keyword-only arguments
        test = introspections['__kwdefaults__']
        print(test)

        # A function has access to the global namespace
        test = introspections['__globals__']
        print(test)

        # A function has a closure
        test = introspections['__closure__']
        print(test)

        # A function has a variables dictionary
        test = introspections['__dict__']
        print(test)

        # A function has a code object
        test = introspections['__code__']
        print(test)

        # A code object has name
        print(test.co_name)

    bar()


foo(1, 2, 3, 4, 5, c=30, d=40, e=50)