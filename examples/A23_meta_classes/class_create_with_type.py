# Using ``type`` to inspect objects and create classes
# ------------------------------------------------------------------------------
# The built-in ``type`` function performs two unrelated tasks. When passed a
# single object it returns that object's class, which can be handy for
# inspection. When given a name, base classes and attributes it creates a new
# class dynamically, allowing programs to define types at runtime.

##############################################################################
# USECASE A : Get object type
##############################################################################
numbers_list = [1, 2]
print(type(numbers_list))

numbers_dict = {1: 'one', 2: 'two'}
print(type(numbers_dict))


##############################################################################
# USECASE B : Create class with base classes, attributes and methods
##############################################################################

def init(self, name):
    self.name = name


def say_hallo_b(self):
    return "Hi, my name is " + self.name


Robot2 = type("Robot2",
              (),
              {"counter": 0,
               "__init__": init,
               "func": lambda self: "Hi, I am " + self.name,
               "say_hello_b": say_hallo_b
               }
)


x = Robot2("Marvin")
print(x.name)
print(x.func())
print(x.say_hello_b())
