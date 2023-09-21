class TestClass(object):
    a = 1

    def __init__(self):
        self.b = 2


# Test class attribute
test = getattr(TestClass, "a", 0xFF)
print(test)

test = getattr(TestClass, "c", 0xFF)
print(test)

try:
    test = getattr(TestClass(), "c")
    print(test)
except AttributeError as e:
    print(e)

# Test instance attribute
test = getattr(TestClass(), "b", 0xFF)
print(test)

test = getattr(TestClass(), "c", 0xFF)
print(test)

try:
    test = getattr(TestClass(), "c")
    print(test)
except AttributeError as e:
    print(e)


