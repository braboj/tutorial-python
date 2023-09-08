# Example : A good example that follows the Open Closed Principle

from abc import ABC, abstractmethod

CONNECT_CMD = 1
SUBSCRIBE_CMD = 2


class PacketABC(ABC):

    @abstractmethod
    def parse(self, stream):
        pass

    @abstractmethod
    def build(self):
        pass


class Connect(PacketABC):

    def __init__(self):
        super(Connect, self).__init__(packet_type=1)
        self.packet_type = 1

    def parse(self, stream):
        self.packet_type = stream[0]

    def build(self):
        return [self.packet_type]


class Subscribe(PacketABC):

    # GOOD: The base class is not modified. Instead, a new class is created
    # that inherits from the base class and adds the validation to the build
    # method.

    def __init__(self, topics):
        super(Subscribe, self).__init__()
        self.packet_type = 2
        self.topics = topics

    def parse(self, stream):
        self.packet_type = stream[0]
        self.topics = stream[1:]

    def build(self):
        stream = [2]
        for topic in self.topics:
            stream.extend(topic.encode("utf-8"))

        return stream


class SubscribeWithValidation(Subscribe):

    # GOOD: Inheritance is used to add validation to the build method without
    # modifying the base class. This is a good example of the Open Closed
    # Principle.

    def build(self):
        stream = super(SubscribeWithValidation, self).build()
        if len(stream) > 256:
            raise ValueError("Stream too long")

        return stream


packet = Subscribe(topics=["1" * 300])
print(packet.build())

try:
    packet = SubscribeWithValidation(topics=["1" * 300])
    packet.build()

except ValueError as e:
    print(e)
