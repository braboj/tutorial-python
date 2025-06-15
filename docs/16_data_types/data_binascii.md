# data_binascii

```python
# Binary-to-ASCII conversions
# -----------------------------------------------------------------------------
# The binascii module exposes low-level routines for converting between binary data and various ASCII encodings.


import binascii


def test_base64():

    print("Test Base64")

    # Convert the string to bytes
    text_out = 'Здравейте, хора!'
    text_stream = text_out.encode('utf-8')
    print(text_out)

    # Encode the byte stream in Base64
    encoded = binascii.b2a_base64(text_stream)
    print(encoded)

    # Decode the byte stream from Base64
    decoded = binascii.a2b_base64(encoded)
    print(decoded)

    # Print the decoded string
    text_in = decoded.decode('utf-8')
    print(text_in)

    # Assert that the expected and obtained strings are equal
    assert text_in == text_out

    print()


def test_hex():

    print("Test Hex")

    # Convert the string to bytes
    text_out = 'Здравейте, хора!'
    text_stream = text_out.encode('utf-8')
    print(text_out)

    # Encode the byte stream in hexadecimal
    encoded = binascii.b2a_hex(text_stream)
    print(encoded)

    # Decode the byte stream from hexadecimal
    decoded = binascii.a2b_hex(encoded)
    print(decoded)

    # Print the decoded string
    text_in = decoded.decode('utf-8')
    print(text_in)

    # Assert that the expected and obtained strings are equal
    assert text_in == text_out

    print()


def test_uu():

    print("Test UUEncode")

    # Convert the string to bytes
    text_out = 'Здравейте, хора!'
    text_stream = text_out.encode('utf-8')
    print(text_out)

    # Encode the byte stream in uuencode
    encoded = binascii.b2a_uu(text_stream)
    print(encoded)

    # Decode the byte stream from uuencode
    decoded = binascii.a2b_uu(encoded)
    print(decoded)

    # Print the decoded string
    text_in = decoded.decode('utf-8')
    print(text_in)

    # Assert that the expected and obtained strings are equal
    assert text_in == text_out

    print()


if __name__ == "__main__":
    test_base64()
    test_hex()
    test_uu()
```
