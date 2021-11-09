# coding: utf-8

from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat
from cryptography import x509
from cryptography.x509 import NameOID
import datetime

##################################################################################################
# A. KEY GENERATION
##################################################################################################

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate public key
public_key = private_key.public_key()

# Serialize own private key
pem = private_key.private_bytes(
        encoding=Encoding(serialization.Encoding.PEM),
        format=PrivateFormat(serialization.PrivateFormat.TraditionalOpenSSL),
        encryption_algorithm=serialization.NoEncryption(),
    )

# Save private key
with open("ca.key", "wb") as f:
    f.write(pem)

##################################################################################################
# B. BUILD THE CERTIFICATE
##################################################################################################

cert = x509.CertificateBuilder()
one_day = datetime.timedelta(1, 0, 0)

# Subject
DN = list()
DN.append(x509.NameAttribute(NameOID.COMMON_NAME, u'local.root'))
DN.append(x509.NameAttribute(NameOID.COUNTRY_NAME, u'BG'))
DN.append(x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u'Varna'))
DN.append(x509.NameAttribute(NameOID.LOCALITY_NAME, u'Varna'))
DN.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, u'Hilscher DTC'))
DN.append(x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, u'Embedded'))
cert = cert.subject_name(x509.Name(DN))

# Issuer
cert = cert.issuer_name(x509.Name(DN))

# Validation period
cert = cert.not_valid_before(datetime.datetime.today() - one_day)
cert = cert.not_valid_after(datetime.datetime.today() + (one_day * 30))

# Cryptographic primitives
cert = cert.serial_number(x509.random_serial_number())
cert = cert.public_key(public_key)

# Extensions
cert = cert.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
ert_builder = cert.add_extension(x509.SubjectAlternativeName([x509.DNSName(u'localhost')]), critical=False)

# Sign the certificate
cert = cert.sign(private_key=private_key, algorithm=SHA256())
isinstance(cert, x509.Certificate)

##################################################################################################
# C. SAVE THE CERTIFICATE
##################################################################################################

# Serialize the certificate
pem = cert.public_bytes(encoding=Encoding(serialization.Encoding.PEM))

# Write our certificate out to disk.
with open("ca.crt", "wb") as f:
    f.write(pem)

# Load the certificate
with open("ca.crt", "rb") as f:
    data = f.read()
    test = x509.load_pem_x509_certificate(data=data)

# Evaluate results
print(test == cert)