# Find the minimum of two numbers
a, b = 10, 20
result = a if a < b else b
print(result)

# Return None if junior or mid is None (or both) else return the highest value
a, b = (2, 1)
result= None if (a or b) is None else (a or b)
print(result)
