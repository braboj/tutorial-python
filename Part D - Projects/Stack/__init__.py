from Device import CommunicationDevice

class DeviceNetSlaveV2(CommunicationDevice):
    name = "DNS V2"
    comclass = 2
    protoclass = 8

    @staticmethod
    def configure():
        print("V2")
