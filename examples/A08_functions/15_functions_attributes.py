# Adding attributes to functions
# ------------------------------------------------------------------------------
# Functions in Python are can have attributes. They are accessed using the dot
# notation (e.g. `foo.name`), and can be used to store metadata about the
# function, such as its name, description, or author.

def foo():
    pass


foo.name = "MyFunc"
foo.description = "This is my function"
foo.author = "Me"

print(foo.author)
# Output: Me

print(foo.name)
# Output: MyFunc

print(foo.description)
# This is my function
