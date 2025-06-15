# data_struct_with_buffer

```python
# Struct packing into buffers
# -----------------------------------------------------------------------------
# Packing directly into an existing buffer lets you build binary data without intermediate strings.

import struct


class Book(object):

    def __init__(self, title, author, price, year):
        self.title = title
        self.author = author
        self.price = price
        self.year = year


if __name__ == "__main__":

    # Create a book object
    book = Book(title='Python for Dummies', author='John Smith', price=25.0, year=2014)

    # Define the byte stream format (32s = 32 characters, f = float, i = integer), big-endian (>)
    format_string = '>32s 32s f i'

    # Create the buffer
    buffer_size = struct.calcsize(format_string)
    buffer = bytearray(buffer_size)

    # Pack the data into the buffer
    serialized = struct.pack(format_string,
                             book.title.encode('utf-8'),
                             book.author.encode('utf-8'),
                             book.price,
                             book.year
                             )

    # Print the size of the serialized object (32 + 32 + 4 + 4 = 72 bytes)
    print('Size of the serialized object: {} bytes'.format(struct.calcsize('32s 32s f i')))

    # Print the binary stream (72 bytes)
    print(serialized)

    # Deserialize the data
    title, author, price, year = struct.unpack_from(format_string, serialized)
    print(title.decode('utf-8').strip('\x00'))
    print(author.decode('utf-8').strip('\x00'))
    print(price)
    print(year)
```
