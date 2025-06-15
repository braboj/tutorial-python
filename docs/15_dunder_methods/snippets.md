# snippets

```python
# Demonstration of special methods
# ---------------------------------------------------------------------------
# Various dunder methods show how objects integrate with Python features

class DunderClass(object):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        pass
    # ---------------------------------------------------------------------------------------------
    # - Context manager
    # ---------------------------------------------------------------------------------------------

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Iterator protocol
    # ---------------------------------------------------------------------------------------------

    def __iter__(self):
        pass

    def __next__(self):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Class decorators
    # ---------------------------------------------------------------------------------------------

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, item):
        pass

    def __getattr__(self, item):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Class representation
    # ---------------------------------------------------------------------------------------------

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __bytes__(self):
        pass

    def __sizeof__(self):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Overload comparison operators
    # ---------------------------------------------------------------------------------------------

    def __eq__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    # ---------------------------------------------------------------------------------------------
    # - Overload arithmetic operators
    # ---------------------------------------------------------------------------------------------
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass
```
