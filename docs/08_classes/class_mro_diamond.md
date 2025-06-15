# class_mro_diamond

```python
# Mro (method resolution order) - diamond problem
# --------------------------------------------------------------------------------
# A diamond inheritance pattern occurs when two classes share a common base
# class. The method resolution order ensures that the base is initialized only
# once. The classes here are organized so that each path to the base is
# considered without duplication.

class A(object):
    @staticmethod
    def process():
        print("A.process()")


class B(A):
    @staticmethod
    def process():
        print("B.process()")


class C(A):
    @staticmethod
    def process():
        print("C.process()")


class D(B, C):
    pass


d = D()
print(D.mro())
d.process()
```
