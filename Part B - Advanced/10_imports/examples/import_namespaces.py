# Example: Namespace of the builtins module

# Get the list of all built-in functions
print(dir(__builtins__))


class MyClass(object):
    pass


def func1():
    a = 1
    print(locals())         # Expected: {'a': 1}
    print(a)                # Expected: 1

    def func2():
        b = 2
        print(locals())     # Expected: {'b': 2}
        print(a, b)         # Expected: 1 2
        print(locals())     # Expected: {'b': 2, 'a': 1}

    func2()
    print(locals())  # Expected: {'a': 1, 'func2': ...}


# Get the global namespace
print(globals())
func1()
print(locals())  # Expected: {'func1': ...}
print(dir())
print(dir(MyClass))
