
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
