a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)

a, b = (None, 1)
result = (a or b) if a or b is not None else None
print(result)