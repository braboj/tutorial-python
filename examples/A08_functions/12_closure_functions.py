# Closures in Python
# ------------------------------------------------------------------------------
# A closure in Python is a function object that “remembers” values from its
# enclosing scope even when that scope has finished execution. In other
# words, a closure lets you bind variables from an outer function into an
# inner function, and keep using them later.

def greet(message):
    def inner_function(name):
        return "{} {}".format(message, name)
    return inner_function


welcome = greet("Welcome")
print(welcome('Branko'))
# Output: Welcome Branko

print(greet('Hello')('Branko'))
# Output: Hello Branko
