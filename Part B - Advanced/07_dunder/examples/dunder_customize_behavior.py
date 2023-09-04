# Example: Dunder methods for customizing object behavior

class TestClass(object):

    def __init__(self):
        print("I'm initialized!")
        self.name = "DunderClass"

    def __new__(cls, *args, **kwargs):
        print("I'm created!")
        return super(TestClass, cls).__new__(cls)

    def __call__(self, *args, **kwargs):
        print("I'm called! My name is {}".format(self.name))

    def __del__(self):
        print("I'm deleted!")


# Create and initialize an instance of DunderClass
test = TestClass()

# Call the instance
test()

# Delete the instance
del test
