# encoding: utf-8
import socket

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
sock.connect(('localhost', 2525))

while True:
    pass
