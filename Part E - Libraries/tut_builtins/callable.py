##############################################################################
# Integer is callable?
##############################################################################
test = 5
print("Integer callable? : {0}".format(callable(test)))


##############################################################################
# Function is callable?
##############################################################################
def test_func(x):
    print(x)


test = test_func
print("Function callable? : {0}".format(callable(test)))


##############################################################################
# Class is callable?
##############################################################################
class TestClass(object):
    def test_func(self, x):
        print(x)


test = TestClass
print("Class callable? : {0}".format(callable(test)))


##############################################################################
# Object is callable?
##############################################################################

# A: Without __call__
class TestClass(object):
    def test_func(self, x):
        print(x)


test = TestClass()
print("Instance callable? : {0}".format(callable(test)))


# B: With __call__
class TestClass(object):
    def __call__(self, *args, **kwargs):
        print("Class instance called")

    def test_func(self, x):
        print(x)


test = TestClass()
print("Instance with _call_ callable? : {0}".format(callable(test)))
test()
