import socket
import sys
import select
import threading


class ChatClient(object):

    def __init__(self, host, port):

        self.done = threading.Event()
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.connect((host, port))
            print("ChatClient connecting...")

        except socket.error:
            print("Connection error!")

    def read_io(self):
        while not self.done.isSet():
            message = input()
            if message == "exit":
                self.done.set()
            self.sock.send(bytearray(message.encode('utf-8')))

    def run(self):

        t = threading.Thread(target=self.read_io)
        t.start()

        while not self.done.isSet():
            message = self.sock.recv(2048)
            print(message)

        self.sock.close()
        t.join()


if __name__ == "__main__":
    myclient = ChatClient('192.168.210.11', 2626)
    myclient.run()
