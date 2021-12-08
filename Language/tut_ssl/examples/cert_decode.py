import ssl
from cryptography import x509
from cryptography.hazmat.backends import default_backend

pem = ssl.get_server_certificate(addr=("www.hilscher.com", 443), ca_certs="")
data = bytearray(pem, encoding="utf-8")

cert = x509.load_pem_x509_certificate(data, default_backend())
print(cert.version)
print(cert.issuer)
print(cert.subject)
print(bytes(cert.signature))
print(cert.not_valid_before)
print(cert.not_valid_after)

for extension in cert.extensions:
    print(extension)

pass
