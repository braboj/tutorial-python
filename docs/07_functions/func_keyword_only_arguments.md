# func_keyword_only_arguments

```python
# Keyword-only arguments
# --------------------------------------------------------------------------------
# Keyword-only parameters must be specified by name in the call. This avoids
# ambiguity and makes the purpose of each argument clear. It is particularly
# helpful when a function accepts many optional parameters.

# The arguments a and b are keyword-only
def keyword_only_arguments(*, a, b):
    return a + b


# The argument a is positional or keyword, b is keyword-only
def one_keyword_only_argument(a, *, b):
    return a + b


# The argument a is positional only, b is keyword-only
def separate_arguments(a, /, *, b):
    return a + b
```
