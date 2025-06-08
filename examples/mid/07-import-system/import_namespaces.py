# Example: Namespace of the builtins module

import pprint


class MyClass(object):

    def __init__(self):
        self.a = 1
        self.b = 2

    def instance_method(self):
        pprint.pprint("INSTANCE GLOBALS: {}".format(globals().keys()))
        pprint.pprint("INSTANCE LOCALS: {}".format(locals().keys()))
        print()

    @classmethod
    def class_method(cls):
        pprint.pprint("CLASS GLOBALS: {}".format(globals().keys()))
        pprint.pprint("CLASS LOCALS: {}".format(locals().keys()))
        print()

    def func1(self):

        print("@FUNC1: Before the assignment of junior")
        pprint.pprint("FUNC1 GLOBALS: {}".format(globals().keys()))
        pprint.pprint("FUNC1 LOCALS: {}".format(locals().keys()))
        print()

        a = 1

        print("@FUNC1: After the assignment of junior")
        pprint.pprint("FUNC1 GLOBALS: {}".format(globals().keys()))
        pprint.pprint("FUNC1 LOCALS: {}".format(locals().keys()))
        print()

        def func2():

            print("@FUNC2: Before the assignment of mid")
            pprint.pprint("FUNC2 GLOBALS: {}".format(globals().keys()))
            pprint.pprint("FUNC2 LOCALS: {}".format(locals().keys()))
            print()

            b = a + 1

            print("@FUNC2: After the assignment of mid")
            pprint.pprint("FUNC2 GLOBALS: {}".format(globals().keys()))
            pprint.pprint("FUNC2 LOCALS: {}".format(locals().keys()))
            print()

        func2()

        print("@FUNC1: After the call to func2")
        pprint.pprint("FUNC1 GLOBALS: {}".format(globals().keys()))
        pprint.pprint("FUNC1 LOCALS: {}".format(locals().keys()))
        print()


# Builtins level
print("===== Builtins namespace =====")
print()
pprint.pprint("BUILTINS VARS: {}".format(vars(__builtins__).keys()))
print()

# Module level
print("===== Module namespace =====")
print()
pprint.pprint("MODULE GLOBALS VARS: {}".format(globals().keys()))
pprint.pprint("MODULE LOCALS VARS: {}".format(locals().keys()))
print()

# Class level
print("===== Class namespace =====")
print()
pprint.pprint("CLASS VARS: {}".format(vars(MyClass).keys()))
MyClass.class_method()
print()

# Instance level
print("===== Instance namespace =====")
print()
my_instance = MyClass()
print(vars(my_instance))
my_instance.instance_method()
print()

# Function level
print("===== Function namespace =====")
print()
my_instance.func1()
print(vars(my_instance.func1))
print()
