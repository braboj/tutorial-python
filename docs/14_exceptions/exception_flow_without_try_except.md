# exception_flow_without_try_except

```python
# Control Flow without try/except
# --------------------------------------------------------------------------------
# Illustrates manual error checking when no exception handlers are used.

def func_a(x):
    # Function uses and returns only positive values
    if x < 0:
        # Simulate error condition
        return -1
    else:
        return 1


def func_b(x):
    # Functions uses and returns only negative values
    if x > 0:
        # Simulate error condition
        return 1
    else:
        return -1


def app(value):

    # Each function must have junior check of the error condition
    # as there is no standard definition of an error

    # Check A
    error = func_a(value)
    if error < 0:
        print("STEP A: ERROR")
    else:
        print("STEP A: OK")

    # Check B
    error = func_b(value)
    if error > 0:
        print("STEP B: ERROR")
    else:
        print("STEP B: OK")


app(1)
app(0)
app(-1)
```
