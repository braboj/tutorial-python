# Set data
# --------------------------------------------------------------------------------
# The set type in Python is a collection of elements with unique values. It
# used to remove duplicates from a collection and to perform set operations like
# union, intersection, and difference. The set type has the following
# characteristics:
#
# - Unique: A set cannot contain duplicate elements.
# - Mutable: You can add or remove elements from a set.
# - Unordered: The elements in a set do not have a specific order.
# - Heterogeneous: A set can contain elements of different data types.
# - Unindexed: You cannot access elements in a set by index

# Passing by reference
s1 = {1, 2, 3}
s2 = s1
s2.add(4)
print(s1, s2)
# Output: {1, 2, 3, 4} {1, 2, 3, 4}

# Copying a set
s3 = s1.copy()
s3.add(5)
print(s1, s3)

# All elements are unique
a = {1, 1, 2, 2, 3, 3}
print(id(a), a, sep=": ")
# Output: {1, 2, 3}

# Mutable: You can add and remove elements
a.add(4)
print(id(a), a, sep=": ")
# Output: {1, 2, 3, 4}

# Unordered: The order of elements is not guaranteed
b = {3, 1, 2}
print(id(b), b, sep=": ")
# Output: {1, 2, 3}

# Heterogeneous: A set can contain elements of different data types
c = {1, "two", 3.0, (4, 5)}
print(id(c), c, sep=": ")
# Output: {1, 'two', 3.0, (4, 5)}

# Unindexed: You cannot access elements by index
d = {1, 2, 3}
print(d[0])
# Output: TypeError: 'set' object is not subscriptable
