from base import TestOp


class Test01(TestOp):
    def __init__(self):
        print(self.__class__.__name__)


class Test02(TestOp):
    def __init__(self):
        print(self.__class__.__name__)

