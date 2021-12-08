# coding: utf-8
from __future__ import print_function

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, KeySerializationEncryption, \
    PublicFormat

##################################################################################################
# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serialize private key
pem_private = private_key.private_bytes(
    encoding=Encoding(serialization.Encoding.PEM),
    format=PrivateFormat(serialization.PrivateFormat.PKCS8),
    encryption_algorithm=serialization.NoEncryption(),
    # encryption_algorithm=serialization.BestAvailableEncryption(password='1234'),
)
for line in pem_private.splitlines():
    print(line)
print()

# Write private key to a file
with open(name='private.key', mode='wb') as f:
    f.write(pem_private)

# Load private key
with open(name='private.key', mode='rb') as f:
    data = f.read()
    loaded_privkey = serialization.load_pem_private_key(
        data=data,
        password=None
    )
print(loaded_privkey)

##################################################################################################

# Generate public key
public_key = private_key.public_key()

# Serialize public key
pem_public = public_key.public_bytes(
    encoding=Encoding(serialization.Encoding.PEM),
    format=PublicFormat(serialization.PublicFormat.SubjectPublicKeyInfo),
)
for line in pem_public.splitlines():
    print(line)
print()

# Write public key to a file
with open(name='public.key', mode='wb') as f:
    f.write(pem_public)

# Load public key key
with open(name='public.key', mode='rb') as f:
    data = f.read()
    print(data)
    loaded_pubkey = serialization.load_pem_public_key(
        data=data,
    )
print(loaded_pubkey)
