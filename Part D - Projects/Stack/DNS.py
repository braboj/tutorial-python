from Device import *


class PacketTemplate(object):
    """ Template class"""

    context = None

    def init(self, context):
        self.context = context

    @classmethod
    def configure(cls):
        pass

    @classmethod
    def deconfigure(cls):
        pass


class PacketApiV2(PacketTemplate):
    name = "DNS V2"

    @classmethod
    def set_config_packet(cls):
        print("Configure {0}".format(cls.name))

    @classmethod
    def configure(cls):
        cls.set_config_packet()


class PacketApiV3(PacketTemplate):
    name = "DNS V3"

    @classmethod
    def set_config_packet(cls):
        print("Configure {0}".format(cls.name))

    @classmethod
    def configure(cls):
        cls.set_config_packet()


class DeviceNetSlave(CommunicationDevice):

    __api__ = PacketApiV3()

    comclass = 2
    protoclass = 8

    def __init__(self, channel):
        super(DeviceNetSlave, self).__init__(channel)

        # Overwrite methods
        for attr_name in dir(self.__api__):
            if "__" not in attr_name:
                setattr(self, attr_name, getattr(self.__api__, attr_name))

    @classmethod
    def api(cls, api):
        cls.__api__ = api


if __name__ == "__main__":

    # Mock the framework behavior
    devcls = Device.get_device_class_from_channel(channel=None)

    # Call the named constructor with the packet api as parameter
    devcls.api(PacketApiV2)

    # Initialize the device class
    dev = devcls(channel=Channel())

    # Configure the device
    dev.configure()
