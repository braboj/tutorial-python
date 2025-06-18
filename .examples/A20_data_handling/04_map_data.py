# Mapping with map()
# -----------------------------------------------------------------------------
# map() applies a function to every element of an iterable, returning the results.


def sqr(x):
    return x * x


# Sample data
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Map using a mapping function (first) and an iterable (second)
iterator = map(sqr, sample)
print(list(iterator))

# Map using a lambda function (first) and an iterable (second)
iterator = map(lambda x: x * x, sample)
print(list(iterator))
