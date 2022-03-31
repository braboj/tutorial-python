# coding: utf-8
import time

from scapy.layers.tls.automaton_cli import TLSClientAutomaton
from scapy.layers.tls.handshake import TLSClientHello, TLS13ClientHello
from scapy.layers.tls.handshake_sslv2 import SSLv2ClientHello
from scapy.layers.tls.crypto.suites import *
from cryptography.x509 import Certificate
from scapy.automaton import Message

ciphersuite = [TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, ]
# ch = SSLv2ClientHello(ciphers=ciphersuite)
ch = TLSClientHello(ciphers=ciphersuite)
# ch = TLS13ClientHello(ciphers=ciphersuite)


t = TLSClientAutomaton(server='192.168.210.240',
                       dport=4433,
                       server_name=None,
                       client_hello=ch,
                       mycert="./pki/cli_cert.pem",
                       mykey="./pki/cli_key.pem",
                       version='sslv3',
                       # resumption_master_secret=None,
                       # session_ticket_file_in=None,
                       # session_ticket_file_out=None,
                       # psk=None,
                       # psk_mode=None,
                       # ciphersuite=None,
                       # curve=None
                       data='quit',
                       )

t.run()