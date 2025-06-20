# Parameterized decorators in Python
# ------------------------------------------------------------------------------
# Unfortunately, Python does not support passing parameters to decorators
# directly. A decorator of a function has always one argument, which is the
# original function to be decorated.
#
# In order to pass parameters to a decorator, we need to create an enclosing
# function that takes the decorator parameters and returns a decorator
# function.
#
# The decorator function will then take the original function as an argument
# and return a wrapper function modifying the behavior of the original function.

def log(message="Operation"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{message}: {func.__name__} called with args: {args}")
            return result
        return wrapper
    return decorator

@log()
def add(a, b):
    return a + b

@log("Custom log")
def sub(a, b):
    return a - b

def div(a, b):
    return a / b

add(5, 3)
# Output: Operation: add called with args: (5, 3)

sub(10, 4)
# Output: Custom log: sub called with args: (10, 4)

div = log("Division operation")(div)
div(10, 2)
# Output: Division operation: div called with args: (10, 2)
