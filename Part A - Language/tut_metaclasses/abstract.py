import abc


class DeviceAbc(abc.ABC):

    @abc.abstractmethod
    def foo(self):
        pass


class Device(DeviceAbc):
    pass


a = Device()
