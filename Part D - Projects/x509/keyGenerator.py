import logging

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import *
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils


class PrivateKey(object):

    def __init__(self,
                 encoding="DER",
                 filename="private.key",
                 ):

        self.log = logging.getLogger(self.__class__.__name__)
        self.log.addHandler(logging.NullHandler())

        # Attributes
        self.encoding = encoding.upper()
        self.filename = filename
        self.bytes = None
        self.key = None

    def serialize(self, encoding=None, password=None):

        # Check encoding
        if encoding is None:
            encoding = self.encoding

        # Check encryption method
        if password:
            encryption = BestAvailableEncryption(password=password)
        else:
            encryption = NoEncryption()

        # Generate stream of bytes
        self.bytes = self.key.private_bytes(
            encoding=Encoding(encoding),
            format=PrivateFormat.PKCS8,
            encryption_algorithm=encryption,
        )

        return self

    def save(self, filename=None, encoding=None, password=None):

        # Check filename
        if filename is None:
            filename = self.filename

        # Check encoding
        if encoding is None:
            encoding = self.encoding

        # Convert the key to a stream of bytes
        self.serialize(encoding, password)

        # Write private key to a file
        with open(name=filename, mode='wb') as f:
            f.write(self.bytes)

        return self

    def load(self, filename=None, encoding=None, password=None):

        # Check filename
        if filename is None:
            filename = self.filename

        # Check encoding
        if encoding is None:
            encoding = self.encoding

        # Read stream of bytes
        with open(name=filename, mode='rb') as f:
            self.bytes = f.read()

        # Initialize deserialization method
        if Encoding(encoding) == Encoding.PEM:
            deserialize = load_pem_private_key
        else:
            deserialize = load_der_private_key

        # Deserialize the data
        self.key = deserialize(
            data=self.bytes,
            password=password
        )

        return self


class PublicKey(object):

    def __init__(
            self,
            private_key,            # Public key will be derived from the private key
            filename="public.key",  # Filename for the private key
    ):

        self.log = logging.getLogger(self.__class__.__name__)
        self.log.addHandler(logging.NullHandler())

        # Attributes
        self.private_key = private_key
        self.filename = filename
        self.encoding = private_key.encoding
        self.hash_algorithm = private_key.hash_algorithm

        self.key = None
        self.bytes = None

        # Generate public key
        self.generate()

    def generate(self):

        # Generate public key
        self.key = self.private_key.key.public_key()

        return self

    def serialize(self, encoding=None):

        # Check encoding
        if encoding is None:
            encoding = self.encoding

        # Generate stream of bytes
        self.bytes = self.key.public_bytes(
            encoding=Encoding(encoding),
            format=PublicFormat.SubjectPublicKeyInfo,
        )

        return self

    def save(self, filename=None, encoding=None):

        # Check filename
        if filename is None:
            filename = self.filename

        # Check encoding
        if encoding is None:
            encoding = self.encoding

        # Convert the key to a stream of bytes
        self.serialize(encoding)

        # Write private key to a file
        with open(name=filename, mode='wb') as f:
            f.write(self.bytes)

        return self

    def load(self, filename=None, encoding=None):

        # Check filename
        if filename is None:
            filename = self.filename

        # Check encoding
        if encoding is None:
            encoding = self.encoding

        # Read stream of bytes
        with open(name=filename, mode='rb') as f:
            self.bytes = f.read()

        # Initialize deserialization method
        if Encoding(encoding) == Encoding.PEM:
            deserialize = load_pem_public_key
        else:
            deserialize = load_der_public_key

        # Deserialize the data
        self.key = deserialize(
            data=self.bytes
        )

        return self


