class TestClass(object):
    a = 1


test = hasattr(TestClass, "a")
print(test)

test = hasattr(TestClass, "b")
print(test)