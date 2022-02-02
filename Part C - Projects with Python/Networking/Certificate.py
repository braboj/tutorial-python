from HilscherFramework.Utils.Log import getLogger
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

        cert = self.subject_name(
           self.subject
        ).issuer_name(
            self.issuer
        ).public_key(
            self.key.public_key()
        ).serial_number(
            self.random_serial_number()
        ).not_valid_before(
            self.datetime.datetime.utcnow()
        ).not_valid_after(
            # Our certificate will be valid for 10 days
            datetime.datetime.utcnow() + datetime.timedelta(days=10)
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
            critical=False,
            # Sign our certificate with our private key
        ).sign(key, hashes.SHA256())


        self.config(**kwargs)

    def config(self, **kwargs):

        for key, value in kwargs.items():

            if key == u"host_addr":
                self.host_addr = kwargs[key]

            elif key == "host_port":
                self.host_port = kwargs[key]

            elif key == u"conn_timeout":
                self.conn_timeout = kwargs[key]

            elif key == u"conn_limit":
                self.conn_limit = kwargs[key]

            elif key == u"session_class":
                self.session_class = kwargs[key]

            elif key == u"secure_flag":
                self.secure_flag = kwargs[key]

    def request(self):

        # Distinguished names of subject
        CommonName = SDN.get('CommonName')
        OrganizationName = SDN.get('OrganizationName')
        OrganizationUnit = SDN.get('OrganizationUnit')
        LocalityName = SDN.get('LocalityName')
        StateName = SDN.get('StateName')
        CountryID = SDN.get('CountryID')
        Email = SDN.get('Email')
        SerialNumber = SDN.get('SerialNumber')

        # Distinguished names
        DN = []
        if CommonName:
            DN.append(x509.NameAttribute(NameOID.COMMON_NAME, CommonName.decode("utf-8")))
        if CountryID:
            DN.append(x509.NameAttribute(NameOID.COUNTRY_NAME, CountryID.decode("utf-8")))
        if OrganizationName:
            DN.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, OrganizationName.decode("utf-8")))
        if OrganizationUnit:
            DN.append(x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, OrganizationUnit.decode("utf-8")))
        if StateName:
            DN.append(x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, StateName.decode("utf-8")))
        if LocalityName:
            DN.append(x509.NameAttribute(NameOID.LOCALITY_NAME, LocalityName.decode("utf-8")))
        if SerialNumber:
            DN.append(x509.NameAttribute(NameOID.SERIAL_NUMBER, SerialNumber.decode("utf-8")))
        if Email:
            DN.append(x509.NameAttribute(NameOID.EMAIL_ADDRESS, Email.decode("utf-8")))

        DN = x509.Name(DN)

        CSR = x509.CertificateSigningRequestBuilder().subject_name(DN).sign(PK, hashes.SHA256(), default_backend())

        if SaveAs is not None:
            with open(SaveAs, "wb") as f:
                f.write(CSR.public_bytes(Encoding("PEM")))
        return CSR

    def serialize(self):
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
    logger = getLogger('Certificates')
    pass
