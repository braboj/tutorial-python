from tut_framework.components.Testcase import Testcase
import tut_framework.components.Logger as Logger


class TC1(Testcase):

    _device_dut_ = object

    def __init__(self):
        super(TC1, self).__init__()

    def test(self):
        self.log.info("Hello from object {0}!".format(id(self)))


test = TC1

if __name__ == "__main__":
    test().test()