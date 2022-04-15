from __future__ import annotations


class Channel_V2(object):

    @staticmethod
    def configure():
        print('Configuration method of the new device class!')


class Channel_V1(object):

    @staticmethod
    def applyConfig():
        print('Configuration method of the old device class!')


class Adapter(Channel_V1):

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def applyConfig(self):
        self.adaptee.configure()


def host_app(service):
    service.applyConfig()


if __name__ == "__main__":

    # Original code using the old service
    host_app(service=Channel_V1())

    # Use adapter for the new service adapted to the old interface
    new_device = Channel_V2()
    host_app(service=Adapter(new_device))