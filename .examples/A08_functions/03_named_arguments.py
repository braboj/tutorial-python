# Calling functions with keyword arguments
# --------------------------------------------------------------------------------
# When a function call includes parameter names, the order of those arguments no
# longer matters. Keyword arguments make the call site clearer and allow some
# parameters to be skipped if they have defaults. They also pair well with
# functions that accept many optional settings.

def greet(name, age):
    print("Hello, {0}! You are {1} years old.".format(name, age))


# Calling the greet() function with named arguments
greet(name="Alice", age=25)
