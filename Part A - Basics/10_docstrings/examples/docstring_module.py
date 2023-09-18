# Example: Docstrings for modules
# ======================================================================
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

This module provides a set of mathematical operations, including addition,
subtraction, multiplication, and division.

Usage:
    - Import this module using 'import math_operations'.
    - Call functions using 'math_operations.add()', 'math_operations.subtract()',
        'math_operations.multiply()', and 'math_operations.divide()'.

Example:
    >>> import math
    >>> math.sin(1)
    1
    >>> math.cos(1)
    0
"""


class HelperClass(object):
    """This is a helper class for the module"""
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
