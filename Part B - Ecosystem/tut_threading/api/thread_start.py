import time
import threading


def my_func():

    print("func : Starting {id}".format(id=id))
    time.sleep(5)
    print('func : Finishing {id}'.format(id=id))


if __name__ == "__main__":

    t = threading.Thread(target=my_func)
    t.start()