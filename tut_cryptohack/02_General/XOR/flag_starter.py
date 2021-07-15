test = "label"
encoded = [ord(x) ^ 13 for x in test]
flag = "".join((chr(x) for x in encoded))
print("crypto{" + bytes(flag) + "}")