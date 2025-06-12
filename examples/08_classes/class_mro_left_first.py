# Mro (method resolution order) - left first
# --------------------------------------------------------------------------------
# Demonstrates mro (method resolution order) - left first.

class A(object):

    @staticmethod
    def process():
        print('A.process()')


class B(object):
    @staticmethod
    def process():
        print('B.process()')


class C(A, B):
    pass


class D(B, A):
    pass


# The method process is searched for until the first class having the method is found (here A)
test = C()
print(C.mro())
test.process()

# The method process is searched for until the first class having the method is found (here B)
test = D()
print(D.mro())
test.process()
