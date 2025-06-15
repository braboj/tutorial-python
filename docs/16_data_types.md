# Data Types

## Comprehension Dictionary

```python
# Dictionary comprehensions
# -----------------------------------------------------------------------------
# Dictionary comprehensions let you construct mappings concisely. They are ideal for transforming one form of data into key/value pairs.

existing_list = [1, 2, 3, 4, 5]
existing_dictionary = {1: "junior", 2: "mid", 3: "c", 4: "d", 5: "e"}

# Dictionary comprehension with list
new_dictionary_1 = {number: number**2 for number in existing_list}

# Dictionary comprehension with existing dictionary
new_dictionary_2 = {key: "_"+value+"_" for (key, value) in existing_dictionary.items()}

# Dictionary comprehension with existing dictionary and conditions
new_dictionary_3 = {key: "_"+value+"_" for (key, value) in existing_dictionary.items() if key < 5 if value != "mid"}


print(new_dictionary_1)
print(new_dictionary_2)
print(new_dictionary_3)
```

## Comprehension List

```python
# List comprehensions
# -----------------------------------------------------------------------------
# List comprehensions allow you to create or filter lists concisely without explicit loops.

existing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension without condition
new_list_1 = [number**2 for number in existing_list]

# List comprehension with condition
new_list_2 = [number**2 for number in existing_list if number < 6]

print(new_list_1)
print(new_list_2)
```

## Data Array

```python
# Efficient arrays
# -----------------------------------------------------------------------------
# The array module stores numeric values more efficiently than lists because all elements share the same type.

import array


def test_int():

    # Create an array of integers
    int_array = array.array('i', [1, 2, 3, 4, 5])

    # Convert the array to a bytes object (useful for binary data)
    bytes_data = int_array.tobytes()
    print(bytes_data)

    # Convert a bytes object back to an array
    new_array = array.array('i')
    new_array.frombytes(bytes_data)
    print(new_array)

    print()


def test_unicode():

    # Use unicode characters
    unicode_array = array.array('u', "Здравейте, хора!")

    # Convert the array to a bytes object (useful for binary data)
    bytes_data = unicode_array.tobytes()
    print(bytes_data)

    # Convert a bytes object back to an array
    new_array = array.array('u')
    new_array.frombytes(bytes_data)
    print(new_array)

    print()


if __name__ == "__main__":
    test_int()
    test_unicode()
```

## Data Base64

```python
# Base64 encoding
# -----------------------------------------------------------------------------
# Base64 converts binary data to ASCII text. This is handy when transmitting bytes over text-based protocols.

import base64

# Convert the string to bytes
text_expected = 'Здравейте, хора!'
text_stream = text_expected.encode('utf-8')

# Encode the byte stream in Base64
encoded = base64.b64encode(text_stream)
print(encoded)

# Decode the byte stream from Base64
decoded = base64.b64decode(encoded)

# Print the decoded string
text_obtained = decoded.decode('utf-8')
print(text_obtained)

# Assert that the expected and obtained strings are equal
assert text_expected == text_obtained
```

## Data Binascii

```python
# Binary-to-ASCII conversions
# -----------------------------------------------------------------------------
# The binascii module exposes low-level routines for converting between binary data and various ASCII encodings.


import binascii


def test_base64():

    print("Test Base64")

    # Convert the string to bytes
    text_out = 'Здравейте, хора!'
    text_stream = text_out.encode('utf-8')
    print(text_out)

    # Encode the byte stream in Base64
    encoded = binascii.b2a_base64(text_stream)
    print(encoded)

    # Decode the byte stream from Base64
    decoded = binascii.a2b_base64(encoded)
    print(decoded)

    # Print the decoded string
    text_in = decoded.decode('utf-8')
    print(text_in)

    # Assert that the expected and obtained strings are equal
    assert text_in == text_out

    print()


def test_hex():

    print("Test Hex")

    # Convert the string to bytes
    text_out = 'Здравейте, хора!'
    text_stream = text_out.encode('utf-8')
    print(text_out)

    # Encode the byte stream in hexadecimal
    encoded = binascii.b2a_hex(text_stream)
    print(encoded)

    # Decode the byte stream from hexadecimal
    decoded = binascii.a2b_hex(encoded)
    print(decoded)

    # Print the decoded string
    text_in = decoded.decode('utf-8')
    print(text_in)

    # Assert that the expected and obtained strings are equal
    assert text_in == text_out

    print()


def test_uu():

    print("Test UUEncode")

    # Convert the string to bytes
    text_out = 'Здравейте, хора!'
    text_stream = text_out.encode('utf-8')
    print(text_out)

    # Encode the byte stream in uuencode
    encoded = binascii.b2a_uu(text_stream)
    print(encoded)

    # Decode the byte stream from uuencode
    decoded = binascii.a2b_uu(encoded)
    print(decoded)

    # Print the decoded string
    text_in = decoded.decode('utf-8')
    print(text_in)

    # Assert that the expected and obtained strings are equal
    assert text_in == text_out

    print()


if __name__ == "__main__":
    test_base64()
    test_hex()
    test_uu()
```

