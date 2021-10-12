# OpenSSL

## Creating Filters

### Intersection

    > openssl ciphers -V 'RSA+AES+SHA'

### Union
    > openssl ciphers -V 'aNULL:eNULL'

### Complement
    > openssl ciphers -V 'aNULL:!eNULL'
    > openssl ciphers -V 'COMPLEMENTOFALL'
    > openssl ciphers -V 'COMPLEMENTOFDEFAULT'

### Other list operations

    -   : Delete temporary ciphers from the list
    +   : Add ciphers to the end of the list

## Predefined Filters

    eNULL           : Encoding None
    aNULL           : Authentication None
    ALL             : All cipher suites except the eNULL
    COMPLEMENTOFALL : Complement of 'ALL'
    HIGH            : High security
    MEDIUM          : Medium security
    LOW             : Low security
    kRSA            : Ciphersuites with RSA key exchange
    aRSA            : Ciphersuites using RSA authentication

## Sorting

    openssl ciphers -V 'ALL:eNULL:@STRENGTH'
    