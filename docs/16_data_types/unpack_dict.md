# unpack_dict

```python
# Dictionary unpacking
# -----------------------------------------------------------------------------
# The * operator can expand a mapping's items into function arguments or into new dictionaries.
"""
https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators
"""

test = {"a": 1, "b": 2, "c": 3}
print(test)

# Unpack dictionary
print(*test)
print(*test.keys())
print(*test.values())
print(*test.items())

# Unpack first element and then the rest
a, *b = test.items()
print(a, b)

# Merge two lists
first = {"A": 1, "B": 2}
second = {"C": 3, "D": 4}
merged = {**first, **second}
print(merged)
```
