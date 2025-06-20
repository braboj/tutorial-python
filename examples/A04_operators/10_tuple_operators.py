# Tuple Operators in Python
# ------------------------------------------------------------------------------
# This example demonstrates common tuple operations including indexing,
# slicing, concatenation, repetition, and membership tests.

my_tuple = (1, 2, 3, 4, 5)

# Indexing
print(my_tuple[0])   # Output: 1
print(my_tuple[-1])  # Output: 5

# Slicing
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Concatenation
print(my_tuple + (6, 7))  # Output: (1, 2, 3, 4, 5, 6, 7)

# Repetition
print(my_tuple * 2)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Membership
print(3 in my_tuple)  # Output: True
print(9 in my_tuple)  # Output: False
