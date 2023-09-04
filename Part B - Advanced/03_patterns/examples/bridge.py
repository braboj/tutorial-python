# Example: Bridge Pattern

from __future__ import annotations
from abc import ABC, abstractmethod


class ChannelAbc(ABC):
    # Interface for concrete implementation

    @abstractmethod
    def set_config(self):
        raise NotImplementedError

    @staticmethod
    def channel_init():
        print("Channel init ...")


class OmbChannel(ChannelAbc):
    " Concrete implementation "

    def set_config(self):
        print("Sending OMB configuration packet ...")


class DnsChannel(ChannelAbc):
    " Concrete implementation "

    def set_config(self):
        print("Sending DNS configuration packet ...")


class DeviceAbc(ABC):
    # Bridge abstraction

    @abstractmethod
    def configure(self):
        raise NotImplementedError


class Device(DeviceAbc):
    # Concrete bridge implementation

    def __init__(self, channel: ChannelAbc):
        self.channel = channel

    def configure(self):
        self.channel.set_config()
        self.channel.channel_init()


def HostApp(device: Device):
    return device.configure()


if __name__ == "__main__":

    # The client code
    channel = OmbChannel()
    HostApp(device=Device(channel))