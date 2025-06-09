a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5}

# Merging two dictionaries using the | operator
c = a | b
print(c)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Updating a dictionary with another using the |= operator
a |= b
print(a)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
