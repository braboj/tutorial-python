# Adding attributes to functions using decorators
# ------------------------------------------------------------------------------
# Sometimes you may want to add metadata to a function, such as an author
# name or version without modifying the function's code directly. A good way
# to do this is by using a decorator. Decorators are functions that modify
# the behavior of another function. In this case, we can create a decorator
# that adds an attribute to the function it decorates.

def owned(func):
    func.author = "Branimir Georgiev"
    return func


@owned
def hello():
    pass


print(hello.author)
# Output: Branimir Georgiev
