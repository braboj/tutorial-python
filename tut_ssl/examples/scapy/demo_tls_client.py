from scapy.layers.tls.handshake import TLSClientHello
from scapy.layers.tls.automaton_cli import TLSClientAutomaton

ch = TLSClientHello(ciphers=0x01)
t = TLSClientAutomaton(server='172.20.10.114', dport=10023, client_hello=ch)
t.run()