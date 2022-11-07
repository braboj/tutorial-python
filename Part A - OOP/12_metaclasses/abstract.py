from abc import ABCMeta, abstractmethod
from six import with_metaclass


class DeviceAbc(with_metaclass(ABCMeta)):

    @abstractmethod
    def foo(self):
        pass


class Device(DeviceAbc):
    pass


a = Device()
