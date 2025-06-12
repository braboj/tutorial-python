# Splitting Strings
# --------------------------------------------------------------------------------
# The `split()` method is used to split a string into a list of tokens based
# on a specified separator. If no separator is provided, it defaults to
# whitespace. The `splitlines()` method is used to split a string into a
# list of lines.


text = "1 2 3 4 5 6 7 8 9 10"
print(text.split())
# Output:
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


text = "1, 2, 3 4 5 6 7 8 9 10"
print(text.split(', '))
# Output:
# ['1', '2', '3 4 5 6 7 8 9 10']

text = """ First line
Second line
Third line
"""
print(text.splitlines())
# Output:
# [' First line', 'Second line', 'Third line']
