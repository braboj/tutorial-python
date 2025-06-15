# generator_delegation

```python
# Example: Generator Delegation

def sub_1():
    yield 1


def sub_2():
    yield 2


def sub_3():
    yield 3


def main_generator():
    yield from sub_1()
    yield from sub_2()
    yield from sub_3()


wrapper = main_generator()
for x in wrapper:
    print(x, end=", ")
```
