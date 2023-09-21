#!/usr/bin/env python

import sys
from ctypes import *


class SRamAccess(Structure):
    _fields_ = [
        ("channel", c_uint),
        ("offset", c_uint),
        ("len", c_uint),
        ("data", c_char_p),
    ]

    @classmethod
    def deserialize(cls, buf):
        inst = cls.from_buffer(buf)
        return inst

    def serialize(self):
        struct_size = sizeof(SRamAccess)
        size = struct_size + self.len
        buf = (c_byte * size)()
        memmove(addressof(buf), addressof(self), struct_size)
        memmove(addressof(buf) + struct_size, self.data.off, self.len)
        return buf

    def __str__(self):
        s = self.__repr__()
        for field_name, _ in self._fields_[:-1]:
            s += "\n  {0:s}: {1:}".format(field_name, getattr(self, field_name))
        s += "\n  {0:s}:".format(self._fields_[-1][0])
        for i in range(self.len):
            s += " 0x{0:02X}".format(self.data[i])
        return "{0:s}\n".format(s)


def main(*argv):
    text = b"abcd12345"
    ssrc = SRamAccess(1, 2, len(text), text)
    print("Src:", ssrc)
    buf = ssrc.serialize()
    print("Buf:", tuple(buf))
    sdst = SRamAccess.deserialize(buf)
    print("\nDst:", sdst)


if __name__ == "__main__":
    # print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    main(*sys.argv[1:])
    print("\nDone.")