"""
HVLPSRV_NET_

    01: Connect
        01: Header
        02: Payload

    02: Disconnect
        01: Header
        02: Payload

    03: Subscribe
        01: Header
        02: Payload

    04: Unsubscribe
        01: Header
        02: Payload

    05: Publish
        01: Header
        02: Payload

    06: Socket
        01: Open
        02: Close
        03:


HVLPCLI_NET_
HVLPSRV_API_
HVLPCLI_API_
"""

from broker_app import *
import logging
import time


class TestOp(object):

    BROKER_ADDR = 'localhost'
    # BROKER_ADDR = '172.20.50.82'
    BROKER_PORT = 65432
    NUM_CLIENTS = 1000

    def __init__(self):

        self.broker = HvlpBroker(
            ip_addr=self.BROKER_ADDR,
            port=self.BROKER_PORT
        )

        self.log = logging.getLogger(self.__class__.__name__)

    def execute(self):
        pass


class HVLPSRV_NET_01_02(TestOp):

    def __init__(self):
        super(HVLPSRV_NET_01_02, self).__init__()
        self.messages = []

    def producer(self):

        sock = socket.socket()
        sock.connect((self.BROKER_ADDR, self.BROKER_PORT))

        # Connect
        sock.sendall(ConnectPacket().to_bytes())
        time.sleep(1)

        # Subscribe
        sock.sendall(SubscribePacket(topics=['test']).to_bytes())
        time.sleep(1)

        # Produce
        i = 0
        while True:
            i += 1
            data = PublishPacket(topic='test', data=[(i % 255), ]).to_bytes()
            sock.sendall(data)
            # time.sleep(0.0001)

    def consumer(self):

        sock = socket.socket()
        sock.connect((self.BROKER_ADDR, self.BROKER_PORT))

        # Connect
        sock.sendall(ConnectPacket().to_bytes())
        time.sleep(1)

        # Subscribe
        sock.sendall(SubscribePacket(topics=['test']).to_bytes())
        time.sleep(1)

        # Produce
        while True:
            message = sock.recv(1024)
            self.messages.append(message)
            self.log.info(Packet.from_bytes(message)[0])

    def execute(self):

        t1 = threading.Thread(target=self.producer)
        t1.start()

        t2 = threading.Thread(target=self.consumer)
        t2.start()


configure_logger()
test = HVLPSRV_NET_01_02()
test.execute()
