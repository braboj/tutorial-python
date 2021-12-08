"""
slice(stop)
slice(start, stop, step)

start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if
not provided.

"""

sequence = list(range(10))

s = slice(1)
print(sequence[s])
print(sequence[:1])

s = slice(1, None, None)
print(sequence[s])
print(sequence[1:])

s = slice(0, 2, None)
print(sequence[s])
print(sequence[0:2])

s = slice(0, 10, 2)
print(sequence[s])
print(sequence[0:10:2])

print(sequence[-1:])
print(sequence[:-1])
print(sequence[-8:-1])
print(sequence[-8:-1:2])