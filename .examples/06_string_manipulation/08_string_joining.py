# String joining
# --------------------------------------------------------------------------------
# The `join()` method is a string method that takes an iterable (like a list)
# and concatenates its elements into a single string, with a specified separator
# between each element. If no separator is provided, it defaults to an empty
# string, effectively concatenating the elements without any characters in
# between.

tokens = '1 2 3 4 5 6 7 8 9'.split()
print(tokens)
# Output:
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

text = ''.join(tokens)
print(text)
# Output:
# 123456789

text = ' '.join(tokens)
print(text)
# Output:
# 1 2 3 4 5 6 7 8 9

text = ','.join(tokens)
print(text)
# Output:
# 1,2,3,4,5,6,7,8,9
