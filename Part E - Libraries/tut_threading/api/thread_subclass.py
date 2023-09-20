import threading
import logging


class MyThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None):

        super(MyThread, self).__init__(group, target, name, args, kwargs)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return


def test():
    for i in range(5):
        t = MyThread(args=(i,), kwargs={'a': 'A', 'b': 'B'})
        t.start()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
    test()

