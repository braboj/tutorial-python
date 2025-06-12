# String type in Python
# --------------------------------------------------------------------------------
# String variables in Python can be defined using single or double quotes.
# Both types of quotes are valid and can be used interchangeably. The string
# has the following characteristics:
#
# - Immutable: Once created, the string cannot be changed.
# - Ordered: The characters in the string maintain their order.
# - Indexed: Each character in the string can be accessed by its index.
# - Homogeneous: All characters in the string are of the same type.

# Immutable (a change creates a new object)
string1 = "Hello, world!"
string2 = string1.replace("world", "Python")
print(id(string1), id(string2))

# Ordered (characters maintain their order)
string3 = "Python"
print(list(string3))
# Output: ['P', 'y', 't', 'h', 'o', 'n']

# Indexed (characters can be accessed by index)
string4 = "Hello, world!"
print(string4[0])
# Output: 'H'

# Homogeneous (all characters are of the same type)
string5 = "Python" + 3
# Output: TypeError: can only concatenate str (not "int") to str
