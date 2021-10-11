from scapy.config import conf
import select

s = conf.L2listen()
rlist = select.select([s], [], [])
if rlist:
    p = s.recv()
    print(p.summary())
s.close()