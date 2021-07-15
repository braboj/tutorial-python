# coding=utf-8

# Convert UTF-8 to list of bytes (our test data)
test = u"Хилшер"
test = bytearray(test, encoding="utf-8")

# Encode and decode data
data = bytes(test)
encoded = data.encode(encoding="hex")
decoded = encoded.decode(encoding="hex")
print("{test} : {encoded} : {decoded}".format(test=test, encoded=encoded, decoded=decoded))
