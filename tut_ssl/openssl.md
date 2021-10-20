# Digital Security with SSL/TLS

## OpenSSL

### Select Ciphers

    Operators
        +   : Logical AND
        :   : Logical OR

        > openssl ciphers -V 'kRSA+aRSA'
        > openssl ciphers -V 'aNULL+eNULL'
        > openssl ciphers -V 'SSLv3:TLSv1'

    Prefixes

        k   : Prefix to select ciphers with specific key exchange
        a   : Prefix to select ciphers with specific authentication
        e   : Prefix to select ciphers with specific encoding
        !   : Prefix to delete ciphers from the list permanently
        -   : Prefix to delete ciphers from the list temporarily
        +   : Prefix to add ciphers to the end of the list

        # Ciphers with Kx=RSA and Au=RSA with any encoding
        > openssl ciphers -V 'kRSA+aRSA'

        # Ciphers with Kx=RSA and Au=RSA with any encoding except None
        > openssl ciphers -V 'kRSA+aRSA:!eNULL'

    Names

        NULL                : None
        DEFAULT             : Default cipher suites
        ALL                 : All cipher suites except eNULL
        HIGH                : High security
        MEDIUM              : Medium security
        LOW                 : Low security
        COMPLEMENTOFALL     : Everything outside 'ALL'
        COMPLEMENTOFDEFAULT : Everything outside 'DEFAULT'

    Sorting

        > openssl ciphers -V 'kRSA+aRSA:@STRENGTH'

    Examples

        # Select cipher suites which use RSA for key exchange
        > openssl ciphers -V 'kRSA'
    
        # Select cipher suites which use RSA for authentication
        > openssl ciphers -V 'aRSA'
    
        # Select cipher suites with no encryption
        > openssl ciphers -V 'eNULL'
    
        # Select cipher suites with AES encryption
        > openssl ciphers - V 'AES'

## Python

### OpenSSL Wrapper

    ssl.wrap_socket()               : Create ad-hock encrypted socket
    ssl.create_default_context()    : Create a pre-configured SSL context
    ssl.match_hostname()            : Match a hostname with the one in the peer's certificate
    ssl.cert_time_to_seconds()      : Converts a date to a time in seconds since the Epoch (01.01.1970 00:00:00)
    ssl.get_server_certificate()    : Get server certificate in PEM format
    ssl.get_default_verify_paths()  : 
    
    
    SSLSocket
    --------------------------------------------------------------------------------------------------
    .do_handshake                   : Perform TLS handshake manually
    .getpeercert                    : Get the decrypted certificate of the peer host
    .cipher                         : Get the cipher suite used for data encryption
    .compresssion                   : Get the compression method
    .get_channel_binding            : ???
    .selected_alpn_protocol         :	
    .selected_npn_protocol          :
    .unwrap                         : Remove the encryption from the socket
    .version                        : 
    .context                        : The TLS configuration context of the socket
    
    SSLContext
    --------------------------------------------------------------------------------------------------
    .cert_store_stats               : 
    .load_cert_chain                : Array of certificates and keys for the device
    .load_default_certs             : Load default certificates (OS dependent)
    .load_verify_locations          : Files used to verify the certificate of the partner
    .get_ca_certs                   : Get the certtificates of certificate authorities	
    .set_default_verify_paths       : Set default paths for certificate verification
    .set_ciphers                    : Set cipher suites to be used by the device
    .set_alpn_protocols             : ??? 
    .set_npn_protocols              : ???
    .set_servername_callback        : ???
    .load_dh_parameters             : Diffie-Hellman parameters
    .set_ecdh_curve                 : Set curve name for the Elliptic Curve-based Diffie-Hellman
    .wrap_socket                    : Encrypt socket
    .session_stats                  : Get session statistics
    .check_hostname                 : Flag to for the client checks the server name in the handshake process with "match_hostname"
    .options                        : Set options by using OR and reset them by using AND
    .protocol                       : SSL/TLS protocol version
    .verify_flags                   : Certificate verification control flags
    .verify_mode                    : Certificate verification mode (none, optional, required)

### Scapy
    automaton_cli.py, automaton_srv.py
    cert.py, x509.py

### Certificates
    criptograpy
