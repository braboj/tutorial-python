# Example: Static method are not bound to the class and can be used as utility functions

class Packet(object):

    max_payload = 1024

    def __init__(self, ip_addr='192.168.10.1', mask="255.255.255.0", payload=()):
        self.payload = payload
        self.ip_addr = ip_addr
        self.mask = mask

    @staticmethod
    def dot_to_bytes(val):
        return bytes(map(int, val.split('.')))

    @staticmethod
    def bytes_to_dot(val):
        return '.'.join(map(str, val))


# Convert IP address in dot notation to bytes
addr_bytes = Packet.dot_to_bytes('192.168.1.1')
print(addr_bytes)

# Convert bytes to IP address in dot notation
addr_dot = Packet.bytes_to_dot(addr_bytes)
print(addr_dot)







