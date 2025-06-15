# adapter_with_inheritance

```python
class ChannelV1(object):

    @staticmethod
    def applyConfig():
        # method name from actual legacy code in the company (Python 2.7)
        print('Configuration method of the old device class!')


class ChannelV2(object):

    @staticmethod
    def configure():
        print('Configuration method of the new device class!')


class ChannelAdapter(ChannelV1, ChannelV2):
    # Class adapter (with inheritance)

    def applyConfig(self):
        # The adapter's applyConfig method calls the new class's configure method
        self.configure()


def host_app(channel):
    # The host_app function works with the ChannelV1 interface
    channel.applyConfig()


if __name__ == "__main__":
    # Original code using the old service (ChannelV1)
    host_app(channel=ChannelV1())

    # Use adapter for the new service (ChannelV2) adapted to the old interface (ChannelV1)
    host_app(channel=ChannelAdapter())
```
