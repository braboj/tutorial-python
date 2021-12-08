from ctypes import *


class Demo(LittleEndianStructure):
    _pack = 1
    _fields_ = [
        ("_vendor", c_uint),
        ("_serial", c_uint),
    ]

    @property
    def vendor(self):
        size = sizeof(self._fields_[0][1])
        buf = (c_byte * size)()
        memmove(addressof(buf), addressof(self._vendor.offset), size)
        return tuple(buf)


if __name__ == "__main__":
    d = Demo(1, 2)
    print(d.vendor)
