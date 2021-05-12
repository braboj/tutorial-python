import socket

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SOL : Socket Layer
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ----------------------------------------------------------------------------
# SO_ACCEPTCONN : Linux/Windows, TCP
# ----------------------------------------------------------------------------
SO_ACCEPTCONN = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("SO_ACCEPTCONN=", end="")
print(SO_ACCEPTCONN.getsockopt(socket.SOL_SOCKET, socket.SO_ACCEPTCONN))


# ----------------------------------------------------------------------------
# SO_BROADCAST : Linux/Windows, UDP
# ----------------------------------------------------------------------------
SO_BROADCAST = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("SO_BROADCAST=", end="")
print(SO_BROADCAST.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST))


# ----------------------------------------------------------------------------
# SO_DEBUG : Linux/Windows, TCP/UDP
# ----------------------------------------------------------------------------
SO_DEBUG = socket.socket()
print("SO_DEBUG=", end="")
print(SO_DEBUG.getsockopt(socket.SOL_SOCKET, socket.SO_DEBUG))


# ----------------------------------------------------------------------------
# SO_DOMAIN :
# ----------------------------------------------------------------------------
# SO_DOMAIN = socket.socket()
# print("SO_DOMAIN=", end="")
# print(SO_DOMAIN.getsockopt(socket.SOL_SOCKET, socket.SO_DOMAIN))


# ----------------------------------------------------------------------------
# SO_DONTROUTE : Linux/Windows, UDP
# ----------------------------------------------------------------------------
SO_DONTROUTE = socket.socket()
print("SO_DONTROUTE=", end="")
print(SO_DONTROUTE.getsockopt(socket.SOL_SOCKET, socket.SO_DONTROUTE))


# ----------------------------------------------------------------------------
# SO_ERROR : Linux/Windows, TCP/UDP
# ----------------------------------------------------------------------------
SO_ERROR = socket.socket()
print("SO_ERROR=", end="")
print(SO_ERROR.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR))


# ----------------------------------------------------------------------------
# SO_EXCLUSIVEADDRUSE : Linux/Windows, TCP/UDP
# ----------------------------------------------------------------------------
SO_EXCLUSIVEADDRUSE = socket.socket()
print("SO_EXCLUSIVEADDRUSE=", end="")
print(SO_EXCLUSIVEADDRUSE.getsockopt(
    socket.SOL_SOCKET,
    socket.SO_EXCLUSIVEADDRUSE)
)


# ----------------------------------------------------------------------------
# SO_KEEPALIVE : Linux/Windows, TCP
# ----------------------------------------------------------------------------
SO_KEEPALIVE = socket.socket()
print("SO_KEEPALIVE=", end="")
print(SO_KEEPALIVE.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE))


# ----------------------------------------------------------------------------
# SO_LINGER : Linux/Windows, TCP
# ----------------------------------------------------------------------------
SO_LINGER = socket.socket()
print("SO_LINGER=", end="")
print(SO_LINGER.getsockopt(socket.SOL_SOCKET, socket.SO_LINGER))


# ----------------------------------------------------------------------------
# SO_MARK :
# ----------------------------------------------------------------------------
# SO_MARK = socket.socket()
# print("SO_MARK=", end="")
# print(SO_MARK.getsockopt(socket.SOL_SOCKET, socket.SO_MARK))


# ----------------------------------------------------------------------------
# SO_OOBINLINE :
# ----------------------------------------------------------------------------
SO_OOBINLINE = socket.socket()
print("SO_OOBINLINE=", end="")
print(SO_OOBINLINE.getsockopt(socket.SOL_SOCKET, socket.SO_OOBINLINE))


# ----------------------------------------------------------------------------
# SO_PASSCRED :
# ----------------------------------------------------------------------------
# SO_PASSCRED = socket.socket()
# print("SO_PASSCRED=", end="")
# print(SO_PASSCRED.getsockopt(socket.SOL_SOCKET, socket.SO_PASSCRED))


# ----------------------------------------------------------------------------
# SO_PASSSEC :
# ----------------------------------------------------------------------------
# SO_PASSSEC = socket.socket()
# print("SO_PASSSEC=", end="")
# print(SO_PASSSEC.getsockopt(socket.SOL_SOCKET, socket.SO_PASSSEC))


# ----------------------------------------------------------------------------
# SO_PEERCRED :
# ----------------------------------------------------------------------------
# SO_PEERCRED = socket.socket()
# print("SO_PEERCRED=", end="")
# print(SO_PEERCRED.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED))

# ----------------------------------------------------------------------------
# SO_PEERSEC :
# ----------------------------------------------------------------------------
# SO_PEERSEC = socket.socket()
# print("SO_PEERSEC=", end="")
# print(SO_PEERSEC.getsockopt(socket.SOL_SOCKET, socket.SO_PEERSEC))


# ----------------------------------------------------------------------------
# SO_PRIORITY :
# ----------------------------------------------------------------------------
# SO_PRIORITY = socket.socket()
# print("SO_PRIORITY=", end="")
# print(SO_PRIORITY.getsockopt(socket.SOL_SOCKET, socket.SO_PRIORITY))


