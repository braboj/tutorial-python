# user_input_python2

```python
# User Input in Python 2
# --------------------------------------------------------------------------------
# Use `input()` to execute the input as Python code, or `raw_input()` to get a
# string input. Please not that this example works in Python 2.x only.

# Type `1+1` that will be printed as a string
prompt = raw_input('Enter a string: ')
print(prompt)
# Output: <string entered by the user>

# Type `1+1` to get the result of the expression
prompt = input('Execute an expression: ')
# Output: <result of the executed statement>
print("Execute statement: {}".format(prompt))
```
