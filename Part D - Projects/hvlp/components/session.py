# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.packets import *
import threading
import socket

WAIT_CONNECT = 0
CONNECTED = 1

STATE_NAME = {
    WAIT_CONNECT: "WAIT_CONNECT",
    CONNECTED: "CONNECTED",
}


class HVLPSession(threading.Thread):

    def __init__(self, broker, connection, addr_info):
        super(HVLPSession, self).__init__()
        self.broker = broker
        self.connection = connection
        self.addr_info = addr_info

        self.state = WAIT_CONNECT
        self.stop = threading.Event()

    def on_subscribe(self, topics):

        # Check whether the topic exists and add the client to the list
        for topic in topics:
            self.broker.register.setdefault(topic, [])
            self.broker.register[topic].append(self.connection)

    def on_unsubscribe(self, topics):

        # Check whether the topic exists and remove the client from the list
        for topic in topics:
            self.broker.register[topic].remove(self.connection)

    def on_publish(self, topic, data):

        # Scan the topic register and re-send the publish packet to all subscribers
        for registered, clients in self.broker.register.items():

            # Scan the register for the desired topic
            if topic == registered:
                message = PublishPacket(topic, data).to_bytes()

                # Send the message to all the registered clients except the sender
                for client in clients:
                    if client != self.connection:
                        print("PUBLISH to {0}".format(client.getpeername()))
                        try:
                            client.sendall(message)
                        except socket.error:
                            print("Client not accessible, deleting fromt the register")
                            self.broker.register[topic].remove(client)

    def handle_packet(self, packet):

        if packet.id == SubscribePacket.ID:
            print("SUBSCRIBE from {0}".format(self.connection.getsockname()))
            self.on_subscribe(packet.topics)

        elif packet.id == UnsubscribePacket.ID:
            print("UNSUBSCRIBE from {0}".format(self.connection.getsockname()))
            self.on_unsubscribe(packet.topics)

        elif packet.id == PublishPacket.ID:
            print("PUBLISH from {0}".format(self.connection.getsockname()))
            self.on_publish(packet.topic, packet.data)

        else:
            print("UNEXPECTED PACKET")

    def update_state(self, packet):

        # STATE: WAIT_CONNECT
        if self.state == WAIT_CONNECT:
            if packet.id == ConnectPacket.ID:
                print('CONNECT from {0}'.format(self.addr_info))
                self.state = 1
            else:
                print("UNEXPECTED PACKET")

        # STATE: CONNECTED
        elif self.state == CONNECTED:
            if packet.id == DisconnectPacket.ID:
                print('DISCONNECT from {0}'.format(self.addr_info))
                self.stop.set()
            else:
                self.handle_packet(packet)

    def run(self):

        while not self.stop.is_set():
            try:
                message = self.connection.recv(1024)
                if message:
                    packet = Packet.from_bytes(message)
                    self.update_state(packet)

            except socket.error as e:
                self.stop.set()

        # Close the connection socket
        print("SESSION CLOSED")
        self.connection.close()

        # Remove connection from the registry
        print(self.broker.register)
        for topic, clients in self.broker.register.items():
            if self.connection in self.broker.register[topic]:
                self.broker.register[topic].remove(self.connection)

        print(self.broker.register)

