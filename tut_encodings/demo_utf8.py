# coding=utf-8

# Convert UTF-8 to list of bytes (our test data)
test = u"Хилшер"
test = bytearray(test, encoding="utf-8")

# Encode and decode data
data = bytes(test)
encoded = data.decode('UTF-8')
decoded = encoded.encode('UTF-8')
print(test, encoded, decoded)