## Data Chainmap

```python
# Combining dictionaries with ChainMap
# -----------------------------------------------------------------------------
# ChainMap lets you combine several dictionaries into a single view without copying them.

from collections import ChainMap

# Create two dictionaries
dict1 = {'junior': 1, 'mid': 2}
dict2 = {'c': 3, 'd': 4}

# Create a ChainMap
chain = ChainMap(dict1, dict2)

# Print the ChainMap
print(chain)

# Print elements
print(list(chain.items()))

# Find value of a key from dict1
print(chain['a'])

# Find value of a key from dict2
print(chain['c'])
```

## Data Codecs

```python
# Encoding text with codecs
# -----------------------------------------------------------------------------
# The codecs module provides tools for encoding and decoding streams of text in different character sets.

import codecs
import pprint


def test_utf8():

    print("Test UTF-8")

    text = 'Здравейте, хора!'
    print(text)

    encoded = codecs.encode(text, 'utf-8')
    print(encoded)

    decoded = codecs.decode(encoded, 'utf-8')
    print(decoded)

    info = codecs.lookup('utf-8')
    print("lookup() -> ", info)

    print()


def test_utf16():

    print("Test UTF-16")

    text = 'Здравейте, хора!'
    print(text)

    encoded = codecs.encode(text, 'utf-16')
    print(encoded)

    decoded = codecs.decode(encoded, 'utf-16')
    print(decoded)

    info = codecs.lookup('utf-16')
    print("lookup() -> ", info)

    print()


def test_base64():

    print("Test Base64")

    text = 'Здравейте, хора!'
    print(text)

    encoded = codecs.encode(text.encode('utf-8'), 'base64')
    print(encoded)

    decoded = codecs.decode(encoded, 'base64')
    print(decoded.decode('utf-8'))

    info = codecs.lookup('base64')
    print("lookup() -> ", info)

    print()


if __name__ == "__main__":

    test_utf8()
    test_utf16()
    test_base64()
```

## Data Codecs Custom

```python
# Custom codecs
# -----------------------------------------------------------------------------
# Registering a custom codec allows you to handle data stored in a specialized encoding.

import codecs


class ROT13Codec(codecs.Codec):
    # ROT13 Cipher - see https://en.wikipedia.org/wiki/ROT13

    def encode(self, stream, errors='strict'):

        # Result is a list of characters
        encoded = []

        # Iterate over the input stream
        for char in stream:

            # Encode lower case letters
            if 'a' <= char <= 'z':
                offset = ord('a')
                encoded_char = chr(((ord(char) - offset + 13) % 26) + offset)

            # Encode upper case letters
            elif 'A' <= char <= 'Z':
                offset = ord('A')
                encoded_char = chr(((ord(char) - offset + 13) % 26) + offset)

            # Other characters are not encoded
            else:
                encoded_char = char

            # Append encoded character to the resulting list
            encoded.append(encoded_char)

        # Return the encoded bytes and the length of the input stream
        return ''.join(encoded), len(stream)

    def decode(self, stream, errors='strict'):
        # ROT13 is its own inverse
        return self.encode(stream, errors)

    def lookup(self, encoding):

        if encoding == 'rot13':
            codec = codecs.CodecInfo(
                name='rot13',
                encode=self.encode,
                decode=self.decode,
            )

        else:
            codec = None

        return codec


# Register the codec with the codecs module before using it
codecs.register(ROT13Codec().lookup)

# Usage
encoded_text = codecs.encode("Hello, World!", encoding='rot13')
print(encoded_text)  # Output: "Uryyb, Jbeyq!"

decoded_text = codecs.decode(encoded_text, encoding='rot13')
print(decoded_text)  # Output: "Hello, World!"
```

