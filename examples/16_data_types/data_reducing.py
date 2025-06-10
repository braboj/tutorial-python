# Example: Reduce Data using the reduce() function

from functools import reduce

def total(x, y):
    return x + y


# Sample data
sample = [1, 1, 1]

# Map using a mapping function (first) and an iterable (second)
value = reduce(total, sample)
print(value)

# Map using a lambda function (first) and an iterable (second)
iterator = reduce(lambda x, y: x + y, sample)
print(value)
