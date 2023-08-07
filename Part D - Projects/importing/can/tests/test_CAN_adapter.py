# coding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from HilscherFramework.Testcase import Testcase
from HilscherFramework.Test import runTest
from Components.can.adapters.can_open_master import *


class test_CAN_adapter(Testcase):
    """ Test the receive functionality with IXXAT or another packet analyzer """

    _device_adapter_ = CANDL_Device

    def __init__(self):
        super(test_CAN_adapter, self).__init__()
        self.description = "Configuration demo for master and slave"

    def test(self, adapter):

        try:
            # Select the desired packet API for CANDL
            adapter.api(CANDL_API_V2)

            # Create and reset the emulator
            emulator = CanNode(device=adapter)
            emulator.reset()

            # Configure the dut and the master
            emulator.configure()

            # Configure the emulator listener
            emulator.start_listen(can_id=(0x7FF, 0x602))
            emulator.stop_listen(can_id=0x7FF)

            # Send a basic CAN frame
            message = CanFrameBasic(can_id=0x603, data=[0xA, 0xB, 0xC, 0xD, 0xE, 0xF], rtr=False)
            emulator.send(message)

            # Receive a CAN frame
            message = emulator.recv(timeout=10)
            self.log.info(message)

            # Send an extended CAN frame
            message = CanFrameExtended(can_id=0x1FFFFFFF, data=[0x00, 0x4B, 0x03, 0x01, 0x01, 0x03, 0x05, 0x09])
            emulator.send(message)

            # Receive a CAN frame
            message = emulator.recv(timeout=10)
            self.log.info(message)

        except Exception as e:
            self.log.error(e)
            raise

        finally:
            pass


# test = Api_Configure_Master
# test = Api_Configure_Slave
test = test_CAN_adapter

if __name__ == "__main__":
    runTest(test)
