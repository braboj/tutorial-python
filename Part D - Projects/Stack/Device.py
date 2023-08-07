"""
Created on 22.02.2010

@author: andreasme
"""
from Registries import Registrar
import logging


class Channel(object):

    def __init__(self):
        self.name = 'Channel Name'


class DeviceRegistrar(Registrar):

    @classmethod
    def get_device_class_from_channel(cls, channel):
        """ Create a new device driver instance by merging different device handlers
             in a new class (if required) """

        log = logging.getLogger('DeviceRegistrar')

        ###########################################################################################
        # 1. Get base classes
        ###########################################################################################

        bases = set()
        for handler_cls in cls.list():

            handler_cls = handler_cls.getDeviceClass()

            # if this class subclasses any of our bases, drop them from the list
            for b in list(bases):
                if issubclass(handler_cls, b):
                    bases.remove(b)

            bases.add(handler_cls)

        print(tuple(bases))

        ###########################################################################################
        # 2. Sort base classes based on their level attribute
        ###########################################################################################

        # when multiple devide handlers fit, we create a new class subclassing all of them
        # in order of their level
        sorted_bases = tuple(sorted(bases, key=lambda x: x.level(), reverse=True))
        print(sorted_bases)

        if len(sorted_bases) == 0:
            dev_cls = None

        elif all(issubclass(b, CompanionDevice) for b in sorted_bases):
            # all bases are companion only device drivers
            dev_cls = None

        elif len(sorted_bases) > 1:
            # get names of bases classes and remove some common names
            names = list(b.__name__ for b in sorted_bases)

            # strip off additional names as long as at least one
            # name is left over
            hide_names = [
                'ConfigurationParent',
                'SlaveDevice',
                'MasterDevice'
            ]

            for x in hide_names:
                if len(names) > 1:
                    names = list(n for n in names if n != x)
                else:
                    break

            mclasses = set(x.__metaclass__ for x in sorted_bases)
            mbases = [DerivedDeviceRegistrar]

            # Merge metaclasses if required
            for x in mclasses:
                for y in mbases[:]:
                    # check is already in list, then discard
                    if issubclass(y, x):
                        break

                    # subclass available, we can drop it
                    if issubclass(x, y):
                        mbases.remove(y)
                else:
                    mbases.append(x)

            # define mnew metaclass if required
            if len(mbases) == 1:
                mcls = mbases[0]
            else:
                mcls = type('_'.join(x.__name__ for x in mbases), tuple(mbases), {})

            dev_cls = mcls('_'.join(names), sorted_bases, {})

        else:
            dev_cls = sorted_bases[0]

        return dev_cls


class DerivedDeviceRegistrar(DeviceRegistrar):
    @classmethod
    def register(cls, device_cls):
        return


class Device(object):
    __metaclass__ = DeviceRegistrar

    # this tuple defines the priority of the device when
    # checking for the device under test
    # dut_priority[0]: 0/auto priority, 1/priority by command line
    # dut_priority[1]: priority by firmware type
    # dut_priority[2]: priority by cifx/channel channel

    dut_priority = (0, 0, 0)

    @classmethod
    def level(cls):
        return -99

    def prepare(self, *args, **kwargs):
        pass

    def cleanup(self, *args, **kwargs):
        pass

    @classmethod
    def getDeviceClass(cls):
        return cls


class CompanionDevice(Device):
    """ Use for device driver which can not run standalone """
    pass


class CommunicationDevice(Device):
    name = "Generic Cifx Communication Channel"
    comclass = None
    protoclass = None

    dut_priority = (0, 1, 0)

    def __init__(self, channel):
        super(CommunicationDevice, self).__init__()
        self.channel = channel
        self.name = "{cls.__name__}({channel.name})".format(cls=self.__class__, channel=channel)

    def __str__(self):
        return self.name

    @classmethod
    def level(cls):
        """
        Returns the level of the specific device adapter. This is used to
        assign the bets fitting device adapter
        """
        level = 0

        try:
            iter(cls.comclass)
            # multiple comunication classes defined
            level -= 1
        except TypeError:
            # single communication class defined
            pass
        except AttributeError:
            # no comclass attribute defined
            level -= 2

        try:
            iter(cls.protoclass)
            # multiple protocol class defined
            level -= 10
        except TypeError:
            # single protocol class defined
            pass
        except AttributeError:
            # no protocol class attribute defined
            level -= 20

        return level


class DeviceNetSlave(CommunicationDevice):
    name = "DNS V1"
    comclass = 2
    protoclass = 8

    @staticmethod
    def configure():
        print("V1")


if __name__ == "__main__":
    devcls = Device.get_device_class_from_channel(channel=None)
    dev = devcls(channel=Channel())
    dev.configure()