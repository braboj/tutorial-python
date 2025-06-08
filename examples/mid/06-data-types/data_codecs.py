# Example: codecs module

import codecs
import pprint


def test_utf8():

    print("Test UTF-8")

    text = 'Здравейте, хора!'
    print(text)

    encoded = codecs.encode(text, 'utf-8')
    print(encoded)

    decoded = codecs.decode(encoded, 'utf-8')
    print(decoded)

    info = codecs.lookup('utf-8')
    print("lookup() -> ", info)

    print()


def test_utf16():

    print("Test UTF-16")

    text = 'Здравейте, хора!'
    print(text)

    encoded = codecs.encode(text, 'utf-16')
    print(encoded)

    decoded = codecs.decode(encoded, 'utf-16')
    print(decoded)

    info = codecs.lookup('utf-16')
    print("lookup() -> ", info)

    print()


def test_base64():

    print("Test Base64")

    text = 'Здравейте, хора!'
    print(text)

    encoded = codecs.encode(text.encode('utf-8'), 'base64')
    print(encoded)

    decoded = codecs.decode(encoded, 'base64')
    print(decoded.decode('utf-8'))

    info = codecs.lookup('base64')
    print("lookup() -> ", info)

    print()


if __name__ == "__main__":

    test_utf8()
    test_utf16()
    test_base64()

