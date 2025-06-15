# generator_expression_equivalent

```python
# Example: Generator expression equivalent

def num():
    for x in range(100):
        if x % 2 == 0:
            yield x


num_generator = num()
for x in num_generator:
    print(x)
```
