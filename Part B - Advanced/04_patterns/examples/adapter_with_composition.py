# Example: Adapter Pattern (Object Adapter)

class Channel_V1(object):

    @staticmethod
    def applyConfig():
        print('Configuration method of the old device class!')


class Channel_V2(object):

    @staticmethod
    def configure():
        print('Configuration method of the new device class!')


class ChannelAdapter(Channel_V1):
    # Class adapter (with composition)

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def applyConfig(self):
        self.adaptee.configure()


def host_app(channel):
    channel.applyConfig()


if __name__ == "__main__":
    # Original code using the old service
    host_app(channel=Channel_V1())

    # Use adapter for the new service adapted to the old interface
    host_app(channel=ChannelAdapter(adaptee=Channel_V2()))
