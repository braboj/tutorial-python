# encoding: utf-8
import socket

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
sock.connect(('192.168.43.235', 2525))

while True:
    pass
