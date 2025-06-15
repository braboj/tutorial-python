# 6_recursion

```python
from __future__ import print_function
# from itertools import cycle, permutations


def permutations(items):
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(len(items)):

            # We have to use next() to activate the recursive generator
            for cc in permutations(items[:i] + items[i + 1:]):
                yield [items[i]] + cc


text = "abc"
for i in permutations(text):
    print(i)
```
