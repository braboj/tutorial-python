# Mro (method resolution order) - combined bottom first and left first
# --------------------------------------------------------------------------------
# Python resolves method names by considering both the depth of the inheritance
# tree and the order in which bases are listed. This file sets up a hierarchy
# that makes the combined bottom-first and left-first rules apparent.

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
