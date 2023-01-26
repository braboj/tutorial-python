# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.errors import *

class Packet(object):

    def __init__(self, packet_id, payload):
        self.id = packet_id
        self.length = len(payload)
        self.payload = payload

    def __str__(self):
        packet_id = str(self.id)
        length = str(self.length)
        payload = self.payload
        message = "PACKET ID: {0} | LEN={1} | PAYLOAD={2}".format(packet_id, length, payload)
        return message

    def to_bytes(self):
        stream = [self.id, self.length]
        stream.extend(self.payload)
        return bytearray(stream)

    @classmethod
    def from_bytes(cls, stream):

        stream = bytearray(stream)

        # Read the packet ID and remove it from the stream
        packet_id = stream[0]
        packet = None

        if packet_id == ConnectPacket.ID:
            packet = ConnectPacket.from_bytes(stream)

        elif packet_id == DisconnectPacket.ID:
            packet = DisconnectPacket.from_bytes(stream)

        elif packet_id == SubscribePacket.ID:
            packet = SubscribePacket.from_bytes(stream)

        elif packet_id == UnsubscribePacket.ID:
            packet = UnsubscribePacket.from_bytes(stream)

        elif packet_id == PublishPacket.ID:
            packet = PublishPacket.from_bytes(stream)

        return packet

###################################################################################################

class ConnectPacket(Packet):

    ID = 1

    def __init__(self, payload=()):
        self.payload = payload
        self.length = len(self.payload)

        super(ConnectPacket, self).__init__(packet_id=self.ID, payload=self.payload)

    @classmethod
    def from_bytes(cls, stream):
        length = stream[1]
        payload = stream[2:length + 2]
        return cls(payload=payload)

###################################################################################################

class DisconnectPacket(Packet):

    ID = 2

    def __init__(self, payload=()):
        self.payload = payload
        self.length = len(self.payload)

        super(DisconnectPacket, self).__init__(packet_id=self.ID, payload=self.payload)

    @classmethod
    def from_bytes(cls, stream):
        length = stream[1]
        payload = stream[2:length + 2]
        return cls(payload=payload)

###################################################################################################

class SubscribePacket(Packet):

    ID = 3

    def __init__(self, topics):
        self.topics = topics
        payload = []
        for topic in topics:
            topic_name = topic.encode('utf-8')
            topic_length = len(topic_name)
            payload.append(topic_length)
            payload.extend(topic_name)


        self.payload = payload
        self.length = len(self.payload)
        super(SubscribePacket, self).__init__(packet_id=self.ID, payload=self.payload)

    @classmethod
    def from_bytes(cls, stream):
        length = stream[1]
        payload = stream[2:length + 2]
        topics = []
        while payload:
            topic_len = payload[0]
            topic_name = payload[1:topic_len + 1]
            payload = payload[topic_len + 1:]
            topics.append(topic_name.decode('utf-8'))

        return cls(topics=topics)

###################################################################################################

class UnsubscribePacket(Packet):

    ID = 4

    def __init__(self, topics):
        self.topics = topics
        payload = []
        for topic in topics:
            topic_name =  topic.encode('utf-8')
            topic_length = len(topic_name)
            payload.append(topic_length)
            payload.extend(topic_name)


        self.payload = payload
        self.length = len(self.payload)
        super(UnsubscribePacket, self).__init__(packet_id=self.ID, payload=self.payload)

    @classmethod
    def from_bytes(cls, stream):
        length = stream[1]
        payload = stream[2:length + 2]
        topics = []
        while payload:
            topic_len = payload[0]
            topic_name = payload[1:topic_len + 1]
            payload = payload[topic_len + 1:]
            topics.append(str(topic_name))

        return cls(topics=topics)

###################################################################################################


class PublishPacket(Packet):

    ID = 5

    def __init__(self, topic, data):

        self.topic = topic.encode('utf-8')
        self.data = data
        self.payload = [len(self.topic)]
        self.payload.extend(self.topic)
        self.payload.extend(data)

        super(PublishPacket, self).__init__(packet_id=self.ID, payload=self.payload)

    @classmethod
    def from_bytes(cls, stream):
        # id = stream[0]
        length = stream[1]
        payload = stream[2:length + 2]
        topic_len = payload[0]
        topic_name = payload[1:topic_len + 1]
        data = payload[topic_len + 1:]

        return cls(topic=topic_name.decode('utf-8'), data=data)


###################################################################################################
# TESTS
###################################################################################################

def test_connect(payload=(1, 2, 3, 4, 5)):

    packet = ConnectPacket(payload)
    print("@CONNECT")
    print("PAYLOAD = {0}".format(payload))

    # Serialize packet
    serialized = tuple(packet.to_bytes())
    print("SERIALIZED = {0}".format(serialized))

    # Deserialize packet
    deserialized = Packet.from_bytes(serialized)
    print("DESERIALIZED = {0}".format(deserialized))

def test_disconnect(payload=(1, 2, 3, 4, 5)):

    packet = DisconnectPacket(payload)
    print("@DISCONNECT")
    print("PAYLOAD = {0}".format(payload))

    # Serialize packet
    serialized = tuple(packet.to_bytes())
    print("SERIALIZED = {0}".format(serialized))

    # Deserialize packet
    deserialized = Packet.from_bytes(serialized)
    print("DESERIALIZED = {0}".format(deserialized))

def test_subscribe(topics=('welcome', 'home')):

    packet = SubscribePacket(topics)
    print("@SUBSCRIBE")
    print("TOPICS = {0}".format(topics))

    # Serialize packet
    serialized = tuple(packet.to_bytes())
    print("SERIALIZED = {0}".format(serialized))

    # Deserialize packet
    deserialized = Packet.from_bytes(serialized)
    print("DESERIALIZED = {0}".format(deserialized))

def test_unsubscribe(topics=('welcome', 'home')):

    packet = UnsubscribePacket(topics)
    print("@UNSUBSCRIBE")
    print("TOPICS = {0}".format(topics))

    # Serialize packet
    serialized = tuple(packet.to_bytes())
    print("SERIALIZED = {0}".format(serialized))

    # Deserialize packet
    deserialized = Packet.from_bytes(serialized)
    print("DESERIALIZED = {0}".format(deserialized))

def test_publish(topic='welcome', data=(0xAA, 0x55)):

    packet = PublishPacket(topic, data)
    print("@PUBLISH")
    print("TOPIC = '{0}' DATA = {1}".format(topic, data))

    # Serialize packet
    serialized = tuple(packet.to_bytes())
    print("SERIALIZED = {0}".format(serialized))

    # Deserialize packet
    deserialized = Packet.from_bytes(serialized)
    print("DESERIALIZED = {0}".format(deserialized))


###################################################################################################
# MAIN
###################################################################################################

if __name__ == "__main__":
    test_connect()
    test_disconnect()
    test_subscribe()
    test_unsubscribe()
    test_publish()



