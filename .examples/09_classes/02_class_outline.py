# Class structure outline
# --------------------------------------------------------------------------------
# This file outlines common elements found in many classes such as attributes,
# static methods and constructors. Organizing these pieces consistently makes
# new classes easier to understand and maintain.
#
# The internal state of a class is defined by its attributes, which can be
# class variables (shared across all instances) or instance variables (unique
# to each instance). Methods can be categorized as instance methods (which
# operate on instance variables), class methods (which operate on class
# variables), or static methods (which do not operate on either).

class ClassStructure(object):
    '""Class definition ....""'

    # Class attributes
    class_var = "Foo"

    def __new__(cls, *args, **kwargs):
        """This method is called to create a new instance of the class."""
        print("This is the constructor method")
        return object.__new__(cls)

    def __init__(self):
        """This method is called to initialize the instance after it is created."""
        print("This is the initialization method")
        self.inst_var = "John"

    def instance_method(self):
        """This method has access to both the class and instance variables."""
        print(self.class_var, self.inst_var)

    @classmethod
    def class_method(cls):
        """This method can access class variables but not instance variables."""
        print(cls.class_var)

    @staticmethod
    def static_method():
        """This method does not have access to the class or instance variables."""
        print(ClassStructure.class_var)
