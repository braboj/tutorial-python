# coding: utf-8
from scapy.layers.tls.automaton_srv import TLSServerAutomaton

t = TLSServerAutomaton(server='192.168.210.240',
                       sport=4433,
                       mycert='./pki/srv_cert.pem',
                       mykey='./pki/srv_key.pem',
                       preferred_ciphersuite=None,
                       client_auth=None,
                       is_echo_server=True,
                       max_client_idle_time=60,
                       handle_session_ticket=None,
                       session_ticket_file=None,
                       curve=None,
                       cookie=None,
                       psk=None,
                       psk_mode=None,
                       debug=5)


t.run()
