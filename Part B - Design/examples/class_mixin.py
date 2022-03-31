"""
Mixins are an alternative class design pattern that avoids both single-inheritance class fragmentation and
multiple-inheritance diamond dependencies.

https://www.residentmar.io/2019/07/07/python-mixins.html

"""

class Base(object):
    def __init__(self, a):
        self.a = a

    def this(self):
        pass

    def that(self):
        pass


class FirstMixin(object):

    @staticmethod
    def first_feature():
        print("First feature")


class SecondMixin(object):

    @staticmethod
    def second_feature():
        print("Second feature")


class Specific1(Base, FirstMixin):
    def __init__(self, a, b):
        super(Specific1, self).__init__(a)
        self.b = b


class Specific2(Base, FirstMixin, SecondMixin):
    def __init__(self, a, c):
        super(Specific2, self).__init__(a)
        self.c = c


a = Specific1(1, 2)
a.first_feature()

b = Specific2(1, 2)
b.first_feature()
b.second_feature()