## Data Copying

```python
# Deep and shallow copying
# -----------------------------------------------------------------------------
# Shallow and deep copying let you duplicate complex objects without affecting the originals.

import copy

# Create a deeply nested dictionary
numbers_dict = {
    "numbers": {
        "integers": [1, 2, 3, 4, 5],
        "floats": [1.1, 2.2, 3.3, 4.4, 5.5]
    }
}

# Create a shallow copy of the dictionary
shallow_copy = copy.copy(numbers_dict)

# Create a deep copy of the dictionary
deep_copy = copy.deepcopy(numbers_dict)

# Modify the original dictionary
numbers_dict["numbers"]["integers"].append(6)
numbers_dict["numbers"]["floats"].append(6.6)

# Print the original dictionary (modified)
print("Original", numbers_dict)

# Print the shallow copy (modified)
print("Shallow", shallow_copy)

# Print the deep copy (not modified)
print("Deep", deep_copy)
```

## Data Counter Class

```python
# Counting with Counter
# -----------------------------------------------------------------------------
# A Counter is a dictionary subclass for tallying hashable objects quickly.

from collections import Counter

# Create a Counter object
a = Counter('abcdeabcdabcaba')
b = Counter(reversed("abcdeabcdabcaba"))

# Print the Counter object
print(a)
print(b)

# Print the three most common element
print(a.most_common(3))
print(b.most_common(3))

# Add two Counter objects
c = a + b
print(c)

# Subtract two Counter objects
d = a - b
print(d)
```

## Data Dataclass

```python
# Lightweight data classes
# -----------------------------------------------------------------------------
# Dataclasses eliminate boilerplate when defining classes meant primarily to store data.

import dataclasses
from dataclasses import dataclass, field
from typing import List


@dataclass
class DataClass(object):
    name: str
    value: int

    def __post_init__(self):
        self.value = self.value * 2

    def __str__(self):
        return f"{self.name}: {self.value}"


@dataclass
class DataClassWithDefaults(DataClass):

    name: str = "MyData with defaults"
    value: int = 0
    data: List[int] = field(default_factory=list)

    def add_value(self, value):
        self.data.append(value)

    def __str__(self):
        return f"{self.name}: {self.value}, {self.data}"


if __name__ == "__main__":

    my_data = DataClass(name="MyData", value=10)
    print(my_data)

    my_data = DataClassWithDefaults()
    my_data.add_value(1)
    print(my_data)
```

## Data Defaultdict

```python
# Automatic keys with defaultdict
# -----------------------------------------------------------------------------
# defaultdict automatically creates missing keys so your code doesn't need explicit checks.

from collections import defaultdict


def test_default_factory(factory):

    d = defaultdict(factory)

    # Test the defaultdict
    try:
        print(d['key1'])
        print(d['key2'])
        print(d['key3'])

    except KeyError as e:
        print("KeyError: {}".format(e))
        assert True

    print()


if __name__ == "__main__":

    default_factories = [
        None,               # Behaves like a regular dictionary
        str,                # Returns an empty string if the key is not found
        int,                # Returns 0 if the key is not found
        float,              # Returns 0.0 if the key is not found
        list,               # Returns an empty list if the key is not found
        tuple,              # Returns an empty tuple if the key is not found
        dict,               # Returns an empty dictionary if the key is not found
        set,                # Returns an empty set if the key is not found
        lambda: 'value',    # Returns a default value if the key is not found
    ]

    for default_factory in default_factories:
        test_default_factory(default_factory)
```

## Data Deque Fifo

```python
# Deque as FIFO queue
# -----------------------------------------------------------------------------
# Deque offers fast O(1) operations at both ends, making it ideal for implementing queues.

from collections import deque


def emtpy_deque(customers):

    # Test the deque
    while True:
        try:

            # Get the item from the right
            item = customers.pop()
            print("Get item: {}".format(item))

        except IndexError as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_deque(customers):

    items = ['Ivan', 'Dragan', 'Petkan', 'Stoyan']

    for item in items:
        customers.appendleft(item)
        print("Add item: {}".format(item))

    print()


if __name__ == "__main__":

    # Create a deque
    d = deque()

    # Fill the deque
    fill_deque(d)

    # Empty the deque
    emtpy_deque(d)
```

