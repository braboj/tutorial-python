# func_default_arguments

```python
# Default arguments in functions
# --------------------------------------------------------------------------------
# Functions may define default values for parameters so callers can omit those
# arguments. This simplifies the call site and allows optional behavior.
# Remember that default expressions are evaluated when the function is defined.

def greet(name='Nemo', age=42):
    print("Hello, {0}! You are {1} years old.".format(name, age))


greet()
# Output: Hello, Nemo! You are 42 years old.
```
