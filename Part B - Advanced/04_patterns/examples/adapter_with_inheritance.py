# Example: Adapter Pattern (Class Adapter)

class ChannelV1(object):

    @staticmethod
    def applyConfig():
        # method name from actual legacy code in the company
        print('Configuration method of the old device class!')


class ChannelV2(object):

    @staticmethod
    def configure():
        print('Configuration method of the new device class!')


class ChannelAdapter(ChannelV1, ChannelV2):
    # Class adapter (with inheritance)

    def applyConfig(self):
        self.configure()


def host_app(channel):
    channel.applyConfig()


if __name__ == "__main__":
    # Original code using the old service
    host_app(channel=ChannelV1())

    # Use adapter for the new service adapted to the old interface
    host_app(channel=ChannelAdapter())