## Data Deque Lifo

```python
# Deque as LIFO stack
# -----------------------------------------------------------------------------
# Using deque as a stack provides efficient push and pop operations.

from collections import deque


def emtpy_deque(plates):

    # Test the deque
    while True:
        try:

            # Get the item from the right
            item = plates.pop()
            print("Get item: {}".format(item))

        except IndexError as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_deque(plates):

    items = ['Soup plate', 'Salad plate', 'Dinner plate', 'Dessert plate']

    for item in items:
        plates.append(item)
        print("Add item: {}".format(item))

    print()


if __name__ == "__main__":

    # Create a deque
    d = deque()

    # Fill the deque
    fill_deque(d)

    # Empty the deque
    emtpy_deque(d)
```

## Data Dill

```python
# Serializing with dill
# -----------------------------------------------------------------------------
# dill extends pickle and can serialize a wider range of Python objects.

import dill
import sys


class Book(object):

    def __init__(self, title, author, price, year):
        self.title = title
        self.author = author
        self.price = price
        self.year = year


if __name__ == "__main__":

    # Create a book object
    book = Book(title='Python for Dummies', author='John Smith', price=25.0, year=2014)

    # Print the book object
    print(book.__dict__)

    # Serialize the book object
    serialized_book = dill.dumps(book)

    # Print the size of the serialized object
    print('Size of the serialized object: {} bytes'.format(sys.getsizeof(serialized_book)))

    # Print the serialized object
    print(serialized_book)

    # Deserialize the book object
    deserialized_book = dill.loads(serialized_book)

    # Print the book object
    print(deserialized_book.__dict__)
```

## Data Filtering

```python
# Filtering with filter()
# -----------------------------------------------------------------------------
# The built-in filter() returns elements for which a function returns True.


def is_even(x):
    return x % 2 == 0


# Sample data
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter using a filtering function (first) and an iterable (second)
iterator = filter(is_even, sample)
print(list(iterator))

# Filter using a lambda function (first) and an iterable (second)
iterator = filter(lambda x: x % 2 == 0, sample)
print(list(iterator))
```

## Data Heapq

```python
# heapq priority queue
# -----------------------------------------------------------------------------
# A heap lets you maintain a priority queue with O(log n) push/pop operations.

import heapq


def empty_heapq(h):
    # Test the heapq
    while True:
        try:
            print(heapq.heappop(h))

        except IndexError as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_heapq(h):

    # Add items to the heapq
    heapq.heappush(h, 4)
    heapq.heappush(h, 1)
    heapq.heappush(h, 7)


if __name__ == "__main__":

    # Create a heapq
    heap = []
    heapq.heapify(heap)

    # Fill the heapq
    fill_heapq(heap)

    # Empty the heapq
    empty_heapq(heap)
```

## Data Mapping

```python
# Mapping with map()
# -----------------------------------------------------------------------------
# map() applies a function to every element of an iterable, returning the results.


def sqr(x):
    return x * x


# Sample data
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Map using a mapping function (first) and an iterable (second)
iterator = map(sqr, sample)
print(list(iterator))

# Map using a lambda function (first) and an iterable (second)
iterator = map(lambda x: x * x, sample)
print(list(iterator))
```

## Data Namedtuple

```python
# Named tuples
# -----------------------------------------------------------------------------
# namedtuples give tuple-like objects readable field names without extra overhead.

from collections import namedtuple

# Create a namedtuple (label, fields)
#   - The label will be used in the representation of the namedtuple
#   - The fields will be used to access the namedtuple attributes

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

# Test the namedtuple representation
print(p)

# Test the namedtuple attributes
print(p.x)
print(p.y)

# Test the namedtuple index access
print(p[0])
print(p[1])
```

## Data Ordered Dict

```python
# Ordered dictionaries
# -----------------------------------------------------------------------------
# OrderedDict remembers the insertion order of keys, which can be useful for reproducible iteration.

from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict()

# Add elements
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

# Print the OrderedDict
print(od)

# Move 'c' to the end
od.move_to_end('c')

# Print the OrderedDict
print(od)

# Move 'c' to the start
od.move_to_end('c', last=False)

# Print the OrderedDict
print(od)
```

## Data Packing

