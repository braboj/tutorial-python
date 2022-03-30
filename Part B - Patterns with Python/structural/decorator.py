from abc import ABC, abstractmethod


class IPayload(ABC):

    @abstractmethod
    def build(self):
        raise NotImplementedError


class Payload(IPayload):

    def build(self):
        return "DEADBEEF"


class IPayloadDecorator(IPayload):

    def __init__(self, packet: IPayload):
        self.packet = packet

    def build(self):
        return self.packet.build()


class TlsPacket(IPayloadDecorator):

    def build(self):
        return f"TLS({self.packet.build()})"


class HttpPacket(IPayloadDecorator):
    def build(self):
        return f"HTTP({self.packet.build()})"


def host_app(packet):
    print(f"RESULT: {packet.build()}", end="")


if __name__ == "__main__":

    channel = Payload()
    print("Original payload:")
    host_app(channel)
    print("\n")

    tls_packet = TlsPacket(channel)
    http_packet = HttpPacket(tls_packet)
    print("Payload is now wrapped:")
    host_app(http_packet)
