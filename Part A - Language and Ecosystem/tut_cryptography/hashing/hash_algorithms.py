# coding: utf-8
from __future__ import print_function
from cryptography.hazmat.primitives.hashes import Hash, SHA256
import hashlib

# Data > Hash Size
message = b'1' * 1000

# Cryptopgrahy library
hasher = Hash(algorithm=SHA256())
hasher.update(message)
a = hasher.finalize()
print(a)

# Hashlib library - Option 1
hasher = hashlib.sha256()
hasher.update(message)
b = hasher.digest()
print(b)

# Hashlib library - Option 2
hasher = hashlib.new('sha256')
hasher.update(message)
c = hasher.digest()
print(c)
