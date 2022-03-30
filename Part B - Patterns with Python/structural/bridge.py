from __future__ import annotations
from abc import ABC, abstractmethod


class Channel(ABC):
    "Implementation interface"

    @abstractmethod
    def set_config(self):
        raise NotImplementedError

    @staticmethod
    def channel_init():
        print(f"Channel init ...")


class OmbChannel(Channel):
    " Concrete implementation "

    def set_config(self):
        print(f"Sending OMB configuration packet ...")


class DnsChannel(Channel):
    " Concrete implementation "

    def set_config(self):
        print(f"Sending DNS configuration packet ...")


class Device(object):
    """ Abstraction """

    def __init__(self, implementation):

        self.i = implementation

    def configure(self):
        self.i.set_config()
        self.i.channel_init()


def HostApp(device: Device):
    return device.configure()


if __name__ == "__main__":

    # The client code
    channel = OmbChannel()
    device = Device(channel)
    HostApp(device=device)