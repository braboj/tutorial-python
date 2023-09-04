# Two-step metaclass creation in Python 3.x
from six import with_metaclass


class SimpleMeta1(type):
    def __init__(cls, name, bases, namespace):
        super(SimpleMeta1, cls).__init__(name, bases, namespace)

        # Print the methods and attributes found at the parsing stage
        print(name, bases, namespace)

        # Create a method called uses_metaclass returning a simple string object
        cls.uses_metaclass = lambda self: 'Added by the meta-class'


class Simple1(object, with_metaclass(SimpleMeta1)):

    # Add a instance method to the namespace
    def foo(self):
        pass

    # Add a static function to the namespace
    @staticmethod
    def bar():
        pass


# Create the class
simple = Simple1()

# Expect 3 methods after the meta-class was executed
print([m for m in dir(simple) if not m.startswith('__')])

# Execute the method added by the meta-class
print(simple.uses_metaclass())
