# Overview

### IP Addressing
0.0.0.0 : When binding sockets any address at all

### TCP States
LISTEN
SYN_SENT
SYN_RECEIVED
ESTABLISHED
FIN_WAIT1
FIN_WAIT2
CLOSE_WAIT
CLOSING
LAST_ACK
TIME_WAIT
CLOSED

### TCP Connection Handshake
CLIENT : SYN 100
SERVER : SYN 224 ACK 101
CLIENT : ACK 225

### TCP Connection Closure
CLIENT : FIN 100
SERVER : ACK 125


# Socket Module

# Socket Object

| API           | Description                                       |
|-------------- |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| socket()      | Socket constructor which determines the general behavior of the socket.                                                                                                                                               |
| bind()        | Bind the socket to an address. It is required for a server socket and optional for a client one. The client socket might be bound in case the NIC adapter has more than one address in the same network.              |
| listen()      | Set the socket to listen for new connection requests.                                                                                                                                                                 |
| accept()      | Used on the server side to accept incoming connection requests (TCP handshake). The socket must  be bound to an address and a port and it must be listening for new connections.                                      |
| connect()     | Connect to the remote address and port.                                                                                                                                                                               |
| connect_ex()  | Like connect but returns an error except an exception.                                                                                                                                                                |
| close()       | Close the socket. By default close will call shutdown unless the linger option is disabled. It this case the socket closure is called "abnormal".                                                                     |
| shutdown()    | Stops sending data, receiving data, or both on this socket. It is used to notify the peer that the connection will be closed soon and it is called a "graceful" disconnect. It is recommened to use it before close() |
| send()        | |
| sendall()     | |
| recv()        | |
| getsockname() | Return the socket’s own address  |
| getpeername() | Return the remote address to which the socket is connected |



# Socket Types

# Socket Options

# Socket Families
* AF_UNIX       : IPC for Unix processes
* AF_INET       : IPv4 communication
* AF_INET6      : IPv6 communication
* AF_NETLINK    : NetLink communication
* AF_CAN        : CAN Bus protocol communication
* AF_BLUETOOTH  : Bluetooth protocol communication
* AF_TIPC       : TPIC protocol for clustering
* AF_ALG        : Linux-only socket based interface to Kernel cryptography
* AF_VSOCK      : Communication between virtual machines and their hosts
* AF_PACKET     : Low-level interface directly to network devices
* AF_QIPCRTR    : Linux-only interface for services on Qualcomm platforms
