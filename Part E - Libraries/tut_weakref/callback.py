"""
https://pymotw.com/3/weakref/

The ref constructor accepts an optional callback function that is invoked when the referenced object is the deleted
object. The callback receives the reference object as an argument after the reference is “dead” and no longer refers
to the original object. One use for this feature is to remove the weak reference object from a cache.
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reference callbacks when the weak reference is deleted
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())