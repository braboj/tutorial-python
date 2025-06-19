# Tuple data
# --------------------------------------------------------------------------------
# A tuple is very similar to a list that is immutable, meaning it cannot be
# changed after creation. Their main advantage is the memory efficiency
# and performance benefits they provide over lists, especially when dealing
# with large datasets. They also can be used as keys in dictionaries.
#
# - Immutable: Once created, the tuple cannot be changed.
# - Ordered: The elements in the tuple maintain their order.
# - Indexed: Each element in the tuple can be accessed by its index.
# - Heterogeneous: Tuples can contain characters of different types

# Immutable (a change creates a new object)
tuple1 = (1, 2, 3)
tuple2 = tuple1
print(tuple2 is tuple1)     # Check if both variables point to the same object
tuple2 += (4, 5)
print(tuple2 is tuple1)     # After modification, they are different objects
# Output:
# False
# True

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
