# data_deque_lifo

```python
# Deque as LIFO stack
# -----------------------------------------------------------------------------
# Using deque as a stack provides efficient push and pop operations.

from collections import deque


def emtpy_deque(plates):

    # Test the deque
    while True:
        try:

            # Get the item from the right
            item = plates.pop()
            print("Get item: {}".format(item))

        except IndexError as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_deque(plates):

    items = ['Soup plate', 'Salad plate', 'Dinner plate', 'Dessert plate']

    for item in items:
        plates.append(item)
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
