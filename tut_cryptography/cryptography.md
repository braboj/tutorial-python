# Cryptography

## Overview
__________________________________________________________________________________________________
Digital communication is the process of sending and receiving data over public infrastructures like the Internet. 
The majority of the early protocols like HTTP and SMTP send data in plaintext. In order to transfer data in a more 
secure way, several problems must be addressed:

| Problem                                     | Solution              | Description                                       | Examples  |
|---------------------------------------------|-----------------------|---------------------------------------------------|-----------|
| How to obfuscate the data?                  | Encryption            | Symmetric and asymmetric ciphers                  | AES, RSA  |
| How to verify the communication partner?    | Authentication        | Digital Signature                                 | RSA, MAC  |
| How to protect the data from tampering?     | Data Integrity        | Hash Functions                                    | MD5, SHA2 |
| How to exchange the shared secret?          | Key Exchange          | Key exchange algorithms                           | DH, RSA   |
| How to store and distribute encrypted data? | Infrastructure        | Standards for certificate format and trust models | X509, PGP |


## Mathematical Blocks
__________________________________________________________________________________________________

### XOR
TODO

### Random Numbers
TODO

### Modular Arithmetic
The modulo operator is defined as the remainder of the integer division of two numbers a and b. Mathematically this 
is defined in the following way:

    а mod b = r
    a = b * q + r

Some definitions allow r to be negative (Truncation, Knuth), some define r as only positive (Euclidian, Flooring). 
In the scope of the document r will be defined to be always positive.

#### Algorithm

    1. Calculate q = truncate(a/b)
    2. Calculate r = b * q - a 
    3. If r < 0 then r = b - r

    Example:

        > +1 mod 12   → q = 0, r = 1
        > -3 mod 12   → q = 0, r = -3 → r = 12 - 3 → r = 9
        > +3 mod -12  → q  =0, r = 3
        > -17 mod 10  → q = -1 → r = -7 → r = 10 - 7 → r = 3
        > +17 mod -10 → q = -1 → r = 7

#### Congruence

    A ≡ B (mod C)
    A mod C = B mod C
    A - B = K * C

    Example:

        > 14 ≡ 2 (mod 12) → Equivalent or congruent for modulo 12
        > 14 mod 12 = 2   → 12 + 0 
        > 2 mod 12 = 2    → 0 + 12

#### Arithmetic

    Addition : (A + B) mod C = (A mod C + B mod C) mod C
    Subtraction : (A - B) mod C = (A mod C - B mod C) mod C
    Multiplication : (A * B) mod C = (A mod C * B mod C) mod C
    Exponentiation : A^B mod C = ( (A mod C) ^ B ) mod C

#### References
* https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
* https://www.omnicalculator.com/math/modulo#what-are-modulo-operations



### Elliptic Curves
Elliptic curves are a repeted intersections on a special type of mathematical functions which allow to generate keys 
with high secruity with smaller key size. For example an EC key of length 224 bits has the same security as a RSA 
key of length 2048 bits. The smaller footprint is especially useful for embedded devices.

#### Definition

    1. y^2 = x^3 + ax + b
    2. 4a^3 + 27b^2 != 0


#### References
* https://www.keycdn.com/support/elliptic-curve-cryptography
* https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/
* https://www.youtube.com/watch?v=NF1pwjL9-DE
* https://www.youtube.com/watch?v=dCvB-mhkT0w


## Hash Functions
__________________________________________________________________________________________________
MD5, SHA1, SHA2

### Key Derivation Functions

In cryptography we often use passwords instead of binary keys, because passwords are easier to remember, to write 
down and can be shorter. When a certain algorithm needs a key (e.g. for encryption or for digital signing) a key 
derivation function (password -> key) is needed.

* PDKDF2
* BCrypt
* SCrypt
* Argon2

By design secure key derivation functions use salt (random number, which is different for each key derivation) and 
many iterations (to speed-down eventual password guessing process). This is a process, known as key stretching.


### Pseudorandom Function
TODO


## Symmetric Cryptography
__________________________________________________________________________________________________
Encryption, MAC

