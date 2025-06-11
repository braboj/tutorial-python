# Merging and updating dictionaries
# -----------------------------------------------------------------------------
# Python 3.9 introduced the | and |= operators to combine dictionaries. The | 
# operator creates a new dictionary containing keys from both operands, while
# |= updates the dictionary on the left in place. This provides a concise
# alternative to using the update() method or ** unpacking for merging.

a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5}

# Merging two dictionaries using the | operator
c = a | b
print(c)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Updating a dictionary with another using the |= operator
a |= b
print(a)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
