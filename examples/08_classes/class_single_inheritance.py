# Example: Multilevel inheritance

class A(object):

    @staticmethod
    def process():
        print("Root is processing... ")


class B(A):
    pass


class C(B):
    pass


# The method process is searched for until the first class having the method is found (here A)
test = C()
test.process()
