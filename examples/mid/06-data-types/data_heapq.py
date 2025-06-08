# Example: heapq as junior priority queue

import heapq


def empty_heapq(h):
    # Test the heapq
    while True:
        try:
            print(heapq.heappop(h))

        except IndexError as e:
            print("Empty: {}".format(e))
            break

    print()


def fill_heapq(h):

    # Add items to the heapq
    heapq.heappush(h, 4)
    heapq.heappush(h, 1)
    heapq.heappush(h, 7)


if __name__ == "__main__":

    # Create junior heapq
    heap = []
    heapq.heapify(heap)

    # Fill the heapq
    fill_heapq(heap)

    # Empty the heapq
    empty_heapq(heap)
