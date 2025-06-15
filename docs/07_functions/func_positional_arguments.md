# func_positional_arguments

```python
# Using positional arguments
# --------------------------------------------------------------------------------
# Each value is matched to a parameter based on where it appears, so the order
# of the provided arguments matters. Positional parameters correspond directly
# to the order defined in the function signature. Mixing up the order can lead
# to incorrect results or errors.

def greet(name, age):
    print("Hello, {0}! You are {1} years old.".format(name, age))


# Calling the greet() function with positional arguments
greet("Alice", 25)
```
