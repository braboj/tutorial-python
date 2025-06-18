# Get the type of a variable
# --------------------------------------------------------------------------------
# Python offers a way to inspect the type of a variable using `type()`. Type
# is a special class in Python that servers many purposes, including
# determining the type of a variable. When invoked on a variable, it returns
# the type of that variable, which can be useful for troubleshooting or understanding
# the data being worked with.

var = 100
print(var, type(var))
# Output: 100 <class 'int'>

var = 100.0
print(var, type(var))
# Output: 100.0 <class 'float'>
