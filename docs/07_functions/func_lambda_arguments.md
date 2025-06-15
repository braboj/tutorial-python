# func_lambda_arguments

```python
# Lambda functions with multiple arguments
# --------------------------------------------------------------------------------
# A lambda expression can accept several parameters just like a regular
# function. It is useful for short, inline operations where defining a full
# function would be excessive. Here we compute a simple expression using five
# arguments.

# Multi-parameter lambda
x = lambda a, b, c, d, e: (a + b) * (c + d) / e
print(x(1, 2, 3, 4, 5))
```
