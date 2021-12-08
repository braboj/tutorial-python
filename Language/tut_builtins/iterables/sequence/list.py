"""
list(iterable)

If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified.

"""

# Empty list
print(list())

# Sequences
test = ('a', 'b')
print(list(test))

test = "ab"
print(list(test))

test = ['a', 'b']
print(list(test))

test = enumerate(test)
print(list(test))

# Sets
test = {'a', 'b'}
print(list(test))

test = frozenset(test)
print(list(test))

# Mappings
test = {"a":1, "b":2}
print(list(test))


# Custom iterable
class MyIterable(object):

    def __init__(self, max_step=10):
        self.max_step = max_step

    def __iter__(self):
        self.step = 0
        return self

    def __next__(self):
        self.step += 1
        if self.step > self.max_step:
            raise StopIteration
        return self.step


test = iter(MyIterable(5))
print(list(test))

# Equivalent code
test = iter(MyIterable(5))
result = []
while True:
    try:
        result.append(next(test))
    except StopIteration:
        break

print(result)