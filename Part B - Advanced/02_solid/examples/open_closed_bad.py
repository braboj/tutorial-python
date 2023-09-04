# Example : A bad example that violates the Open Closed Principle

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


class ConnectPacket(PacketABC):

    def __init__(self):
        super(ConnectPacket, self).__init__(packet_type=1)
        self.packet_type = 1

    def parse(self, stream):
        self.packet_type = stream[0]

    def build(self):
        return [self.packet_type]


class SubscribePacket(PacketABC):

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

        # Code smell: We need to add a validation to ensure that the stream is
        # not too long. If we add this validation here we will be violating
        # the Open-Closed Principle.

        # if len(stream) > 256:
        #     ...

        return stream


packet = SubscribePacket(topics=["topic1", "topic2"])
request = packet.build()
