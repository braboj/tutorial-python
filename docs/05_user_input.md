# User Input

## User Input Python2

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

## User Input Python3

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

## User Input With Six

```python
# Cross-Version User Input with six
# --------------------------------------------------------------------------------
# If the code needs to work in both Python 2 and 3, you can use the `six`
# library to handle user input.

from six.moves import input

prompt = input('Enter something: ')
print(prompt)
# Output: <user input in bytes>
```
