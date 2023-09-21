"""
https://pymotw.com/3/weakref/

Proxies
It is sometimes more convenient to use a proxy, rather than a weak reference. Proxies can be used as though they
were the original object, and do not need to be called before the object is accessible. As a consequence,
they can be passed to a library that does not know it is receiving a reference instead of the real object.

If the proxy is accessed after the referent object is removed, a ReferenceError exception is raised.

"""


import weakref


class ExpensiveObject(object):

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('(Deleting {})'.format(self))


obj = ExpensiveObject('My Object')
r = weakref.ref(obj)
p = weakref.proxy(obj)

print('via obj:', obj.name)
print('via ref:', r().name)
print('via proxy:', p.name)
del obj
print('via proxy:', p.name)