```python
# Packing *args and **kwargs
# -----------------------------------------------------------------------------
# Packing arguments allows functions to accept an arbitrary number of positional or keyword parameters.

def func1(*args):

    # args is a tuple of arguments (packed)
    print(sum(args))

    # Unpack the tuple into individual arguments
    print(*args)


func1(1, 2, 3, 4)
```

## Data Pickle

```python
# Object serialization with pickle
# -----------------------------------------------------------------------------
# pickle serializes and deserializes Python objects so they can be saved and restored later.

import pickle
import sys


class Book(object):

    def __init__(self, title, author, price, year):
        self.title = title
        self.author = author
        self.price = price
        self.year = year


if __name__ == "__main__":

    # Create a book object
    book = Book(title='Python for Dummies', author='John Smith', price=25.0, year=2014)

    # Print the book object
    print(book.__dict__)

    # Serialize the book object
    serialized_book = pickle.dumps(book)

    # Print the size of the serialized object
    print('Size of the serialized object: {} bytes'.format(sys.getsizeof(serialized_book)))

    # Print the serialized object
    print(serialized_book)

    # Deserialize the book object
    deserialized_book = pickle.loads(serialized_book)

    # Print the book object
    print(deserialized_book.__dict__)
```

## Data Queue Fifo

```python
# FIFO queue with Queue
# -----------------------------------------------------------------------------
# queue.Queue provides a thread-safe FIFO structure for coordinating producer/consumer workloads.

from six.moves import queue


def empty_queue(customers):

    # Test the queue
    while True:
        try:
            item = customers.get(block=False)
            print("Get item: {}".format(item))

        except queue.Empty as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_queue(customers):

    items = ['Ivan', 'Dragan', 'Petkan', 'Stoyan']

    for item in items:
        customers.put(item)
        print("Add item: {}".format(item))

    print()


if __name__ == "__main__":

    # Create a FIFO queue
    d = queue.Queue()

    # Fill the queue
    fill_queue(d)

    # Empty the queue
    empty_queue(d)
```

## Data Queue Lifo

```python
# LIFO queue with LifoQueue
# -----------------------------------------------------------------------------
# LifoQueue behaves like a stack while remaining safe for use with multiple threads.

from six.moves import queue


def empty_queue(customers):

    # Test the queue
    while True:
        try:
            item = customers.get(block=False)
            print("Get item: {}".format(item))

        except queue.Empty as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_queue(customers):

    items = ['Ivan', 'Dragan', 'Petkan', 'Stoyan']

    for item in items:
        customers.put(item)
        print("Add item: {}".format(item))

    print()


if __name__ == "__main__":

    # Create a LIFO queue
    d = queue.LifoQueue()

    # Fill the queue
    fill_queue(d)

    # Empty the queue
    empty_queue(d)
```

## Data Queue Priority

```python
# Priority queues
# -----------------------------------------------------------------------------
# PriorityQueue orders tasks by priority, letting the smallest value be retrieved first.

from six.moves import queue


def empty_queue(customers):

    # Test the queue
    while True:
        try:
            priority, item = customers.get(block=False)
            print("Get {:8} : priority {:5}".format(item, priority))

        except queue.Empty as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_queue(customers):

    priorities = [3, 1, 2, 4]
    items = ['Ivan', 'Dragan', 'Petkan', 'Stoyan']

    for priority, item in zip(priorities, items):
        priority = int(priority)
        customers.put((priority, item))
        print("Add {:8} : priority {:5}".format(item, priority))

    print()


if __name__ == "__main__":

    # Create a FIFO queue
    d = queue.PriorityQueue()

    # Fill the queue
    fill_queue(d)

    # Empty the queue
    empty_queue(d)
```

## Data Reducing

```python
# Aggregating with reduce()
# -----------------------------------------------------------------------------
# reduce() repeatedly applies a function to items, collapsing them into a single result.

from functools import reduce

def total(x, y):
    return x + y


# Sample data
sample = [1, 1, 1]

# Map using a mapping function (first) and an iterable (second)
value = reduce(total, sample)
print(value)

# Map using a lambda function (first) and an iterable (second)
iterator = reduce(lambda x, y: x + y, sample)
print(value)
```

## Data Reversing

```python
# Reverse iteration
# -----------------------------------------------------------------------------
# The reversed() built-in returns an iterator that yields items from the end to the start.

# Sample data
sample_1 = [1, 2, 5, 4, 3]
sample_2 = {1: 'a', 2: 'b', 5: 'd', 4: 'c', 3: 'e'}

# Reverse a list
iterator = reversed(sample_1)
print(list(iterator))

# Reverse a dictionary
iterator = reversed(sample_2.items())
print(list(iterator))
```

