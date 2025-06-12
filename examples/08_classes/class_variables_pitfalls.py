# Class Variables Pitfalls
# --------------------------------------------------------------------------------
# Demonstrates class variables pitfalls.
"""Class vs. Instance Variables
--------------------------------
Class variables are shared by all instances, while instance variables belong
to each object. Assigning to ``self.variable`` creates an instance attribute.
If a class attribute with the same name exists, the instance attribute hides it
and later reads through ``self`` return the instance value. Mixing them can be
confusing because updates seem to apply only to some objects.

When you read ``self.value`` and ``value`` is not defined on the instance,
Python falls back to the class attribute:

    class A:
        value = 1

    obj = A()
    print(obj.value)  # 1 from the class

Any assignment using ``self`` stores a value on the instance:

    obj.value = 2
    print(A.value)   # 1
    print(obj.value) # 2

Here ``obj.value`` now shadows ``A.value``. To access the class attribute
explicitly you must use ``A.value``.
"""


class TestOp(object):

    immutable = 1
    mutable = [1, ]


class Test(TestOp):

    def __init__(self):
        super(Test, self).__init__()

    def test_immutable(self):

        print("#" * 80)
        print("Testing immutable class variable")
        print("#" * 80)

        # self references to the class variable
        print("")
        print("Read value through class name and then self...")

        print("CLS  => {0}:{1}".format(id(TestOp.immutable), TestOp.immutable))
        print("SELF => {0}:{1}".format(id(self.immutable), self.immutable))

        # self creates and references an instance variable (shadows the class variable)
        print("")
        print("Change immutable type using self...")

        self.immutable = 2
        print("CLS  => {0}:{1}".format(id(TestOp.immutable), TestOp.immutable))
        print("SELF => {0}:{1}".format(id(self.immutable), self.immutable))

        # Changing the value of immutable class variable will create a new object
        print("")
        print("Change the value of the class immutable variable...")

        TestOp.immutable = 3
        print("CLS  => {0}:{1}".format(id(TestOp.immutable), TestOp.immutable))
        print("SELF => {0}:{1}".format(id(self.immutable), self.immutable))

        print("")

    def test_mutable(self):
        print("#" * 80)
        print("Testing mutable class variable")
        print("#" * 80)

        # self references to the class variable
        print("")
        print("Read value through class name and then self...")

        print("CLS  => {0}:{1}".format(id(TestOp.mutable), TestOp.mutable))
        print("SELF => {0}:{1}".format(id(self.mutable), self.mutable))

        # self creates and references an instance variable (shadows the class variable)
        print("")
        print("Change mutable type using self...")

        self.mutable.append(2)
        print("CLS  => {0}:{1}".format(id(TestOp.mutable), TestOp.mutable))
        print("SELF => {0}:{1}".format(id(self.mutable), self.mutable))

        # self
        print("")
        print("Change the value of the class mutable variable...")

        TestOp.mutable.append(3)
        print("CLS  => {0}:{1}".format(id(TestOp.mutable), TestOp.mutable))
        print("SELF => {0}:{1}".format(id(self.mutable), self.mutable))

        print("")


if __name__ == "__main__":

    test = Test()

    test.test_mutable()
    print("Final value of immutable class variable is {0}:{1}\n".format(id(Test.immutable), Test.immutable))

    test.test_immutable()
    print("Final value of mutable class variable is {0}:{1}\n".format(id(Test.mutable), Test.mutable))
