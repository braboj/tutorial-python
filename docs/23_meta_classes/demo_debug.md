# demo_debug

```python
# coding=utf-8

"""
__new__ is called for the creation of a new class, while __init__ is called
after the class is created, to perform additional initialization before the
class is handed to the caller.

The primary difference is that when overriding __new__() you can change
things like the ‘name’, ‘bases’ and ‘namespace’ arguments before you call
the super constructor and it will have an effect, but doing the same thing
in __init__() you won’t get any results from the constructor call.

"""

from collections import OrderedDict
import time


class DebugMeta(type):

    @classmethod
    def __prepare__(cls, name, bases):

        namespace = OrderedDict()
        namespace["owner"] = "Branimir Georgiev"
        print("Preparing namespace dictionary {0}".format(namespace))
        return namespace

    def __new__(mcs, name, bases, namespace):

        x = super(DebugMeta, mcs).__new__(mcs, name, bases, namespace)
        print("Creating new class {0}".format(x))
        x.timestamp = time.time()
        return x

    def __init__(cls, name, bases, namespace):

        print("Class initialization")
        super(DebugMeta, cls).__init__(name, bases, namespace)
        cls.access = "rw"

    def __call__(cls, *args, **kwargs):

        print("Class call")
        return super(DebugMeta, cls).__call__(*args, **kwargs)

    def __del__(self):
        print("Class deleted")


class Base(metaclass=DebugMeta):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)
        print("Instance initialization {0}".format(vars(self)))

    def __new__(cls, *args, **kwargs):
        x = super(Base, cls).__new__(cls, *args, **kwargs)
        print("Creating new instance {0}".format(x))
        return x

    def __call__(self, *args, **kwargs):
        print("Instance called args={0} and kwargs={1}".format(args, kwargs))

    def __del__(self):
        print("Instance deleted")

config = {"a":1, "b":2}
test = Base()
test(1, test=2)
```
