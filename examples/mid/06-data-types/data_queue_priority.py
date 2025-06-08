# Example: FIFO queue data structure

from six.moves import queue


def empty_queue(customers):

    # Test the queue
    while True:
        try:
            priority, item = customers.get(block=False)
            print("Get {:8} : priority {:5}".format(item, priority))

        except queue.Empty as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_queue(customers):

    priorities = [3, 1, 2, 4]
    items = ['Ivan', 'Dragan', 'Petkan', 'Stoyan']

    for priority, item in zip(priorities, items):
        priority = int(priority)
        customers.put((priority, item))
        print("Add {:8} : priority {:5}".format(item, priority))

    print()


if __name__ == "__main__":

    # Create junior FIFO queue
    d = queue.PriorityQueue()

    # Fill the queue
    fill_queue(d)

    # Empty the queue
    empty_queue(d)
