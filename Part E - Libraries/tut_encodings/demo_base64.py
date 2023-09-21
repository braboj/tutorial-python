# coding=utf-8
import base64

# Convert UTF-8 to list of bytes (our test data)
test = u"Хилшер"
test = bytearray(test, encoding="utf-8")

# Convert data to bytes
data = bytes(test)

# Encode/decode using bytes methods
encoded = data.encode(encoding="base64").strip("\n")
decoded = encoded.decode(encoding="base64").strip("\n")
print("{test} : {encoded} : {decoded}".format(test=test, encoded=encoded, decoded=decoded))

# Encode/decode using base64
encoded = base64.b64encode(test)
decoded = base64.b64decode(encoded)
print("{test} : {encoded} : {decoded}".format(test=test, encoded=encoded, decoded=decoded))