# ----------------------------------------------------------------------------
# SO_PROTOCOL :
# ----------------------------------------------------------------------------
# SO_PROTOCOL = socket.socket()
# print("SO_PROTOCOL=", end="")
# print(SO_PROTOCOL.getsockopt(socket.SOL_SOCKET, socket.SO_PROTOCOL))


# ----------------------------------------------------------------------------
# SO_RCVBUF :
# ----------------------------------------------------------------------------
SO_RCVBUF = socket.socket()
print("SO_RCVBUF=", end="")
print(SO_RCVBUF.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))


# ----------------------------------------------------------------------------
# SO_RCVLOWAT :
# ----------------------------------------------------------------------------
# SO_RCVLOWAT = socket.socket()
# print("SO_RCVLOWAT=", end="")
# print(SO_RCVLOWAT.getsockopt(socket.SOL_SOCKET, socket.SO_RCVLOWAT))


# ----------------------------------------------------------------------------
# SO_RCVTIMEO :
# ----------------------------------------------------------------------------
SO_RCVTIMEO = socket.socket()
print("SO_RCVTIMEO=", end="")
print(SO_RCVTIMEO.getsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO))

# ----------------------------------------------------------------------------
# SO_REUSEADDR : Linux/Windows, TCP/UDP
# ----------------------------------------------------------------------------
SO_REUSEADDR = socket.socket()
print("SO_REUSEADDR=", end="")
print(SO_REUSEADDR.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))


# ----------------------------------------------------------------------------
# SO_REUSEPORT :
# ----------------------------------------------------------------------------
# SO_REUSEPORT = socket.socket()
# print("SO_REUSEPORT=", end="")
# print(SO_REUSEPORT.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT))


# ----------------------------------------------------------------------------
# SO_SETFIB :
# ----------------------------------------------------------------------------
# SO_SETFIB = socket.socket()
# print("SO_SETFIB=", end="")
# print(SO_SETFIB.getsockopt(socket.SOL_SOCKET, socket.SO_SETFIB))


# ----------------------------------------------------------------------------
# SO_SNDBUF :
# ----------------------------------------------------------------------------
SO_SNDBUF = socket.socket()
print("SO_SNDBUF=", end="")
print(SO_SNDBUF.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))


# ----------------------------------------------------------------------------
# SO_SNDLOWAT :
# ----------------------------------------------------------------------------
# SO_SNDLOWAT = socket.socket()
# print("SO_SNDLOWAT=", end="")
# print(SO_SNDLOWAT.getsockopt(socket.SOL_SOCKET, socket.SO_SNDLOWAT))


# ----------------------------------------------------------------------------
# SO_SNDTIMEO :
# ----------------------------------------------------------------------------
SO_SNDTIMEO = socket.socket()
print("SO_SNDTIMEO=", end="")
print(SO_SNDTIMEO.getsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO))


# ----------------------------------------------------------------------------
# SO_TYPE :
# ----------------------------------------------------------------------------
SO_TYPE = socket.socket()
print("SO_TYPE=", end="")
print(SO_TYPE.getsockopt(socket.SOL_SOCKET, socket.SO_TYPE))


# ----------------------------------------------------------------------------
# SO_USELOOPBACK : Windows
# ----------------------------------------------------------------------------
# SO_USELOOPBACK = socket.socket()
# print("SO_USELOOPBACK=", end="")
# print(SO_USELOOPBACK.getsockopt(socket.SOL_SOCKET, socket.SO_USELOOPBACK))


# ----------------------------------------------------------------------------
# SO_VM_SOCKETS_BUFFER_SIZE : Linux
# ----------------------------------------------------------------------------
# SO_VM_SOCKETS_BUFFER_SIZE = socket.socket(socket.AF_VSOCK)
# print("SO_VM_SOCKETS_BUFFER_SIZE=", end="")
# print(SO_VM_SOCKETS_BUFFER_SIZE.getsockopt(
#     socket.SOL_SOCKET,
#     socket.SO_VM_SOCKETS_BUFFER_SIZE)
# )


# ----------------------------------------------------------------------------
# SO_VM_SOCKETS_BUFFER_MIN_SIZE : Linux
# ----------------------------------------------------------------------------
# SO_VM_SOCKETS_BUFFER_MIN_SIZE = socket.socket(socket.AF_VSOCK)
# print("SO_VM_SOCKETS_BUFFER_MIN_SIZE=", end="")
# print(SO_VM_SOCKETS_BUFFER_MIN_SIZE.getsockopt(
#     socket.SOL_SOCKET,
#     socket.SO_VM_SOCKETS_BUFFER_MIN_SIZE)
# )


# ----------------------------------------------------------------------------
# SO_VM_SOCKETS_BUFFER_MAX_SIZE : Linux
# ----------------------------------------------------------------------------
# SO_VM_SOCKETS_BUFFER_MAX_SIZE = socket.socket(socket.AF_VSOCK)
# print("SO_VM_SOCKETS_BUFFER_MAX_SIZE=", end="")
# print(SO_VM_SOCKETS_BUFFER_MAX_SIZE.getsockopt(
#     socket.SOL_SOCKET,
#     socket.SO_VM_SOCKETS_BUFFER_MAX_SIZE)
# )
