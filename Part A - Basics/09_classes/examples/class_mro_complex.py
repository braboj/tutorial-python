# Example: MRO (Method Resolution Order) - Combined bottom first and left first

class A(object):
    @staticmethod
    def process():
        print("A.process()")


class B(object):
    @staticmethod
    def process():
        print("B.process()")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
print(D.mro())
d.process()
