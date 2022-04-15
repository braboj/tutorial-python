from cryptography.x509 import *
import logging


class Certificate(CertificateBuilder):

    def __init__(self,
                 subject,
                 issuer,
                 key,
                 valid_from, valid_to, extensions):

        super(Certificate, self).__init__()
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.addHandler(logging.NullHandler())

        self.subject = subject
        self.issuer = issuer
        self.key = key
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.extensions = extensions

    def request(self):
        pass

    def to_bytes(self):
        pass

    def from_bytes(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    def verify(self):
        pass

    def report(self):
        pass


if __name__ == "__main__":
    pass
