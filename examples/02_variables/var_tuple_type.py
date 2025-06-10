# Tuple type in Python
# -----------------------------------------------------------------------------
# A tuple is very similar to a list that is immutable, meaning it cannot be
# changed after creation. Their main advantage is the memory efficiency
# and performance benefits they provide over lists, especially when dealing
# with large datasets. They also can be used as keys in dictionaries.
#
# - Immutable: Once created, the string cannot be changed.
# - Ordered: The characters in the string maintain their order.
# - Indexed: Each character in the string can be accessed by its index.
# - Heterogeneous: Strings can contain characters of different types

# Immutable (a change creates a new object)
tuple1 = (1, 2, 3)
tuple2 = tuple1 + (4, 5)
print(id(tuple1), id(tuple2))

# Ordered (characters maintain their order)
tuple3 = (1, 2, 3)
print(list(tuple3))
# Output: [1, 2, 3]

# Indexed (characters can be accessed by index)
tuple4 = (3, 2, 1)
print(tuple4[0])
# Output: 3

# Heterogeneous (can contain different types)
tuple5 = (1, "two", 3.0, True)
print(tuple5)
# Output: (1, 'two', 3.0, True)
