# Example: Adapter Pattern (Class Adapter)

class ChannelV1(object):

    @staticmethod
    def apply_config():
        print('Configuration method of the old device class!')


class ChannelV2(object):

    @staticmethod
    def configure():
        print('Configuration method of the new device class!')


class ChannelAdapter(ChannelV1, ChannelV2):
    # Class adapter (with inheritance)

    def apply_config(self):
        self.configure()


def host_app(channel):
    channel.apply_config()


if __name__ == "__main__":
    # Original code using the old service
    host_app(channel=ChannelV1())

    # Use adapter for the new service adapted to the old interface
    host_app(channel=ChannelAdapter())
