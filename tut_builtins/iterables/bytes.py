"""
The bytes() method returns a immutable bytes object initialized with the given size and data.

bytes([source[, encoding[, errors]]])

source (Optional) - source to initialize the array of bytes.

Type	Description
String	Converts the string to bytes using str.encode() Must also provide encoding and optionally errors
Integer	Creates an array of provided size, all initialized to null
Object	A read-only buffer of the object will be used to initialize the byte array
Iterable Creates an array of size equal to the iterable count and initialized to the iterable elements Must be
iterable of integers between 0 <= x < 256
No source (arguments)	Creates an array of size 0


encoding (Optional) - if the source is a string, the encoding of the string.
errors (Optional) - if the source is a string, the action to take when the encoding conversion fails

"""

# Create an array with N elements
test = 10
result = bytes(test)
print(result)
print(list(result))

# Convert iterable to bytes
test = [1, 2, 3, 4, 5, 255]
result = bytes(test)
print(result)
print(list(result))

# Convert string to bytes
test = u'Хилшер'
result = bytes(test, encoding='utf-8')
print(result)
print(list(result))
