# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.session import *
from components.errors import *

import socket
import threading


class HVLPBroker(object):

    def __init__(self, ip_addr, port, protocol):
        self.ip_addr = ip_addr
        self.port = port
        self.session_type = protocol
        self.srv_sock = socket.socket()
        self.stop = threading.Event()
        self.register = {}

    def run(self):

        try:
            self.srv_sock.bind((self.ip_addr, self.port))
            self.srv_sock.listen(0)

            while True:

                # Wait for new connection requests
                connection, addr_info = self.srv_sock.accept()
                print("Connection from: {0}".format(addr_info))

                # Start the protocol session thread
                session = self.session_type(
                    broker=self,
                    connection=connection,
                    addr_info=addr_info
                )
                session.start()

        except HvlpError as e:
            print(e)


if __name__ == "__main__":
    server = HVLPBroker(ip_addr='localhost', port=65432, protocol=HVLPSession)
    server.run()
