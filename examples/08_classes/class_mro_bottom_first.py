# Example: MRO (Method Resolution Order) - Bottom first

class A(object):

    @staticmethod
    def process():
        print('A.process()')


class B(object):
    @staticmethod
    def process():
        print('B.process()')


class C(A, B):

    @staticmethod
    def process():
        print('C.process()')


obj = C()
obj.process()
print(C.mro())
