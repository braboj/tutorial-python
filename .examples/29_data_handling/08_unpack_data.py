# Unpacking snippets
# -----------------------------------------------------------------------------
# These small .examples show how the * operator can gather or scatter items from sequences.
test_string = "PYTHON"
test_list = [1, 2, 3, 4]
test_dict = {"A": 1, "B": 2}

# Unpack string
*test, = test_string
print(test)

# Unpack list
*test, = test_list
print(test)

# Unpack dictionary items
*test, = test_dict.items()
print(test)

# Copy dictionary
test = {**test_dict}
print(test)
print(test is test_dict)


# Dictionary unpacking
# -----------------------------------------------------------------------------
# The * operator can expand a mapping's items into function arguments or into new dictionaries.
"""
https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators
"""

test = {"a": 1, "b": 2, "c": 3}
print(test)

# Unpack dictionary
print(*test)
print(*test.keys())
print(*test.values())
print(*test.items())

# Unpack first element and then the rest
a, *b = test.items()
print(a, b)

# Merge two lists
first = {"A": 1, "B": 2}
second = {"C": 3, "D": 4}
merged = {**first, **second}
print(merged)

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
