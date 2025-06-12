# Class structure
# --------------------------------------------------------------------------------
# Demonstrates class structure.

class ClassStructure(object):

    CLASS_VARIABLE = "Hi, I am "

    def __new__(cls, *args, **kwargs):
        print("This is the constructor method")
        return object.__new__(cls)

    def __init__(self):
        print("This is the initialization method")
        self.instance_variable = "John"

    @classmethod
    def class_method(cls):
        print("This is a class method, the class prefix is: {}".format(cls.class_variable))

    @staticmethod
    def static_method():
        print("This is a static method, the class prefix is: {}".format(ClassStructure.class_variable))

    def instance_method(self):
        print("This is an instance method, `{} {}`".format(self.class_variable, self.instance_variable))
