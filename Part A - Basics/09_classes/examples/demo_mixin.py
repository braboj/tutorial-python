""" Mixin Design for Python 2 and 3

Mixins are an alternative class design pattern that avoids both single-inheritance class fragmentation and
multiple-inheritance diamond dependencies.

 - The constructor of the mixin class must only have *args and **kwargs as parameters
 - Each mixin class shall have a super call in its __init__ method forwarding *args and **kwargs
 - The mixin classes are a special form of multiple inheritance
 - The mixin class may have any instance attributes.

https://www.residentmar.io/2019/07/07/python-mixins.html
https://www.pythontutorial.net/python-oop/python-mixin/

"""


class A(object):
    def __init__(self):
        super(A, self).__init__()
        self.a = 'a'
        print('A')

    def a_method(self):
        print('{}_method'.format(self.a))


class B(object):
    def __init__(self):
        super(B, self).__init__()
        self.b = 'b'
        print('B')

    def b_method(self):
        print('{}_method'.format(self.b))


class C(A, B):
    def __init__(self, c='c'):
        super(C, self).__init__()
        self.c = c
        print('C')

    def c_method(self):
        print('{}_method'.format(self.c))


c = C()
print(c.a)
print(c.b)
print(c.c)
c.a_method()
c.b_method()
c.c_method()