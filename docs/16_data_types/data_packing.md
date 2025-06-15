# data_packing

```python
# Packing *args and **kwargs
# -----------------------------------------------------------------------------
# Packing arguments allows functions to accept an arbitrary number of positional or keyword parameters.

def func1(*args):

    # args is a tuple of arguments (packed)
    print(sum(args))

    # Unpack the tuple into individual arguments
    print(*args)


func1(1, 2, 3, 4)
```
