class Device(object):

    def __init__(self, channel1, channel2):
        self._channel1 = channel1 or Channel_1()
        self._channel2 = channel2 or Channel_2()

    def operation(self):
        self._channel1.start()
        self._channel2.configure_flash()
        self._channel2.start()
        self._channel1.work()
        self._channel2.work()
        self._channel1.stop()
        self._channel2.stop()
        self._channel2.deconfigure_flash()


class Channel_1(object):

    @staticmethod
    def start():
        print("CHANNEL1: Send configuration packet")
        print("CHANNEL1: Send channel init")

    @staticmethod
    def work():
        print("CHANNEL1: Receiving data...")

    @staticmethod
    def stop():
        print("CHANNEL1: Send deconfigure")


class Channel_2(object):

    @staticmethod
    def configure_flash():
        print("CHANNEL2: Configure flash")

    @staticmethod
    def deconfigure_flash():
        print("CHANNEL2: Deconfigure flash")

    @staticmethod
    def start():
        print("CHANNEL2: Send configuration packet")
        print("CHANNEL2: Send channel init")

    @staticmethod
    def work():
        print("CHANNEL2: Receiving data ...")

    @staticmethod
    def stop():
        print("CHANNEL2: Send deconfigure")


def host_app(device: Device):
    device.operation()


if __name__ == "__main__":
    ch1 = Channel_1()
    ch2 = Channel_2()
    device = Device(ch1, ch2)
    host_app(device)
