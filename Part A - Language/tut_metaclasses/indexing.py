from six import with_metaclass


##############################################################################
# Metaclass definition
##############################################################################

class Indexer(type):
    def __init__(cls, name, bases, namespace):
        super(Indexer, cls).__init__(name, bases, namespace)

        if not hasattr(cls, "subclasses"):
            cls.subclasses = []

        if not hasattr(cls, "index"):
            cls.index = 0

        # Index only subclasses
        for b in bases:
            if isinstance(b, Indexer):
                cls.subclasses.append(1)

        cls.index = len(cls.subclasses)


##############################################################################
# First base class and subclasses
##############################################################################

class A(with_metaclass(Indexer)):
    pass


class A1(A):
    pass


class A2(A):
    pass


print(A.index, A1.index, A2.index)


##############################################################################
# Second base class and subclasses
##############################################################################

class B(with_metaclass(Indexer)):
    pass


class B1(B):
    pass


class B2(B):
    pass


print(B.index, B1.index, B2.index)
