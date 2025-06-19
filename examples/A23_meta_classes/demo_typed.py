from six import with_metaclass


# Create metaclass
class MyMetaClass(type):
    def __init__(cls, name, bases, namespace):
        super(MyMetaClass, cls).__init__(name, bases, namespace)


# Create first custom class from metaclass
class A(object, with_metaclass(MyMetaClass)):
    A = 1

    def __init__(self, param=1):
        self.a = param

    @staticmethod
    def configure():
        print("A")


# Create second custom class from metaclass
class B(object, with_metaclass(MyMetaClass)):
    B = 2

    def __init__(self, param=1):
        self.b = param

    @staticmethod
    def configure():
        print("B")


# Show that order of super classes determines class behavior

# -> Inherits combined class attributes but instance attrib/methods from A
D = MyMetaClass('D', (A, B), {})
test = D()
print(vars(test))
test.configure()

# -> Inherits combined class attributes but instance attrib/methods from B
D = MyMetaClass('D', (B, A), {})
test = D()
print(vars(test))
test.configure()

# -> Solution when multiple inheritance problems (due to bad design, etc.)

# Recast class type
test = B(test)
pass
