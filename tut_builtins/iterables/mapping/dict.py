# coding: utf-8

"""
The dict() constructor creates a dictionary in Python.

class dict(**kwarg)
class dict(iterable, **kwarg)
class dict(mapping, **kwarg)

"""

##############################################################################
# Example A: kwargs as named arguments
##############################################################################

test = dict(a=1, b=2, c=3, d=4)
print(test)

##############################################################################
# Example B: Iterable as collection of two element data
##############################################################################

# List of tuples
i = [("a", 1), ("b", 2)]
test = dict(i, c=3, d=4)
print(test)

# Tuple of lists
i = (['a', 1], ['b', 2])
test = dict(i, c=3, d=4)
print(test)

# Set of tuples
i = {("a", 1), ("b", 2)}
test = dict(i, c=3, d=4)
print(test)

##############################################################################
# Example C: Mapping as collection of key/value pairs
##############################################################################

m = {"a": 1, "b": 2}
test = dict(m, c=3, d=4)
print(test)

##############################################################################
# Example D: Dictionary operations
##############################################################################

test = {
    "a": 1,
    "b": 2
}

# Get all dictionary methods
print(dir(test))

# Get items, keys and values as iterables
print(test.items())
print(test.keys())
print(test.values())

# Access value using key
print(test.get("a"))
print(test["b"])

# Get value from key and remove key-value pair
print(test.pop("a"))
print(test)

# Add key-value pair
print(test.update(a=1))
print(test)

# Get last key-value pair and remove it (LIFO)
print(test.popitem())
print(test)

# Add key-value pair
print(test.update(a=1))
print(test)

# Copy dictionary to a new object
print(id(test))
print(id(test.copy()))

# Delete dictionary elements
test.clear()
print(test)

# Creates a new dictionary with keys from an iterable
keys = ("a", "b")
test = dict.fromkeys(keys, 0)
print(test)

# Get value and insert key-value pair if not present
test = {"a": 1}
print(test.setdefault("a", 0xFF))
print(test.setdefault("b", 0xFF))



