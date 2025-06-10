"""
The statement self.<variable> may refer to two things at different times. When no instance
variable exists for a name, Python will look up the variable in the class. So the value retrieved
for self.<variable> will be the class variable.

But when setting an attribute via self, Python will always set an instance variable. So now
self.<variable> is a new instance variable whose value is equal to the class variable + 1. This
attribute shadows the class attribute, which you can no longer access via self but only via the
class.
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
