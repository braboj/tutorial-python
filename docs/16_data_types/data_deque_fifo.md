# data_deque_fifo

```python
# Deque as FIFO queue
# -----------------------------------------------------------------------------
# Deque offers fast O(1) operations at both ends, making it ideal for implementing queues.

from collections import deque


def emtpy_deque(customers):

    # Test the deque
    while True:
        try:

            # Get the item from the right
            item = customers.pop()
            print("Get item: {}".format(item))

        except IndexError as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_deque(customers):

    items = ['Ivan', 'Dragan', 'Petkan', 'Stoyan']

    for item in items:
        customers.appendleft(item)
        print("Add item: {}".format(item))

    print()


if __name__ == "__main__":

    # Create a deque
    d = deque()

    # Fill the deque
    fill_deque(d)

    # Empty the deque
    emtpy_deque(d)
```
