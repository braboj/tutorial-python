# https://pymotw.com/3/weakref/

##############################################################################
# CLASSIC REFERENCING
##############################################################################
import ctypes


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


# Object instantiation
print("Create expensive object")
obj = ExpensiveObject()
addr = id(obj)

# Expensive referencing
print("Reference expensive object multiple times")
ref = []
for i in range(10):
    ref.append(obj)
    print(obj)

# Print reference count
ref_count = ctypes.c_long.from_address(addr).value
print("Reference count is {0}".format(ref_count))

# Delete strong reference
print('deleting obj')
del obj

# Print reference count
ref_count = ctypes.c_long.from_address(addr).value
print("Reference count is {0}".format(ref_count))
