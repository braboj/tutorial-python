# Check if two variables point to the same object (same object-ID)

a = [1, 2, 3]
b = a
print(b is a)

a = 1
b = 1
print(b is a)