"""
https://pymotw.com/3/weakref/

For more robust management of resources when weak references are cleaned up, use finalize to associate callbacks
with objects. A finalize instance is retained until the attached object is deleted, even if the application does
not retain a reference to the finalizer.

The arguments to finalize are the object to track, a callable to invoke when the object is garbage collected,
and any positional or named arguments to pass to the callable.

The finalize instance has a writable propertly atexit to control whether the callback is invoked as a program is
exiting, if it hasn’t already been called.

The default is to invoke the callback. Setting atexit to false disables that behavior.

Warning:
1. Giving the finalize instance a reference to the object it tracks causes a reference to be retained, so the object
is never garbage collected.
2. Using a bound method of a tracked object as the callable can also prevent an object from being finalized properly.

"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Finalizing objects by using callbacks with arguments
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
weakref.finalize(obj, on_finalize, 'extra argument')

del obj
