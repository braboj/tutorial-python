# List unpacking
# -----------------------------------------------------------------------------
# Using * with a list expands its items when calling a function.
"""
https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators
"""

test = [1, 2, 3]
print(test)

# Unpack list and print uses elements as arguments
print(*test)

# Unpack first element and then the rest
a, *b = test
print(a, b)

# Merge two lists
first = [1, 2, 3]
second = [4, 5, 6]
merged = [*first, *second]
print(merged)
