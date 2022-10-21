class A(object):

    @staticmethod
    def process():
        print('A process()')


class B(object):
    pass


class C(A, B):
    pass


obj = C()
obj.process()
print(C.mro())   # print MRO for class C
