# Example: Multiple inheritance

class A(object):

    @staticmethod
    def process():
        print("Class A is processing... ")


class B(object):

    @staticmethod
    def process():
        print("Class B is processing... ")


class C(A, B):
    pass


class D(B, A):
    pass


# The method process is searched for until the first class having the method is found (here A)
test = C()
test.process()

# The method process is searched for until the first class having the method is found (here B)
test = D()
test.process()
