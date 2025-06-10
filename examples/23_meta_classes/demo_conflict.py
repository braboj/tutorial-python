from six import with_metaclass


class MetaClassA(type):
    pass


class MetaClassB(type):
    pass


class A(object, with_metaclass(MetaClassA)):
    pass


class B(object, with_metaclass(MetaClassB)):
    pass


try:
    class C1(A, B):
        pass

except Exception as e:
    print(e)


class MetaClassC(MetaClassA, MetaClassB):
    pass


class C2(A, B, with_metaclass(MetaClassC)):
    pass

