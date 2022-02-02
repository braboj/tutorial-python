# coding: utf-8

from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat
from cryptography import x509
from cryptography.x509 import NameOID
import datetime

##################################################################################################
# A. GENERATE OWN KEY
##################################################################################################

# Generate own private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate own public key
public_key = private_key.public_key()

# Serialize own private key
pem = private_key.private_bytes(
        encoding=Encoding(serialization.Encoding.PEM),
        format=PrivateFormat(serialization.PrivateFormat.TraditionalOpenSSL),
        encryption_algorithm=serialization.NoEncryption(),
    )

# Save own private key
with open("ia.key", "wb") as f:
    f.write(pem)

##################################################################################################
# B. BUILD OWN CSR
##################################################################################################

csr = x509.CertificateSigningRequestBuilder()
one_day = datetime.timedelta(1, 0, 0)

# Subject
DN = list()
DN.append(x509.NameAttribute(NameOID.COMMON_NAME, u'local.intermediate'))
DN.append(x509.NameAttribute(NameOID.COUNTRY_NAME, u'BG'))
DN.append(x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u'Varna'))
DN.append(x509.NameAttribute(NameOID.LOCALITY_NAME, u'Varna'))
DN.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, u'Hilscher DTC'))
DN.append(x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, u'Embedded'))
csr = csr.subject_name(x509.Name(DN))

# Extensions
csr = csr.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
ert_builder = csr.add_extension(x509.SubjectAlternativeName([x509.DNSName(u'localhost')]), critical=False)

# Sign the certificate
csr = csr.sign(private_key=private_key, algorithm=SHA256())
isinstance(csr, x509.Certificate)

# Serialize the certificate
pem = csr.public_bytes(encoding=Encoding(serialization.Encoding.PEM))

# Write our certificate request
with open("ca.csr", "wb") as f:
    f.write(pem)

##################################################################################################
# C. SIGN CSR BY ISSUER
##################################################################################################

# Load issuer certificate
with open(name='ca.crt', mode='rb') as f:
    issuer = x509.load_pem_x509_certificate(data=f.read())

# Load issuer private key
with open(name='ca.key', mode='rb') as f:
    issuer_key = serialization.load_pem_private_key(data=f.read(), password=None)

# Create Intermediate Authority Certificate
builder = x509.CertificateBuilder()
builder = builder.subject_name(csr.subject)
builder = builder.public_key(csr.public_key())
builder = builder.serial_number(x509.random_serial_number())
builder = builder.not_valid_before(datetime.datetime.utcnow())
builder = builder.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365 * 5))
builder = builder.issuer_name(issuer.subject)
builder = builder.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=False)

crt = builder.sign(private_key=issuer_key, algorithm=issuer.signature_hash_algorithm)

# Save Intermediate Authority Certificate
with open(name='ia.crt', mode='wb') as f:
    f.write(crt.public_bytes(Encoding(serialization.Encoding.PEM)))
