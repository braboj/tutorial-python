# Example : A bad example that violates the Single Responsibility Principle

CONNECT_CMD = 1
SUBSCRIBE_CMD = 2


class Packet(object):

    # Code smell: The has too many methods that are not related to each other
    # and that can be grouped into different classes. For example we can either
    # have a class for parsing and another for building or we can have a class
    # for each packet type.

    def __init__(self, packet_type, data):
        self.packet_type = packet_type
        self.data = data

    def parse(self, stream):

        packet_type = stream[0]

        if packet_type == CONNECT_CMD:
            self.parse_connect(stream[1:])

        elif packet_type == SUBSCRIBE_CMD:
            self.parse_subscribe(stream[1:])

        else:
            print("Invalid packet type")

    def build(self):

        if self.packet_type == CONNECT_CMD:
            return self.build_connect()

        elif self.packet_type == SUBSCRIBE_CMD:
            return self.build_subscribe(topics=self.data)

        else:
            print("Invalid packet type")

    @staticmethod
    def build_connect():
        return [CONNECT_CMD]

    def parse_connect(self, stream):
        self.packet_type = stream[0]
        self.data = stream[1:]

    @staticmethod
    def build_subscribe(topics):
        stream = [SUBSCRIBE_CMD]
        for topic in topics:
            stream.extend(topic.encode("utf-8"))

        return stream

    def parse_subscribe(self, stream):
        self.packet_type = stream[0]
        self.data = stream[1:]
        return stream


packet = Packet(packet_type=SUBSCRIBE_CMD, data=["topic1", "topic2"])
request = packet.build()
