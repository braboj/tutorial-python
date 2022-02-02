# import inspect
# import sys
# import socket
# from traceback import format_tb, print_stack

import os
import Logger
from Registries import Registrar


_framework_path = os.path.dirname(__file__)


class TestcaseRegistrar(Registrar):
    """ An Instance of this class is created whenever a testcase is defined. """

    def __init__(cls, name, bases, dct):
        cls.log = Logger.getLogger(cls.__class__.__name__)
        testcase = {}
        devices = {}
        optdevices = {}
        parameters = {}

        for attr, value in dct.items():
            if (not (attr.startswith('_') and attr.endswith('_'))) or attr.startswith('__') or attr.startswith(
                    "_" + name + '__'):
                continue

            c, sep, n = attr[1:-1].partition('_')

            if sep != '_':
                raise AttributeError('Unexpected field %s in testcase %s' % (attr, name))
            elif c == 'device':
                devices[n] = value
            elif c == 'optdevice':
                optdevices[n] = value
            elif c == 'param':
                parameters[n] = value
            elif c == 'testcase':
                testcase[n] = value
            else:
                raise AttributeError('Unexpected field %s in testcase %s' % (attr, name))

            delattr(cls, attr)

        cls.testcase = staticmethod(lambda: dict(testcase))
        cls.devices = staticmethod(lambda: dict(devices))
        cls.optdevices = staticmethod(lambda: dict(optdevices))
        cls.parameters = staticmethod(lambda: dict(parameters))

        super(TestcaseRegistrar, cls).__init__(name, bases, dct)
        cls.log.debug(cls.devices().items())


class Testcase(object):
    __metaclass__ = TestcaseRegistrar

    def __init__(self):
        self.log = Logger.getLogger("{self.__class__.__name__}".format(self=self))

        # create variables that hold the test results
        self.result = None
        self.testcase_exc_list = []
        self.misc_exc_list = []

        self.__dut = None
        self.result = False

    @property
    def dut(self):
        return self.__dut

    def prepare(self, **kwargs):
        pass

    def cleanup(self, **kwargs):
        pass

    def probe(self, **kwargs):
        pass

    def run(self, DeviceList):
        return self.result



