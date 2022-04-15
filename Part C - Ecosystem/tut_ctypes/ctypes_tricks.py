import ctypes

mac = [1, 2, 3, 4, 5, 6]

# (*...) will unpack the list
# arr[0] = mac[0]
# ...
# arr[5] = mac[5]

arr = (ctypes.c_ubyte * 6)(*mac)
print(arr)