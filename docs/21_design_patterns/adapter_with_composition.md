# adapter_with_composition

```python
# Example: Adapter Pattern (Object Adapter)

class ChannelV1(object):

    @staticmethod
    def applyConfig():
        # method name from actual legacy code in the company
        print('Configuration method of the old device class!')


class ChannelV2(object):

    @staticmethod
    def configure():
        print('Configuration method of the new device class!')


class ChannelAdapter(ChannelV1):
    # Class adapter (with composition)

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def applyConfig(self):
        self.adaptee.configure()


def host_app(channel):
    channel.applyConfig()


if __name__ == "__main__":
    # Original code using the old service
    host_app(channel=ChannelV1())

    # Use adapter for the new service adapted to the old interface
    host_app(channel=ChannelAdapter(adaptee=ChannelV2()))
```
