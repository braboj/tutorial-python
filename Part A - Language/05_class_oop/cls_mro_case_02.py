class A(object):
    @staticmethod
    def process():
        print("A.process()")


class B(object):
    @staticmethod
    def method():
        print("B.process()")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
d.process()
print(D.mro())  # print MRO for class C
