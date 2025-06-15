# data_queue_lifo

```python
# LIFO queue with LifoQueue
# -----------------------------------------------------------------------------
# LifoQueue behaves like a stack while remaining safe for use with multiple threads.

from six.moves import queue


def empty_queue(customers):

    # Test the queue
    while True:
        try:
            item = customers.get(block=False)
            print("Get item: {}".format(item))

        except queue.Empty as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_queue(customers):

    items = ['Ivan', 'Dragan', 'Petkan', 'Stoyan']

    for item in items:
        customers.put(item)
        print("Add item: {}".format(item))

    print()


if __name__ == "__main__":

    # Create a LIFO queue
    d = queue.LifoQueue()

    # Fill the queue
    fill_queue(d)

    # Empty the queue
    empty_queue(d)
```
