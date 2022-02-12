"""
https://stackoverflow.com/questions/306313/is-operator-behaves-unexpectedly-with-integers

Immutalbe objects are allocated and never changed. A variable is a reference or pointer to the
memory of the immutable object.

Immutable types: int, float, string, tuple
"""

# An integer object is created in memory and the variable points to it
from __future__ import print_function

test = 1
print(id(test))

# Integers are immutable, which means that operations on them will create a new object. The
# variable will point to the new object.
test += 1
print(id(test))

# Strings are immutable
test = "ABC"
try:
    test[0] = 'a'
except Exception as e:
    print(e)

# Tuples are immutable
test = ('A', 'B', 'C')
try:
    test[0] = 'a'
except Exception as e:
    print(e)

###############################################################################
# Examples

# Check the identity of integers
print([id(x) for x in range(-1, 2)])