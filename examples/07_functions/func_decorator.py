# Decorators to modify or extend function behavior
# -----------------------------------------------------------------------------
# A decorator is a function that takes another function as an argument,
# modifies or extends its behavior, and returns a new function. They are
# related to closures, as they can access variables from the enclosing scope.

def decorate(func):
    """A simple decorator function."""

    def wrapper(*args, **kwargs):
        """Wrapper function with additional behavior."""

        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with {args} and {kwargs}")
        return result

    return wrapper

@decorate
def hello_world():
    print('Hello world')

hello_world()

def hello_python():
    print('Hello Python')

hello_python = decorate(hello_python)
hello_python()
