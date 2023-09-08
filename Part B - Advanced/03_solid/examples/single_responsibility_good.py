# Example : A good example that follows the Single Responsibility Principle

from abc import ABC, abstractmethod

CONNECT_CMD = 1
SUBSCRIBE_CMD = 2


class PacketABC(ABC):

    # GOOD: Each class has a single responsibility. The ConnectPacket class
    # is responsible for parsing and building CONNECT packets. This class
    # ensures that each packet class will have the same interface.

    @abstractmethod
    def parse(self, stream):
        pass

    @abstractmethod
    def build(self):
        pass


class ConnectPacket(PacketABC):

    # GOOD: The ConnectPacket classi is responsible for parsing and building
    # CONNECT packets.

    def __init__(self):
        super(ConnectPacket, self).__init__(packet_type=1)
        self.packet_type = 1

    def parse(self, stream):
        self.packet_type = stream[0]

    def build(self):
        return [self.packet_type]


class SubscribePacket(PacketABC):

    # GOOD: The SubscribePacket classi is responsible for parsing and building
    # CONNECT packets.

    def __init__(self, topics):
        super(SubscribePacket, self).__init__()
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


packet = SubscribePacket(topics=["topic1", "topic2"])
request = packet.build()
