i = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 8]

# Filter with function
f = filter(lambda x: x % 2, i)
print(list(f))

# Filter without function
f = filter(None, i)
print(list(f))





