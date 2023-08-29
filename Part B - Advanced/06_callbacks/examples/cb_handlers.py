from collections import defaultdict


class Monitor(object):

    def __init__(self, name):
        self.name = name
        self._callbacks = defaultdict(list)

    def register_callback(self, event, callback):
        self._callbacks[event].append(callback)

    def unregister_callback(self, event, callback):
        self._callbacks[event].remove(callback)

    def trigger_event(self, event):
        for callback in self._callbacks[event]:
            callback(event, self)


def callback1(event, device):
    print('Callback 1: Got {} on device {}'.format(event, device.name))


def callback2(event, device):
    print('Callback 2: Got {} on device {}'.format(event, device.name))


d = Monitor('Device 1')
d.register_callback('event1', callback1)
d.register_callback('event1', callback2)

d.trigger_event('event1')
d.trigger_event('event2')
