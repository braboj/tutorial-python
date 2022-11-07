from abc import ABCMeta, abstractmethod
from six import with_metaclass


class DeviceInterface(with_metaclass(ABCMeta)):
    """ Example interfaces """

    def __init__(self):
        self._bar = "bar"

    @abstractmethod
    def foo(self):
        pass


class Samsung(DeviceInterface):
    """ Samsung MUST implement the method foo() from DeviceInterface"""

    def foo(self):
        print('foo')


test = Samsung()
test.foo()