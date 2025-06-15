# user_input_python3

```python
# User Input in Python 3
# --------------------------------------------------------------------------------
# Use `input()` to get input from the user, which returns a string. Use `eval()`
# to evaluate the input as a Python expression, or `int()` to convert it to
# an integer.

# Enter `1+1` that will be printed as a string
prompt = input('Enter a string: ')
print(prompt)
# Output: <user input>

# Enter `1+1` to get the result of the expression
prompt = input('Enter an expression: ')
evaluated_input = eval(prompt)
print(f"Execute statement: {evaluated_input}")
# Output: <user input evaluated as a Python expression>
```
