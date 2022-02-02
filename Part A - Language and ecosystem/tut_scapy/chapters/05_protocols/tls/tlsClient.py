# coding: utf-8

from scapy.layers.tls.all import *

ciphersuite = [TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, ]
ch = TLSClientHello(ciphers=ciphersuite)

t = TLSClientAutomaton(server='192.168.210.240',
                       dport=4433,
                       server_name=None,
                       client_hello=ch,
                       # version='tlsv12',
                       mycert="./pki/cli_cert.pem",
                       mykey="./pki/cli_key.pem",
                       data=['hello', 'quit'],
                       )

t.run()
