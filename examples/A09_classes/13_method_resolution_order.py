# MRO (Method Resolution Order) - bottom first
# ------------------------------------------------------------------------------
# The method resolution order (MRO) in Python is the order in which Python
# looks for methods in a class hierarchy. It is particularly important in
# multiple inheritance scenarios, where a class inherits from multiple parent
# classes.
#
# The MRO is determined by the C3 linearization algorithm, which ensures that
# the order of method resolution is consistent and respects the order of
# inheritance. The MRO can be viewed using the `mro()` method of a class.


# Example of MRO in Python (bottom up, left to right)
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


test = D()
print(D.mro())
# Output:
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
