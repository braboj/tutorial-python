"""
The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of
the results.
"""

# One iterable as argument
result = map(lambda x: x*2, [1, 2, 3])
print(list(result))

# Two iterables as argument
result = map(lambda x1, x2: x1+x2, [1, 2, 3], [4, 5, 6])
print(list(result))