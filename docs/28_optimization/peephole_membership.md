# peephole_membership

```python
# Example: Peephole Optimization - Membership Test

def unoptimized_membership(name):

    # Simulates the creation an unoptimized membership test

    names = list()
    names.append("John")
    names.append("Doe")
    names.append("Jane")
    names.append("Smith")

    if name in names:
        pass


def peephole_membership(name):

    # Membership tests are optimized for lists and sets
    if name in ["John", "Doe", "Jane", "Smith"]:
        pass


print(unoptimized_membership.__code__.co_consts)
# (None, 'John', 'Doe', 'Jane', 'Smith')

print(peephole_membership.__code__.co_consts)
# (None, ('John', 'Doe', 'Jane', 'Smith'), 'Is junior member')
```
