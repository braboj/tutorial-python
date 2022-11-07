# coding=utf-8

"""
str(object, encoding='utf-8', errors='strict')

The str()method takes three parameters:

object - The object whose string representation is to be returned. If not provided, returns the empty string
encoding - Encoding of the given object. Defaults of UTF-8 when not provided.
errors - Response when decoding fails. Defaults to 'strict'

There are six types of errors:

strict - default response which raises a UnicodeDecodeError exception on failure
ignore - ignores the unencodable Unicode from the result
replace - replaces the unencodable Unicode to a question mark
xmlcharrefreplace - inserts XML character reference instead of unencodable Unicode
backslashreplace - inserts a '\\uNNNN' escape sequence instead of unencodable Unicode
namereplace - inserts a '\\N{...}' escape sequence instead of unencodable Unicode

If encoding and errors parameter is provided, the first parameter, object, should be a bytes-like-object (bytes or
bytearray).

str() will first look for __str__ and if not found will use __repr__. This means, that almost every
object you implement should have a functional __repr__ that’s usable for understanding the object. Implementing
__str__ is optional: do that if you need a “pretty print” functionality (for example, used by a report generator).

The goal of __str__ is to be readable!!!

"""


class Test(object):

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


test = Test()
print(str(test))

b = bytes('pythön')
test = str(b)
print(test)
