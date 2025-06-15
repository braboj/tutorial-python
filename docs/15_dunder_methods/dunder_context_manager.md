# dunder_context_manager

```python
# Dunder methods for context manager
# ---------------------------------------------------------------------------
# The __enter__ and __exit__ methods allow an object to define its own
# setup and teardown logic when used in a with-statement. This example shows
# how implementing these hooks customizes resource management behavior.

class Complex(object):

    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __enter__(self):
        print(">>> Inside __enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(">>> Inside __exit__")
        print(" Execution type:", exc_type)
        print(" Execution value:", exc_val)
        print(" Traceback:", exc_tb)

        if exc_type is not None:
            print("\nException occurred")
            return True
        else:
            print("\nNo exception occurred")
            return False


with Complex(1, 0) as c:
    print(">>> Inside with block")
    print(c.real, c.imag)
    print(c.real / 0)
```
