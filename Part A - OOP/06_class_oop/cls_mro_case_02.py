"""
In Python, the MRO is from bottom to top and left to right. This means that, first, the method is searched in the
class of the object. If it is not found, it is searched in the immediate super class. In the case of multiple super
classes, it is searched left to right, in the order by which was declared by the developer.  When there is a
super class before subclass then it must be removed from that position in MRO.

https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
https://www.educative.io/edpresso/what-is-mro-in-python
http://www.srikanthtechnologies.com/blog/python/mro.aspx
"""

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
