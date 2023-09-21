import Crypto.Util.number as number

key1 = 1
key2 = 2
key3 = 3
flag = 4
print(key1, key2, key3, flag)

a = key1
b = key1 ^ key2
c = key2 ^ key3
d = flag ^ key1 ^ key3 ^ key2
print(a, b, c, d)

key1 = a
key2 = b ^ key1
key3 = c ^ key2
flag = d ^ key1 ^ key2 ^ key3
print(key1, key2, key3, flag)

A = int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313", base=16)
B = int("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", base=16)
C = int("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", base=16)
D = int("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", base=16)

key1 = A
key2 = A ^ key1
key3 = C ^ key2
flag = D ^ key1 ^ key2 ^ key3
print(number.long_to_bytes(flag))







