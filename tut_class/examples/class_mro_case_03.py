class A(object):
    def process(self):
        print('A process()')


class B(A):
    pass


class C(A):
    def process(self):
        print('C process()')


class D(B,C):
    pass


obj = D()
obj.process()
print(D.mro())