## Data Sorting

```python
# Sorting with sorted()
# -----------------------------------------------------------------------------
# sorted() creates a new sorted list from any iterable, optionally using a key function.

class Book(object):

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return "Book({title}, {author}, {year})".format(
            title=self.title, author=self.author, year=self.year)


# List of books
books = [
    Book('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
    Book('To Kill a Mockingbird', 'Harper Lee', 1960),
    Book('1984', 'George Orwell', 1949),
    Book('Brave New World', 'Aldous Huxley', 1932),
    Book('The Catcher in the Rye', 'J.D. Salinger', 1951),
]

# Sort the list of dictionaries based on the 'year' key in each dictionary
sorted_books = sorted(books, key=lambda book: book.year)

# Print the sorted list
for b in sorted_books:
    print(b)
```

## Data Struct

```python
# Working with struct
# -----------------------------------------------------------------------------
# The struct module packs and unpacks binary data to interact with C-style structs.

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
    serialized = struct.pack('>32s 32s f i',
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
    title, author, price, year = struct.unpack('32s 32s f i', serialized)
    print(title.decode('utf-8').strip('\x00'))
    print(author.decode('utf-8').strip('\x00'))
    print(price)
    print(year)
```

## Data Struct With Buffer

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

## Data Unpacking

```python
# Argument unpacking
# -----------------------------------------------------------------------------
# Unpacking with * and ** lets you pass iterables or mappings as arguments in a clean syntax.

# A list of arguments
pos_args = [1, 2, 3, 4]
keyword_args = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# A sample function that takes 4 arguments
# and prints the,
def func1(a, b, c, d):
    print(a, b, c, d)


# Variable number of arguments
def func2(a, b, c, d, *args):
    print(a + b + c + d + sum(args))


# Variable number of keyword arguments
def func3(**kwargs):
    print(kwargs['a'] + kwargs['b'] + kwargs['c'] + kwargs['d'])


func1(*pos_args)
func2(*pos_args)
func3(**keyword_args)

test = "PYTHON"
unpacked = [*test]
print(unpacked)
```

## Data Zipping

```python
# Pairing items with zip()
# -----------------------------------------------------------------------------
# zip() pairs elements from multiple iterables so you can iterate over them in lockstep.

# Sample data
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# Zip two lists
zipped = zip(numbers, letters)
zipped_list = list(zipped)
print(zipped_list)

# Unzip into two lists
unzipped = zip(*zipped_list)
numbers, letters = map(list, unzipped)
print(numbers)
print(letters)
```

## Unpack Dict

```python
# Dictionary unpacking
# -----------------------------------------------------------------------------
# The * operator can expand a mapping's items into function arguments or into new dictionaries.
"""
https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators
"""

test = {"a": 1, "b": 2, "c": 3}
print(test)

# Unpack dictionary
print(*test)
print(*test.keys())
print(*test.values())
print(*test.items())

# Unpack first element and then the rest
a, *b = test.items()
print(a, b)

# Merge two lists
first = {"A": 1, "B": 2}
second = {"C": 3, "D": 4}
merged = {**first, **second}
print(merged)
```

## Unpack List

```python
# List unpacking
# -----------------------------------------------------------------------------
# Using * with a list expands its items when calling a function.
"""
https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators
"""

test = [1, 2, 3]
print(test)

# Unpack list and print uses elements as arguments
print(*test)

# Unpack first element and then the rest
a, *b = test
print(a, b)

# Merge two lists
first = [1, 2, 3]
second = [4, 5, 6]
merged = [*first, *second]
print(merged)
```

## Unpack Snippets

```python
# Unpacking snippets
# -----------------------------------------------------------------------------
# These small examples show how the * operator can gather or scatter items from sequences.
test_string = "PYTHON"
test_list = [1, 2, 3, 4]
test_dict = {"A": 1, "B": 2}

# Unpack string
*test, = test_string
print(test)

# Unpack list
*test, = test_list
print(test)

# Unpack dictionary items
*test, = test_dict.items()
print(test)

# Copy dictionary
test = {**test_dict}
print(test)
print(test is test_dict)
```
