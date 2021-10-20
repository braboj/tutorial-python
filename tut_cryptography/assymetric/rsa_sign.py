# coding: utf-8

"""
SHA = Secure Hash Algorithm 2
PSS = Probabilistic Signature Scheme (PKCS#1 v2.1) used for padding of RSA signatures
MGF = Mask Generator Function
"""

from __future__ import print_function
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.hashes import Hash, SHA256
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils

##################################################################################################
# A. SIGN THE MESSAGE
##################################################################################################

# Create sample message
message = b'1' * 100

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Hash multipes of the message
hasher = Hash(algorithm=SHA256())
for i in range(1000):
    hasher.update(message)
digest = hasher.finalize()

# Digest must be 32 bytes
print([hex(x) for x in bytearray(digest)])
print(len(digest))

# Sign the message digest
signature = private_key.sign(
    digest,
    padding.PSS(
        mgf=padding.MGF1(SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    utils.Prehashed(SHA256())
)

# Signature must be 256 bytes
print([hex(x) for x in bytearray(signature)])
print(len(signature))


##################################################################################################
# B. VERIFY THE MESSAGE
##################################################################################################

# Obtain public key
public_key = private_key.public_key()

# Verify signed message
public_key.verify(
    signature,
    message * 1000,
    padding.PSS(
        mgf=padding.MGF1(SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    SHA256()
)
