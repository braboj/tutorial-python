# coding: utf-8

from scapy.layers.tls.automaton_cli import TLSClientAutomaton
from scapy.layers.tls.handshake import TLSClientHello, TLS13ClientHello
from scapy.layers.tls.handshake_sslv2 import SSLv2ClientHello
from scapy.layers.tls.crypto.suites import *
from cryptography.x509 import Certificate
from scapy.automaton import Message

# ciphersuite = [TLS_RSA_WITH_RC4_128_MD5, ]
# ch = SSLv2ClientHello(ciphers=ciphersuite)
# ch = TLSClientHello(ciphers=ciphersuite)
# ch = TLS13ClientHello(ciphers=ciphersuite)


t = TLSClientAutomaton(server='192.168.210.240',
                       dport=4433,
                       server_name=None,
                       # client_hello=ch,
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

t.cmdin.r(t.INITIAL)
t.cmdin.send(t.INIT_TLS_SESSION)
t.cmdin.send(t.CONNECT)
t.cmdin.send(t.PREPARE_CLIENTFLIGHT1)
t.cmdin.send(t.SENT_CLIENTFLIGHT1)