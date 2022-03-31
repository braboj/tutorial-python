"""
sorted(iterable, key=None, reverse=False)

iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
reverse (Optional) - sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

"""

iterable = [2, 1, 4, 3]

test = sorted(iterable, reverse=False)
print(test)

test = sorted(iterable, reverse=True)
print(test)

iterable = {'b': 1, 'a': 2, 'd': 3, 'c': 4}

# Dictionary is converted to list of keys
test = sorted(iterable, reverse=True)
print(test)

# Another way of sorted keys
test = sorted(iterable.keys(), reverse=True)
print(test)

# Sorted values
test = sorted(iterable.values(), reverse=True)
print(test)

# Sorted dictionary by using the keys for the sorting
test = sorted(iterable.items(), reverse=True, key=lambda x: x[0])
print(test)

# Sorted dictionary by using the values for the sorting
test = sorted(iterable.items(), reverse=True, key=lambda x: x[1])
print(test)