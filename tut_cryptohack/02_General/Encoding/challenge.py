import telnetlib
import json
import base64
import codecs
import Crypto.Util.number as number

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")


def json_recv():
    line = readline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


decoded = None
for level in range(100):

    received = json_recv()
    codec = received["type"]
    data = received["encoded"]

    if received["type"] == "base64":
        decoded = data.decode(encoding="base64")

    elif received["type"] == "hex":
        decoded = data.decode(encoding="hex")

    elif received["type"] == "bigint":
        decoded = number.long_to_bytes(int(data, base=16))

    elif received["type"] == "utf-8":
        decoded = "".join((chr(x) for x in data))

    elif received["type"] == "rot13":
        decoded = codecs.decode(data, "rot_13")

    else:
        raise Exception("Unknown encoding type")

    print(level, codec, decoded)
    to_send = {"decoded": decoded}
    json_send(to_send)

# Print flag from server
flag = json_recv()
print(flag)
