from weakref import WeakValueDictionary


class Counter:
    _instances = WeakValueDictionary()

    @property
    def count(self):
        return len(self._instances)

    def __init__(self, name):
        self.name = name
        self._instances[id(self)] = self
        print(name, 'created')

    def __del__(self):
        print(self.name, 'deleted')
        if self.count == 0:
            print('Last Counter object deleted')
        else:
            print(self.count, 'Counter objects remaining')


x = Counter("First")
y = Counter("Second")

