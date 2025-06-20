# Understanding variable scope in Python
# ------------------------------------------------------------------------------
# There are two types of variable scope in Python: global and local. If a
# local variable has the same name as a global variable, the local variable
# will take precedence within the function.
#
# If the function needs to use the global variable, it must declare it as
# global using the `global` keyword.
#
# !!! WARNING !!!
# Modifying a global variable inside a function can lead to unexpected behavior
# and should be done with caution. A good practice is to avoid the use of
# global variables altogether, unless absolutely necessary.

var = 1
print(var)


# Output: 1

# Local variable with the same name
def func_local_var():
    # Redefine the variable within the function scope
    var = 2
    print(var)


func_local_var()
print(var)


# Output: 1

def func_using_global_var():
    # Declare that we want to use the global variable
    global var
    var = 3
    print(var)


func_using_global_var()
