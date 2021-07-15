import Crypto.Util.number as number

test = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

flag = number.long_to_bytes(test)
flag.encode(encoding="ascii")
print(flag)

message = flag
test = number.bytes_to_long(message)
print(test)

message = u'0x667265656c616e63655f737562737469747574655f646f64'
data = int(message, base=16)
test = number.long_to_bytes(data)
print(message)
