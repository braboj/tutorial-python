import base64
import json


def dict_to_bytes(data):
    """ Convert dictionary to bytes """

    data_str = str(data).encode('ascii')
    test_data_bytes = base64.b64encode(data_str)

    return test_data_bytes


def bytes_to_dict(data):
    """ Convert bytes to dictionary """

    data_loaded = base64.b64decode(data)  # Decode from Base64
    data_str = data_loaded.decode("ascii")
    temp_dict = data_str.replace("'", "\"")  # Prepare to convert string dict to dict
    result = json.loads(temp_dict)

    return result


def bin_len_string(data):
    """ Calculates tree(dictionary) length and shape it in 4 bytes BIN string. """

    dict_len = len(data)  # Dictionary length
    result = dict_len.to_bytes(length=4, byteorder="big")

    return result


def hex_to_bin(data):
    """ Converts HEX data string to BIN format. """

    bit_string = ""
    for byte in data:
        byte = bin(byte)
        bit_string += byte

    bit_string_final = ""
    bit_string_split = bit_string.split("0b")
    for i in range(1, len(bit_string_split)):
        if len(bit_string_split[i]) != 8:
            to_add = 8 - len(bit_string_split[i])
            bit_string_split[i] = to_add * "0" + bit_string_split[i]
        bit_string_final += bit_string_split[i]

    return bit_string_final
