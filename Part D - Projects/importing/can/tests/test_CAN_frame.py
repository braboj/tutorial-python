# coding: utf-8
from __future__ import print_function
from __future__ import unicode_literals

# Add the local directories to the system path
import sys
sys.path.append(str("."))
sys.path.append(str(".."))

from ..frame import *
from ..errors import *


def test_constructor():
    # Basic frame
    data_m = []
    for _ in range(20):
        data_m.append(10)
    message = CanFrameBasic(can_id=0x05, data=data_m)
    print(repr(message))
    print(message.data)
    print(message.can_id)
    print(message.rtr)
    message.report()

    # Extended frame
    message = CanFrameExtended(can_id=0x07, data=data_m)
    print(repr(message))
    print(message.data)
    print(message.can_id)
    message.report()


def test_can_id():
    """ Test frame generation until first invalid address is found """

    print("TEST CAN-ID VALIDATION...")
    errors = []
    frame_types = [CanFrameBasic, CanFrameExtended]

    for frame_type in frame_types:
        for i in (0, frame_type.MAX_CAN_ID - 1, frame_type.MAX_CAN_ID, frame_type.MAX_CAN_ID + 1):
            try:
                frame_type(can_id=i, data=[0x00, 0x4B, 0x03, 0x01, 0x01])
            except CanBusAddressError:
                print("Address error at 0x{0:X}".format(i))
                errors.append(True) if i == frame_type.MAX_CAN_ID + 1 else None

    print(errors)
    passed = all(errors)

    return passed


def test_rtr():
    """ Test RTR with non-boolean values """

    print("TEST RTR VALIDATION...")
    frame_types = [CanFrameBasic, CanFrameExtended]

    for frame_type in frame_types:
        for rtr_value in (0, 1, 2):
            frame = frame_type(rtr=rtr_value)
            print(frame)
            if bool(rtr_value) != frame.rtr:
                raise ValueError

    return True


def test_length():
    """ Test data length validation """

    print("TEST DATA LENGTH VALIDATION...")
    frame_types = [CanFrameBasic, CanFrameExtended]

    for frame_type in frame_types:
        for data_len in (0, 1, 16, 100, 256, 512):
            frame = frame_type(data=['a'] * data_len)
            print(frame.data)


def test_data():

    test_bytes = ['A' * 8, 'Ю' * 4]

    for data in test_bytes:
        payload = bytearray(data, "utf-8")
        frame = CanFrameBasic(data=payload)
        print(frame)


if __name__ == "__main__":
    test_can_id()
    test_rtr()
    test_length()
    test_constructor()
    test_data()
