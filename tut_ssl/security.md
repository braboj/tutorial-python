# Tutorial TLS and PKI

## OpenSSL
______________________________________________________________________________

### Secure Client Simulation

    openssl s_client 
        -cert ... 
        -key ...
        -connect host:port          : 
        -showcerts                  : 
        -no_ticket                  :
        -sess_in ...                :
        -sess_out ...               :

### Secure Server Simulation

    openssl s_server
        -accept     ...             : ???
        -port       ...             : Port to listen to
        -verify     ...             : Verification depth of the certificate chain
        -cert       ...             : File for the server certificate
        -cert_chain ...             :
        -CAfile
        -CApath
        -cert_form  ...             : DER or PEM
        -key        ...             : File for the private key
        -key_form   ...             : DER or PEM
        -debug
        -msg
        -state
        -[ssl2, tls1_2, no_ssl2...] : Select specific protocol version
        -no_ticket
        -no_resumption_on_reneg
        -cipher
        -ciphersuites


### Generate Keys

    # Generate private key
    openssl genrsa 
        -out private_key.pem 
        1024
    
    # Generate public key
    openssl rsa 
        -in private_key.pem 
        -out public_key.pem 
        -pubout 
        -outform PEM

### Generate Certificates

    # Create a self-signed certificate
    openssl req 
        -new 
        -x509 
        -days 3650 
        -key private_key.pem 
        -out ca_cert.pem 
        -sha256
    
    # Create a new certificate signature request
    openssl req 
        -new 
        -out device_cert.csr 
        -key private_key.pem 
        -sha256

### Sign Certificates

    # Sign a certificate request
    openssl x509 
        -req -in device_csr.pem 
        -CA ca_cert.pem 
        -CAkey private_key.pem 
        -CAcreateserial
        -out device_cert.pem 
        -days 3650 
        -sha256
        

### Convert Formats

    openssl x509 -inform pem -in Certificate.pem -outform der -out Certificate.der
    openssl rsa -inform pem -in PrivateKey.pem -outform der -out PrivateKey.der

### Ciphers
    
```
openssl ciphers
    -[ssl3, tls1, ... , tls1_3]     : Ciphers used for negotiation
    -v                              : Verbose with openssl names 
    -V                              : Verbose with official names
```

### Cipher Strings

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
______________________________________________________________________________

### ssl

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

### scapy
    automaton_cli.py, automaton_srv.py
    cert.py, x509.py

### cryptography
    criptograpy
