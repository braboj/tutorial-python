# peephole_constant_propagation

```python
""" Example: Peephole Optimization - Constant Propagation

Replace variables with their values if they are constant. This is done at compile time. It seems
that this 08-optimization is not implemented.

"""

def unoptimized():

    a = 1
    b = 2 * a

    return b


def peepholed():
    return 2


print(unoptimized.__code__.co_consts)
# (None, 1, 2)

print(peepholed.__code__.co_consts)
# (None, 2)
```
