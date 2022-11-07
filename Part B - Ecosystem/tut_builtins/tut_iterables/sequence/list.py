"""
list(iterable)

If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified.

"""

# Empty list
print([])
print(list())

# Convert tuple to list
test = ('a', 'b')
print(list(test))

# Convert string to list
test = "ab"
print(list(test))

# Copy list
a = ['a', 'b']
b = list(test)
print(a, id(a), b, id(b))

# Convert enumaration to list
test = enumerate(test)
print(list(test))

# Convert set to list
test = {'a', 'b'}
print(list(test))

# Convert dict to list
test = {"a": 1, "b": 2}
print(list(test))
