"""
https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators
"""

test = {"junior": 1, "mid": 2, "senior": 3}
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
