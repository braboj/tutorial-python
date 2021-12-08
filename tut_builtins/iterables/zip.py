"""
The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.

zip(*iterables)

The zip() function returns an iterator of tuples based on the iterable objects.

If we do not pass any parameter, zip() returns an empty iterator
If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the
iterables.

Suppose, two iterables are passed to zip(); one iterable containing three and other containing five elements. Then,
the returned iterator will contain three tuples. It's because iterator stops when the shortest iterable is exhausted.

"""

##############################################################################
# Zip with the same size

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

test = zip()
print(list(test))

test = zip(a)
print(list(test))

test = zip(a, b)
print(list(test))

##############################################################################
# Zip with different sizes

a = ['a', 'b', 'c']
b = [1, 2, 3, 4, 5]

test = zip(a, b)
print(list(test))

##############################################################################
# Unzip

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

zipped = zip(coordinate, value)
zipped_list = list(zipped)
print(zipped_list)

c, v = zip(*zipped_list)
print('c =', c)
print('v =', v)

