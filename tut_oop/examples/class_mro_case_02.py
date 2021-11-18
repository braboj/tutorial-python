class A(object):
    def process(self):
        print("A.process()")


class B(object):
    def method(self):
        print("B.process()")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
d.process()
print(D.mro())   # print MRO for class C