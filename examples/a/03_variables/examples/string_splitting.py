# Split the string into a list of tokens using the split() method.
text = "1 2 3 4 5 6 7 8 9 10"
print(text.split())

# Split the string into a list of tokens using the split() method and the separator argument.
text = "1, 2, 3 4 5 6 7 8 9 10"
print(text.split(', '))

# Split the multi-line string into a list of tokens using the splitlines() method.
text = """ First line
Second line
Third line
"""
print(text.splitlines())