### Stream Ciphers
### Block Ciphers

## Asymmetric Cryptography
__________________________________________________________________________________________________
Key Exchange, Digital Signature

### Key Exchange
RSA, DH, DHE, ECDHE

### Digital Signature
RSA, DSA

## Infrastructure
__________________________________________________________________________________________________
X509, PGP

#### ASN.1
Abstract Syntax Notation One

#### X509
ANS.1 structure

    Certificate
        Version Number
        Issuer Name
        Subject name
        Validity period
            Not Before
            Not After
        Serial Number
    
        Signature Algorithm ID
        Subject Public Key Info
            Public Key Algorithm
            Subject Public Key
    
        Issuer Unique Identifier (optional)
        Subject Unique Identifier (optional)
        Extensions (optional)
            ...
        Certificate Signature Algorithm
        Certificate Signature

#### X609
BER, CER, DER

#### PKCS
Public-Key Cryptography Standards

* PKCS 1: Implementation of RSA algorithm
* PKCS 2: Implementation of DH
* PKCS 5: Password based encryption
* PKCS 7: Cryptographic Message Standard
* PKCS 8: Private Key Information Syntax Standard

#### PEM
Privacy-Enhanced Mail
Base64 encoding
Solves the problem of transfering binary data using only ASCII symbols.

      -----BEGIN PRIVATE KEY-----
      MIIBVgIBADANBgkqhkiG9w0BAQEFAASCAUAwggE8AgEAAkEAq7BFUpkGp3+LQmlQ
      Yx2eqzDV+xeG8kx/sQFV18S5JhzGeIJNA72wSeukEPojtqUyX2J0CciPBh7eqclQ
      2zpAswIDAQABAkAgisq4+zRdrzkwH1ITV1vpytnkO/NiHcnePQiOW0VUybPyHoGM
      /jf75C5xET7ZQpBe5kx5VHsPZj0CBb3b+wSRAiEA2mPWCBytosIU/ODRfq6EiV04
      lt6waE7I2uSPqIC20LcCIQDJQYIHQII+3YaPqyhGgqMexuuuGx+lDKD6/Fu/JwPb
      5QIhAKthiYcYKlL9h8bjDsQhZDUACPasjzdsDEdq8inDyLOFAiEAmCr/tZwA3qeA
      ZoBzI10DGPIuoKXBd3nk/eBxPkaxlEECIQCNymjsoI7GldtujVnr1qT+3yedLfHK
      srDVjIT3LsvTqw==
      -----END PRIVATE KEY-----

      -----BEGIN ENCRYPTED PRIVATE KEY-----
      MIIBrzBJBgkqhkiG9w0BBQ0wPDAbBgkqhkiG9w0BBQwwDgQImQO8S8BJYNACAggA
      MB0GCWCGSAFlAwQBKgQQ398SY1Y6moXTJCO0PSahKgSCAWDeobyqIkAb9XmxjMmi
      hABtlIJBsybBymdIrtPjtRBTmz+ga40KFNfKgTrtHO/3qf0wSHpWmKlQotRh6Ufk
      0VBh4QjbcNFQLzqJqblW4E3v853PK1G4OpQNpFLDLaPZLIyzxWOom9c9GXNm+ddG
      LbdeQRsPoolIdL61lYB505K/SXJCpemb1RCHO/dzsp/kRyLMQNsWiaJABkSyskcr
      eDJBZWOGQ/WJKl1CMHC8XgjqvmpXXas47G5sMSgFs+NUqVSkMSrsWMa+XkH/oT/x
      P8ze1v0RDu0AIqaxdZhZ389h09BKFvCAFnLKK0tadIRkZHtNahVWnFUks5EP3C1k
      2cQQtWBkaZnRrEkB3H0/ty++WB0owHe7Pd9GKSnTMIo8gmQzT2dfZP3+flUFHTBs
      RZ9L8UWp2zt5hNDtc82hyNs70SETaSsaiygYNbBGlVAWVR9Mp8SMNYr1kdeGRgc3
      7r5E
      -----END ENCRYPTED PRIVATE KEY-----