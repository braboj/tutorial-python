# data_filtering

```python
# Filtering with filter()
# -----------------------------------------------------------------------------
# The built-in filter() returns elements for which a function returns True.


def is_even(x):
    return x % 2 == 0


# Sample data
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter using a filtering function (first) and an iterable (second)
iterator = filter(is_even, sample)
print(list(iterator))

# Filter using a lambda function (first) and an iterable (second)
iterator = filter(lambda x: x % 2 == 0, sample)
print(list(iterator))
```
