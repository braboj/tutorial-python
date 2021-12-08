#!/usr/bin/env python

import sys
import ctypes as ct


class SRamAccess(ct.Structure):
    _fields_ = [
        ("channel", ct.c_uint),
        ("offset", ct.c_uint),
        ("len", ct.c_uint),
        ("data", ct.c_char_p),
    ]

    @classmethod
    def deserialize(cls, buf):
        inst = cls.from_buffer(buf)
        return inst

    def serialize(self):
        struct_size = ct.sizeof(SRamAccess)
        size = struct_size + self.len
        buf = (ct.c_char * size)()
        ct.memmove(ct.addressof(buf), ct.addressof(self), struct_size)
        ct.memmove(ct.addressof(buf) + struct_size, self.data, self.len)
        return bytearray(buf)

    def __str__(self):
        s = self.__repr__()
        for field_name, _ in self._fields_[:-1]:
            s += "\n  {0:s}: {1:}".format(field_name, getattr(self, field_name))
        s += "\n  {0:s}:".format(self._fields_[-1][0])
        for i in range(self.len):
            s += " 0x{0:02X}".format(self.data[i])
        return "{0:s}\n".format(s)


def main(*argv):
    text = b"abcd1234"
    ssrc = SRamAccess(1, 2, len(text), text)
    print("Src:", ssrc)
    buf = ssrc.serialize()
    print("Buf:", buf)
    sdst = SRamAccess.deserialize(buf)
    print("\nDst:", sdst)


if __name__ == "__main__":
    print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    main(*sys.argv[1:])
    print("\nDone.")