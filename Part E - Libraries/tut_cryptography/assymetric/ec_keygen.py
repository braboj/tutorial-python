from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.serialization import *

##################################################################################################
# PRIVATE KEY
##################################################################################################

# Generate private key
private_key = ec.generate_private_key(
    curve=ec.SECP384R1()
)

# Serialize private key
pem = private_key.private_bytes(
    encoding=Encoding.PEM,
    format=PrivateFormat.PKCS8,
    encryption_algorithm=NoEncryption(),
)
print(pem)

# Save private key
with open(name='private.key', mode='wb') as f:
    f.write(pem)

# Load private key
with open(name='private.key', mode='rb') as f:
    data = f.read()
    loaded_key = load_pem_private_key(
        data=data,
        password=None
    )
    print(data)

# Create message
message = '1' * 100

# Sign message
signature = loaded_key.sign(
    data=message,
    signature_algorithm=ec.ECDSA(SHA256())
)

# Verify signature of loaded key with original public key
public_key = private_key.public_key()
public_key.verify(signature, message, ec.ECDSA(SHA256()))


##################################################################################################
# PUBLIC KEY
##################################################################################################

# Generate public key
public_key = private_key.public_key()

# Serialize public key
pem = public_key.public_bytes(
    encoding=Encoding(Encoding.PEM),
    format=PublicFormat(PublicFormat.SubjectPublicKeyInfo)
)
print(pem)

# Save public key
with open(name='public.key', mode='wb') as f:
    f.write(pem)

##################################################################################################

# Create message
message = '1' * 100

# Sign message
signature = private_key.sign(
    data=message,
    signature_algorithm=ec.ECDSA(SHA256())
)


# Verify signature
public_key.verify(signature, message, ec.ECDSA(SHA256()))