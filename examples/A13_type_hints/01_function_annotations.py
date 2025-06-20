# Annotations for Python Functions
# ------------------------------------------------------------------------------
# Annotations were introduced in Python 3.0 and allow developers to attach
# metadata to function parameters and return values. The metadata can be of
# any type, but it is commonly used to indicate the expected data types of
# parameters and the return value of a function.
#
# Annotations are not enforced at runtime, but they can be used by static
# type checkers, IDEs, and documentation generators to provide better
# support for developers. The annotations are stored in the `__annotations__`
# attribute of the function object.


def add(x: int, y: int) -> int:
    return x + y

def sub(x: "int", y: "int") -> "int":
    return x - y

print(add.__annotations__)
# Output: {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

print(sub.__annotations__)
# Output: {'x': 'int', 'y': 'int', 'return': 'int'}
