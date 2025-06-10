# List variables in Python
# -----------------------------------------------------------------------------
# The list type in Python is used to represent a collection of items. It is
# important to note that lists are passed by reference (see mutability in
# examples). When you assign a list to another variable, both variables point
# to the same list in memory. This means that changes made to one variable
# will affect the other variable as well. To create a copy of a list, you can
# use the `copy()` method or the slicing (e.g. `a = b[:]`). The list has the
# following properties:
#
# - Indexed: Elements can be accessed by their index
# - Mutable: Can be modified after creation
# - Ordered: Order of elements is preserved
# - Heterogeneous: Can contain elements of different types

# Indexed
a = [1, 2, 3]
print(a[0])
# Output: 1

# Mutable
b = [1, 2, 3]
b[0] = 4
print(b)
# Output: [4, 2, 3]

# Ordered
c = [2, 1, 3]
print(c)
# Output: [2, 1, 3]

# Heterogeneous
d = [1, 'two', 3.0]
print(d)
# Output: [1, 'two', 3.0]

# (!) Passing by reference (!)
l1 = [1, 2, 3]
l2 = l1
l2[0] = 4
print(l1, l2)
# Output: [4, 2, 3]

# Copying a list
l3 = l1.copy()
l3[0] = 5
print(l1, l3)
# Output: [4, 2, 3] [5, 2, 3]