class RsaPrivateKey(PrivateKey):

    def __init__(self,
                 size=2048,
                 encoding="DER",
                 filename="private.key",
                 hash_algorithm=hashes.SHA256()
                 ):

        super(RsaPrivateKey, self).__init__(encoding, filename)

        # Initialize logger
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.addHandler(logging.NullHandler())

        # Attributes
        self.size = size
        self.encoding = encoding.upper()
        self.filename = filename
        self.bytes = None
        self.hash_algorithm = hash_algorithm
        self.key = None

        # Generate key
        self.generate()

    def generate(self):

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.size
        )
        self.key = private_key

        return self

    def sign(self, data, hash_algorithm=None):

        # Check hasher
        if hash_algorithm is None:
            hash_algorithm = self.hash_algorithm

        # Calculate message digest
        hasher = hashes.Hash(algorithm=hash_algorithm)
        hasher.update(data)
        digest = hasher.finalize()

        # Sign the message digest
        signature = self.key.sign(
            data=digest,
            padding=padding.PSS(
                mgf=padding.MGF1(self.hash_algorithm),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            algorithm=utils.Prehashed(self.hash_algorithm)
        )

        return signature


class RsaPublicKey(PublicKey):

    def __init__(self, private_key):
        super(RsaPublicKey, self).__init__(private_key)

    def verify(self, signature, data):

        # Calculate message digest
        hasher = hashes.Hash(algorithm=self.hash_algorithm)
        hasher.update(data)
        digest = hasher.finalize()

        # Verify signature with public key
        self.key.verify(
            signature=signature,
            data=digest,
            padding=padding.PSS(
                mgf=padding.MGF1(self.hash_algorithm),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            algorithm=utils.Prehashed(self.hash_algorithm)
        )

        return True


class EcPrivateKey(PrivateKey):

    def __init__(self,
                 curve='secp256r1',
                 encoding="DER",
                 filename="private.key",
                 hash_algorithm=hashes.SHA256()
                 ):

        super(EcPrivateKey, self).__init__(encoding, filename)
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.addHandler(logging.NullHandler())

        # Get available curves and change keys to uppercase
        curves = vars(ec)
        self.curve = curves[curve.upper()]

        # Attributes
        self.encoding = encoding.upper()
        self.filename = filename
        self.hash_algorithm = hash_algorithm
        self.bytes = None
        self.key = None

        # Generate key
        self.generate()

    def generate(self):

        private_key = ec.generate_private_key(
            curve=self.curve()
        )
        self.key = private_key

        return self

    def sign(self, data, hash_algorithm=None):

        # Check hasher
        if hash_algorithm is None:
            hash_algorithm = self.hash_algorithm

        # Calculate message digest
        hasher = hashes.Hash(algorithm=hash_algorithm)
        hasher.update(data)
        digest = hasher.finalize()

        # Sign the message digest
        signature = self.key.sign(
            data=digest,
            signature_algorithm=ec.ECDSA(utils.Prehashed(self.hash_algorithm))
        )

        return signature


class EcPublicKey(PublicKey):

    def __init__(self, private_key):
        super(EcPublicKey, self).__init__(private_key)

    def verify(self, signature, data):

        # Calculate message digest
        hasher = hashes.Hash(algorithm=self.hash_algorithm)
        hasher.update(data)
        digest = hasher.finalize()

        # Verify signature with public key
        self.key.verify(
            signature=signature,
            data=digest,
            signature_algorithm=ec.ECDSA(utils.Prehashed(self.hash_algorithm))
        )

        return True


def rsakey(keysize=2048, SaveAs=None, encoding="DER", password=None):
    pk = RsaPrivateKey(size=keysize)
    if SaveAs:
        pk.save(filename=SaveAs, encoding=encoding, password=password)
    return pk


def eckey(curve='secp256r1', SaveAs=None, encoding="DER", password=None):
    pk = EcPrivateKey(curve=curve)
    if SaveAs:
        pk.save(filename=SaveAs, encoding=encoding, password=password)
    return pk


def test():

    # RSA
    private = RsaPrivateKey(size=2048, encoding="DER")
    private.save()
    expected = private.bytes
    private.load()
    obtained = private.bytes
    assert obtained == expected

    public = RsaPublicKey(private)
    public.save()
    expected = private.bytes
    public.load()
    obtained = private.bytes
    assert obtained == expected

    message = 'A'
    signature = private.sign(message)
    public.verify(signature, message)

    rsakey(SaveAs="test.rsa.key", encoding="PEM", password='1234')

    # Elliptic Curve
    private = EcPrivateKey()
    private.save()
    expected = private.bytes
    private.load()
    obtained = private.bytes
    assert obtained == expected

    public = EcPublicKey(private)
    public.save()
    expected = private.bytes
    public.load()
    obtained = private.bytes
    assert obtained == expected

    message = 'A'
    signature = private.sign(message)
    public.verify(signature, message)

    eckey(SaveAs="test.ec.key", encoding="PEM", password='1234')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test()
