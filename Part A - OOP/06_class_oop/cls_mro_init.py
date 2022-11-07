"""
Method resolution order (MRO)

In Python, the MRO is from bottom to top and left to right. This means that, first, the method is searched in the
class of the object. If it is not found, it is searched in the immediate super class. In the case of multiple super
classes, it is searched left to right, in the order by which was declared by the developer.  When there is a
super class before subclass then it must be removed from that position in MRO.

https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
https://www.educative.io/edpresso/what-is-mro-in-python
http://www.srikanthtechnologies.com/blog/python/mro.aspx
"""
##################################################################################################
class A(object):

    def __init__(self, a):
        self.a = a

    def test(self):
        print(self.a)


##################################################################################################
class B(object):

    def __init__(self, b):
        self.b = b

    def test(self):
        print(self.b)


##################################################################################################
class AB(A, B):

    # MRO is AB -> A

    def __init__(self):
        super(AB, self).__init__()


##################################################################################################
class BA(B, A):

    # MRO is BA -> B

    def __init__(self):
        super(BA, self).__init__()

##################################################################################################
