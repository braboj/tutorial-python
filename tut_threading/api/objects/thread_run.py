import threading


class MyThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)

    def run(self):
        print("Called by threading.Thread.start()")


if __name__ == '__main__':
    mythread = MyThread()
    mythread.start()
    mythread.join()