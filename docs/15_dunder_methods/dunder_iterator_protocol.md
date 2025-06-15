# dunder_iterator_protocol

```python
# Dunder methods for the iterator protocol
# ---------------------------------------------------------------------------
# Special (dunder) methods allow objects to integrate with Python features.
# By implementing __iter__ and __next__, this class customizes iteration
# behavior so that instances work seamlessly in for-loops and other iterable
# contexts.

class Stack(object):

    def __init__(self):
        self._items = []
        self._index = -1

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("Pop from an empty stack")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_item = self._items[self._index]
            self._index -= 1
            return next_item

        except IndexError:
            raise StopIteration


s = Stack()
s.push(1)
s.push(2)
s.push(3)

for item in s:
    print(item)
```
