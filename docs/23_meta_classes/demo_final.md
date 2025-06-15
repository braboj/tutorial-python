# demo_final

```python
from six import with_metaclass


class Final(type):
    def __init__(cls, name, bases, namespace):
        super(Final, cls).__init__(name, bases, namespace)

        for klass in bases:
            if isinstance(klass, Final):
                raise TypeError(str(klass.__name__) + " is final")


class A(object, with_metaclass(Final)):
    A = 1

    def a(self):
        pass


class B(A):
    B = 1

    def b(self):
        pass


a = A()
print(a)

b = B()
print(b)
```
