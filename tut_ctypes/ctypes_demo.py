from ctypes import c_ubyte, windll

##################################################################################################
# Create a single ctype object and initialize
##################################################################################################
print("-" * 80)

# Create
a = c_ubyte(1)

# Usage
print(a)            # Print object
print(a.value)      # Read objects value

##################################################################################################
# Create an array of ctypes objects and initialize
# ctypes arrays implement __iter__ but are not iterators
##################################################################################################
print("-" * 80)

# Create
IO_TYPE = c_ubyte * 3
a = IO_TYPE(1, 2, 3)
b = (c_ubyte * 3)(1, 2, 3)
assert(type(a) == type(b))
print(type(a), type(b))

# Usage
i = iter(a)         # Get the iterator for the ctypes array
print(i)            # Print the iterator object
print(next(i))      # Iterate
print(tuple(a))     # Convert to another iterable type


##################################################################################################
#
##################################################################################################
from ctypes import *
print(cdll.msvcrt)
libc = cdll.msvcrt
pass