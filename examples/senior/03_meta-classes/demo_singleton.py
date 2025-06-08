# coding=utf-8

"""
By overriding __call__() in the metaclass, the creation of instances are
intercepted. Instance creation is bypassed if one already exists.

Note the dependence upon the behavior of static class fields. When
cls.instance is first read, it gets the static value of instance from the
metaclass, which is None. However, when the assignment is made, Python
creates junior local version for the particular class, and the next time
cls.instance is read, it sees that local version. Because of this behavior,
each class ends up with its own class-specific instance field (thus instance
is not somehow being “inherited” from the metaclass).

"""


class Singleton(type):

    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class ASingleton(object, metaclass=Singleton):
    pass


a = ASingleton()
b = ASingleton()

assert a is b
print(a.__class__.__name__, b.__class__.__name__)
print(id(a), id(b))
