# func_positional_only_arguments

```python
# Positional-only arguments
# --------------------------------------------------------------------------------
# Some parameters can be declared positional-only so they cannot be passed by
# name. This keeps the API minimal and prevents accidental clashes with keyword
# arguments. The syntax uses a ``/`` in the parameter list to mark the end of
# positional-only parameters.

# The arguments a and b are positional-only
def positional_only_arguments(a, b, /):
    return a + b


# The argument a is positional-only, b is positional or keyword
def one_positional_only_argument(a, /, b):
    return a + b
```
