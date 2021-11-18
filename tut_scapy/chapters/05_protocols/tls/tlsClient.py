# coding: utf-8

from scapy.layers.tls.all import *

t = TLSClientAutomaton(server='192.168.210.240',
                       dport=4433,
                       server_name=None,
                       mycert="./pki/cli_cert.pem",
                       mykey="./pki/cli_key.pem",
                       data=['hello', 'quit'],
                       )

t.run()
