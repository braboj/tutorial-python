
# Create root class (use args and kwargs in case subclass have more parameters than the parent)
class Root(object):

    def __init__(self, param1, *args, **kwargs):
        self.param1 = param1


# Create subclass (use args and kwargs in case subclass have more parameters than the parent)
class A(Root):

    def __init__(self, param1=1, param2=2, *args, **kwargs):
        super(A, self).__init__(param1=param1)
        self.param2 = param2


# Create subclass (use args and kwargs in case subclass have more parameters than the parent)
class B(A):

    def __init__(self, *args, **kwargs):
        super(B, self).__init__(*args, **kwargs)
        self.param3 = kwargs["param3"]


if __name__ == "__main__":

    root = Root(param1=1)
    print(vars(root))

    a = A(param1=10, param2=20)
    print(vars(a))

    b = B(param1=100, param2=200, param3=300)
    print(vars(b))
