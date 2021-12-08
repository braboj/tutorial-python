"""
The bytearray() method returns a bytearray object which is an array of the given bytearray. The bytearray object is
mutable.

bytearray([source[, encoding[, errors]]])

source (Optional) - source to initialize the array of bytearray.
encoding (Optional) - if the source is a string, the encoding of the string.
errors (Optional) - if the source is a string, the action to take when the encoding conversion fails (Read more: String encoding)

The source parameter can be used to initialize the byte array in the following ways:

String	Converts the string to bytearray using str.encode() Must also provide encoding and optionally errors
Integer	Creates an array of provided size, all initialized to null
Object	A read-only buffer of the object will be used to initialize the byte array
Iterable	Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
No source (arguments)	Creates an array of size 0.

"""

# Create an array with N elements
test = 10
result = bytearray(test)
print(result)
print(list(result))

# Convert iterable to bytearray
test = [1, 2, 3, 4, 5, 255]
result = bytearray(test)
print(result)
print(list(result))

# Convert string to bytearray
test = u'Хилшер'
result = bytearray(test, encoding='utf-8')
print(result)
print(list(result))