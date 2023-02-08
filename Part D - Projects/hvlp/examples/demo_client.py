from components.broker import *
from components.client import *
from components.packets import *
from components.errors import *

import threading
import time


###################################################################################################

def producer():
    test_client = HvlpClient()
    test_client.open()
    test_client.connect()
    test_client.subscribe('a')

    for i in range(256):
        test_client.publish('a', i)
        logging.info('PUBLISH')


###################################################################################################

def consumer(stop):
    test_client = HvlpClient()

    test_client.open()
    test_client.connect()
    test_client.subscribe('a')

    t = threading.Thread(target=test_client.listen, args=(stop,))
    t.start()

    while not stop.is_set():
        try:
            packet = Packet.from_bytes(test_client.stream_in)
            test_client.stream_in = test_client.stream_in[len(packet):]
            logging.info(packet)
        except HvlpParsingError:
            pass


###################################################################################################

logging.basicConfig(format=b'%(asctime)s - %(funcName)-25s: %(message)s', level=logging.INFO)

broker = HvlpBroker()
broker.start()

stop_flag = threading.Event()
stop_flag.clear()

p = threading.Thread(target=producer)
p.start()

c = threading.Thread(target=consumer, args=[stop_flag, ])
c.start()

for _ in range(10):
    logging.info('.')
    time.sleep(1)

stop_flag.set()
broker.stop()
