def foo(a, b=10, *args, c=20, **kwargs):
    """This is a function that does nothing."""
    return a + b + c

print(foo(1))
print(dir(foo))
print(foo.__name__)
print(foo.__doc__)
print(foo.__code__)
print(foo.__defaults__)
print(foo.__kwdefaults__)
print(foo.__annotations__)