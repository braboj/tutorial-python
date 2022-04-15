# coding: utf-8

from scapy.layers.tls.all import *
from scapy.automaton import *


class TestTlsAutomaton(TLSClientAutomaton):

    def __init__(self, resume=False, *args, **kargs):
        super(TestTlsAutomaton, self).__init__(*args, **kargs)
        self.resume = resume
        # self.advertised_tls_version = None
        self.session_id = None
        self.cur_session = None
        self.old_session = None

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
        p = self.buffer_in[0]
        if p.sid == self.session_id:
            raise self.RESUME_TLS_SESSION()
        else:
            self.session_id = p.sid

    @ATMT.state()
    def WAIT_CLIENTDATA(self):
        pass

    @ATMT.condition(WAIT_CLIENTDATA, prio=1)
    def add_ClientData(self):

        data = (self.data_to_send.pop()).strip('\r\n')

        if data in (b'reconnect', 'tcennocer'):
            raise self.RECONNECT()

        if data == b"quit":
            return

        if self.linebreak:
            data += b"\n"

        self.add_record()
        self.add_msg(TLSApplicationData(data=data))
        raise self.ADDED_CLIENTDATA()

    @ATMT.state()
    def RESUME_TLS_SESSION(self):
        self.add_record()
        self.add_msg(TLSChangeCipherSpec())
        raise self.ADDED_CHANGECIPHERSPEC()

    @ATMT.state()
    def RECONNECT(self):
        self.old_session = self.cur_session

        self.cur_session = tlsSession(connection_end="client")
        self.cur_session.sid = self.session_id

        self.cur_session.client_kx_ffdh_params = self.old_session.client_kx_ffdh_params
        self.cur_session.client_kx_privkey = self.old_session.client_kx_privkey

        self.cur_session.client_certs = self.mycert
        self.cur_session.client_key = self.mykey

        self.cur_session.server_certs = self.old_session.server_certs
        self.cur_session.server_key = self.old_session.server_key

        self.cur_session.advertised_tls_version = self.old_session.advertised_tls_version

        raise self.CONNECT()


t = TestTlsAutomaton(server='192.168.210.240',
                     dport=4433,
                     server_name=None,
                     mycert="./pki/cli_cert.pem",
                     mykey="./pki/cli_key.pem",
                     data=['reconnect', 'quit'],
                     resume=True,
                     )

t.run()
