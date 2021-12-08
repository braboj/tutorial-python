"""
https://www.programiz.com/python-programming/methods/built-in/memoryview

Python Buffer Protocol
The buffer protocol provides a way to access the internal data of an object. This internal data is a memory array or
a buffer. The buffer protocol allows one object to expose its internal data (buffers) and the other to access those
buffers without intermediate copying. This protocol is only accessible to us at the C-API level and not using our
normal codebase. So, in order to expose the same protocol to the normal Python codebase, memory views are present.

What is a memory view?
A memory view is a safe way to expose the buffer protocol in Python. It allows you to access the internal buffers
of an object by creating a memory view object.

Why buffer protocol and memory views are important?
We need to remember that whenever we perform some action on an object (call a function of an object,
slice an array), Python needs to create a copy of the object. If we have large data to work with (eg. binary data
of an image), we would unnecessarily create copies of huge chunks of data, which serves almost no use. Using the
buffer protocol, we can give another object access to use/modify the large data without copying it. This makes the
program use less memory and increases the execution speed.

Syntax
memoryview(obj)

obj - object whose internal data is to be exposed. obj must support the buffer protocol

"""

# random bytearray
random_byte_array = bytearray(u'Хилшер', 'utf-8')
mv = memoryview(random_byte_array)

# access memory view's zeroth index
print(mv[0])

# create byte from memory view
print(bytes(mv[0:2]))

# create list from memory view
print(list(mv[0:3]))


