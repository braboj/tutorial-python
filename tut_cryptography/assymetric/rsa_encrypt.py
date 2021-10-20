# coding: utf-8

"""
OAEP: Optimal asymmetric encryption padding used for RSA encryption
"""

from __future__ import print_function
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric import padding

# Create message to encrypt
message = b"encrypted data"

# Generate the private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate the public key
public_key = private_key.public_key()

# Encrypt the message with the public key
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=SHA256()),
        algorithm=SHA256(),
        label=None
    )
)
print(ciphertext)


# Decrypt the message with the private key
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=SHA256()),
        algorithm=SHA256(),
        label=None
    )
)
print(plaintext)
