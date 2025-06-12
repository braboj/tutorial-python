# Mro (method resolution order) - diamond problem
# --------------------------------------------------------------------------------
# Demonstrates mro (method resolution order) - diamond problem.

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
