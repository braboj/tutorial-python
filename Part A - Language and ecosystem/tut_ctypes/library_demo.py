from ctypes import *
import pathlib

libc = cdll.msvcrt
print(libc)
print(libc.printf)
print(libc.time(None))
print(hex(windll.kernel32.GetModuleHandleA(None)))
