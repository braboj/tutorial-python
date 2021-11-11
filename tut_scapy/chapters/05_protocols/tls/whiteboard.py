# coding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

import threading
from contextlib import contextmanager
import sys
from scapy.autorun import StringWriter
from scapy.layers.tls.all import *
from Queue import Queue
import re


@contextmanager
def captured_output():
    old_out, old_err = sys.stdout, sys.stderr
    new_out, new_err = StringWriter(debug=old_out), StringWriter(debug=old_out)
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def check_output_for_data(out, err, expected_data):
    errored = err.s.strip()
    if errored:
        return False, errored
    output = out.s.strip()
    if expected_data:
        expected_data = str(expected_data)
        print("Testing for output: '%s'" % expected_data)
        p = re.compile(r"> Received: b?'([^']*)'")
        for s in p.finditer(output):
            if s:
                data = s.group(1)
                print("Found: %s" % data)
                if expected_data in data:
                    return (True, data)
        return False, output
    else:
        return False, None


def run_tls_test_server(expected_data, q, curve=None, cookie=False, client_auth=False,
                        psk=None, handle_session_ticket=False):
    correct = False
    print("Server started !")
    with captured_output() as (out, err):
        # Prepare automaton
        mycert = "./pki/cli_cert.pem"
        mykey = "./pki/cli_key.pem"
        print(mykey)
        print(mycert)
        assert os.path.exists(mycert)
        assert os.path.exists(mykey)
        kwargs = dict()
        if psk:
            kwargs["psk"] = psk
            kwargs["psk_mode"] = "psk_dhe_ke"
        t = TLSServerAutomaton(mycert=mycert,
                               mykey=mykey,
                               curve=curve,
                               cookie=cookie,
                               client_auth=client_auth,
                               handle_session_ticket=handle_session_ticket,
                               debug=5,
                               **kwargs)
        # Sync threads
        q.put(True)
        # Run server automaton
        t.run()
        # Return correct answer
        res = check_output_for_data(out, err, expected_data)
    # Return data
    q.put(res)


def run_tls_test_client(send_data=None, cipher_suite_code=None, version=None,
                        client_auth=False, key_update=False, stop_server=True,
                        session_ticket_file_out=None, session_ticket_file_in=None):
    print("Loading client...")
    mycert = "./pki/cli_cert.pem" if client_auth else None
    mykey = "./pki/cli_key.pem" if client_auth else None
    commands = [send_data]
    if key_update:
        commands.append(b"key_update")
    if stop_server:
        commands.append(b"stop_server")
    if session_ticket_file_out:
        commands.append(b"wait")
    commands.append(b"quit")
    if version == "0002":
        t = TLSClientAutomaton(data=commands, version="sslv2", debug=5, mycert=mycert, mykey=mykey,
                               session_ticket_file_in=session_ticket_file_in,
                               session_ticket_file_out=session_ticket_file_out)
    elif version == "0304":
        ch = TLS13ClientHello(ciphers=int(cipher_suite_code, 16))
        t = TLSClientAutomaton(client_hello=ch, data=commands, version="tls13", debug=5, mycert=mycert, mykey=mykey,
                               session_ticket_file_in=session_ticket_file_in,
                               session_ticket_file_out=session_ticket_file_out)
    else:
        ch = TLSClientHello(version=int(version, 16), ciphers=int(cipher_suite_code, 16))
        t = TLSClientAutomaton(client_hello=ch, data=commands, debug=5, mycert=mycert, mykey=mykey,
                               resumption_master_secret=True,
                               session_ticket_file_in=session_ticket_file_in,
                               session_ticket_file_out=session_ticket_file_out)
    print("Running client...")
    t.run()


def test_tls_client(suite, version, curve=None, cookie=False, client_auth=False,
                    key_update=False, sess_in_out=False):
    msg = ("TestC_%s_data" % suite).encode()
    # Run server
    q_ = Queue()
    print("Starting server...")
    th_ = threading.Thread(target=run_tls_test_server, args=(msg, q_),
                           kwargs={"curve": None, "cookie": False, "client_auth": client_auth,
                                   "handle_session_ticket": sess_in_out},
                           name="test_tls_client %s %s" % (suite, version))
    th_.setDaemon(True)
    th_.start()
    # Synchronise threads
    print("Syncrhonising...")
    assert q_.get(timeout=5) is True
    time.sleep(1)
    print("Thread synchronised")

    # Run client
    if sess_in_out:
        file_sess = "./session"
        run_tls_test_client(msg, suite, version, client_auth, key_update, stop_server=False)
        run_tls_test_client(msg, suite, version, client_auth, key_update, stop_server=True)
    else:
        run_tls_test_client(msg, suite, version, client_auth, key_update)

    # Wait for server
    print("Client running, waiting...")
    th_.join(5)
    if th_.is_alive():
        raise RuntimeError("Test timed out")
    # Return values
    if q_.empty():
        raise RuntimeError("Missing return value")
    ret = q_.get(timeout=5)
    print(ret)
    assert ret[0]


test_tls_client("009e", "0303", client_auth=True, sess_in_out=True)
