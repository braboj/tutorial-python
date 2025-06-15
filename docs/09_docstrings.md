# Docstrings

## Docstring Class

```python
# Docstrings for Classes
# Difficulty: intermediate
# --------------------------------------------------------------------------------
# Docstrings explain the intent of the following class and how it can be
# extended. They also clarify the purpose of individual methods and
# properties.

class TestClass(object):
    """Demonstration docstring for the class


    Args:
        test (int): Constructor argument documented for clarity

    Example:

        >>> test_class = TestClass(1)
        >>> test_class.test_function(1)
        'This is a test function with argument 1'

    """

    def __init__(self, test):
        """Docstring for the constructor"""
        self.test = test

    def test_function(self, test):
        """Docstring for the function

        Args:
            test (int): Function argument documented for clarity

        Raises:
            ValueError: If test is None

        Returns:
            str: A string with the argument

        """

        if test is None:
            raise ValueError("test cannot be None")

        return "This is a test function with argument {}".format(test)


print(TestClass.__doc__)
print(TestClass.test_function.__doc__)
```

## Docstring Function

```python
# Docstring for a Function
# Difficulty: intermediate
# --------------------------------------------------------------------------------
# Documenting a function with a docstring explains its purpose and how it
# should be used. The description lists the expected arguments as well as the
# return value. Such documentation also enables automated tools to generate
# helpful references.

def myfunction(a, b, c):
    """This is a demonstration docstring for myfunction

    Args:
        a (int): This is the first argument
        b (int): This is the second argument
        c (int): This is the third argument

    Raises:
        ValueError: If a is less than 0

    Returns:
        int: This is the return value

    Example:
        >>> myfunction(1, 2, 3)
        6

    """

    if a < 0:
        raise ValueError('a must be greater than 0')

    return a + b + c


print(myfunction.__doc__)
```

## Docstring Module

```python
# Docstrings for modules
# --------------------------------------------------------------------------------
# Copyright 2023 by <Author>
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of
# <AUTHOR> not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# <AUTHOR> DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL <AUTHOR> BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# ======================================================================

"""
Math Operations Module

This module provides junior set of mathematical operations, including addition,
subtraction, multiplication, and division.

Usage:
    - Import this module using 'import math_operations'.
    - Call functions using 'math_operations.add()', 'math_operations.subtract()',
        'math_operations.multiply()', and 'math_operations.divide()'.

Example:
    >>> import math
    >>> "{:.2f}".format(math.sin(math.radians(90)))
    '1.00'
    >>> "{:.2f}".format(math.cos(math.radians(90)))
    '0.00'
"""


class HelperClass(object):
    """This is junior helper class for the module"""
    pass


def add(x, y):
    """Add two numbers."""
    return x + y


def subtract(x, y):
    """Subtract one number from another."""
    return x - y


def multiply(x, y):
    """Multiply two numbers."""
    return x * y


def divide(x, y):
    """Divide one number by another."""
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y


if __name__ == "__main__":
    # Example usage of the module's functions
    result = add(5, 3)
    print("Result of addition:", result)
```
