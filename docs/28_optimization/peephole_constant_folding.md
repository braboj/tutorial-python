# peephole_constant_folding

```python
# Example: Peephole Optimization - Constant Folding

def unoptimized_const():

    # Simulates the creation of unoptimized constants

    # Short strings
    a = "Hello"
    a = a + a + a

    # Tuples
    b = (1, 2)
    b = b * 3

    # Expressions
    c = 60
    c = c * 5

    return a, b, c


def peephole_const():

    # Python optimizes strings up to 4096 characters and tuples of length up to 256 elements
    # Varite the length of the string and tuple to see the difference.

    # Short strings
    a = "Hello" * 3

    # Tuples
    b = (1, 2) * 3

    # Expressions
    c = 60 * 60

    return a, b, c


print(unoptimized_const.__code__.co_consts)
# (None, 'Hello', 1, 2, 5, (10, 20, 30), 7)

print(peephole_const.__code__.co_consts)
# (None, 604800, 'HelloHelloHello', (1, 2, 1, 2, 1, 2))
```
