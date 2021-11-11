# coding: utf-8

from scapy.layers.tls.all import *
from scapy.automaton import *


class MyTlsClientAutomaton(TLSClientAutomaton):

    def __init__(self, resume=False, *args, **kargs):
        super(MyTlsClientAutomaton, self).__init__(*args, **kargs)
        self.resume = resume
        self.session_id = None

    @ATMT.state()
    def PREPARE_CLIENTFLIGHT1(self):
        self.add_record()

    @ATMT.condition(PREPARE_CLIENTFLIGHT1)
    def should_add_ClientHello(self):

        # Disable sesssion tickets
        p = TLSClientHello(
            sidlen=0,
            ext=[TLS_Ext_SessionTicket(len=0)]
        )

        # Use stored Session-ID
        if self.resume and self.session_id is not None:
            p.sidlen = len(self.session_id)
            p.sid = self.session_id

        # Add TLS_Ext_SignatureAlgorithms for TLS 1.2 ClientHello
        if self.cur_session.advertised_tls_version == 0x0303:
            p.ext += [TLS_Ext_SignatureAlgorithms(sig_algs=["sha256+rsa"])]

        # Add TLS_Ext_ServerName
        if self.server_name:
            p.ext += TLS_Ext_ServerName(
                servernames=[ServerName(servername=self.server_name)]
            )

        # Add the Hello Message to the TLS RECORD
        self.add_msg(p)
        raise self.ADDED_CLIENTHELLO()

    @ATMT.state()
    def RECEIVED_SERVERFLIGHT1(self):
        self.session_id = self.buffer_in[0].sid


t = MyTlsClientAutomaton(server='192.168.210.240',
                         dport=4433,
                         server_name=None,
                         mycert="./pki/cli_cert.pem",
                         mykey="./pki/cli_key.pem",
                         data=['hello', 'quit'],
                         resume=True,
                         )

t.run()
