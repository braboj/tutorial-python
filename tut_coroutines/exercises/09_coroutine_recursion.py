from __future__ import print_function
# from itertools import cycle, permutations


def permutations(items):
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i] + items[i + 1:]):
                yield [items[i]] + cc


text = ['r', 'e']
for p in permutations(text):
    print(''.join(p), end=", ")

print("\r")

text = "game"
for p in permutations(text):
    print(''.join(p), end=", ")