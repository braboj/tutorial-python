import threading
import time


def on_new_client():
    while True:
        print(".")
        time.sleep(1)


while True:
    t = threading.Thread(target=on_new_client, args=(c,addr))
    t.start()

s.close()