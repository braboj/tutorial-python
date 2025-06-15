# class_mro_bottom_first

```python
# Mro (method resolution order) - bottom first
# --------------------------------------------------------------------------------
# In this layout the interpreter begins searching for methods in the most
# derived class and moves upward through the hierarchy. The arrangement helps
# clarify how attribute lookup progresses when multiple parents define the same
# name.

class A(object):

    @staticmethod
    def process():
        print('A.process()')


class B(object):
    @staticmethod
    def process():
        print('B.process()')


class C(A, B):

    @staticmethod
    def process():
        print('C.process()')


obj = C()
obj.process()
print(C.mro())
```
