# The typing module provides support for type hints in Python.
# ------------------------------------------------------------------------------
# The `typing` was introduced in Python 3.5 and provides a convention on how to
# use type hints in Python. In this regard, it provides a stricter naming
# convention for type hints compared to simple annotations.
#
# The `typing` module provides a set of classes and functions that can be used
# to define complex data types, such as lists, dictionaries, and tuples, with
# specific types for their elements.

from typing import Union, Final

# Define a constant
var: Final[int] = 100

# Define a function accepting multiple types for processing data
def process_data(data: Union[int, float, str]) -> str:

    if isinstance(data, (int, float)):
        return f"Numeric data processed: {data * 2}"

    elif isinstance(data, str):
        return f"String data processed: {data.upper()}"

    else:
        return "Unsupported data type"

print(process_data(10))
# Output: Numeric data processed: 20

print(process_data(3.14))
# Output: Numeric data processed: 6.28

print(process_data("hello"))
# Output: String data processed: HELLO
