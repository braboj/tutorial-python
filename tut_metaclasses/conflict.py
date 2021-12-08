class MetaClassA(type):
    pass


class MetaClassB(type):
    pass


class A(object, metaclass=MetaClassA):
    pass


class B(object, metaclass=MetaClassB):
    pass


try:
    class C1(A, B):
        pass

except Exception as e:
    print(e)


class MetaClassC(MetaClassA, MetaClassB):
    pass


class C2(A, B, metaclass=MetaClassC):
    pass

