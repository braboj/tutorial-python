"""
next(iterator, default)
"""

test = iter([1, 2, 3, 4, 5])

# Test next with default value
while True:
    value = next(test, -1)
    print(value)
    if value == -1:
        break