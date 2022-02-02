from  binascii import unhexlify

test = b"73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = unhexlify(test)
data = [ord(x) for x in decoded]
print(decoded)

result = {}
for key in range(1, 256):
    output = b""
    for b in data:
        output += chr(b ^ key)

    result[key] = output

flag = [x for x in result.values() if "crypto" in x]
print(flag)