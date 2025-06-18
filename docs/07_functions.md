# Functions

## Func Annotations

```python
# Function 16_type_hints for parameters and return values
# --------------------------------------------------------------------------------
# Annotations in Python functions allow you to specify the expected types of
# parameters and the return type of the function. This can help with code
# readability and static type checking.
#
# There are no strict rules enforced by Python regarding these 16_type_hints,
# but they serve as a guide for developers and can be used by tools like
# type checkers, IDEs, and documentation 01_generators.

def add(x: int, y: int) -> int:
    return x + y
```

## Func Attributes

```python
# Adding attributes to functions
# --------------------------------------------------------------------------------
# Functions in Python are first-class objects, which means they can have
# attributes just like any other object. Attributes are accessed using
# the dot notation (e.g. `foo.name`), and can be used to store metadata
# about the function, such as its name, description, or author.

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
```

## Func Attributes Decorator

```python
# Adding attributes to functions using decorators
# --------------------------------------------------------------------------------
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
```

## Func Callback

```python
# Using callback functions to handle events
# --------------------------------------------------------------------------------
# A callback function is passed as an argument to another function and executed
# when a particular event occurs. This technique lets the caller customize
# behavior without changing the callee. Callbacks are common in event-driven
# architectures and asynchronous code.

_listeners = {}

def on(event_name, callback):
    _listeners.setdefault(event_name, []).append(callback)


def emit(event_name, *args, **kwargs):
    for callback in _listeners.get(event_name, []):
        callback(*args, **kwargs)


def handle_data(data):
    print(f"[DATA] Received: {data!r}")


def handle_error(msg):
    print(f"[ERROR] {msg}")


on("data", handle_data)
on("error", handle_error)

emit("data", {"id": 1, "value": 42})
emit("data", {"id": 2, "value": 99})
emit("error", "Timeout occurred")
```

## Func Closures

```python
# Closures in Python
# --------------------------------------------------------------------------------
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
```

## Func Decorator

```python
# Decorators to modify or extend function behavior
# --------------------------------------------------------------------------------
# A decorator is a function that takes another function as an argument,
# modifies or extends its behavior, and returns a new function. They are
# related to closures, as they can access variables from the enclosing scope.

def decorate(func):
    """A simple decorator function."""

    def wrapper(*args, **kwargs):
        """Wrapper function with additional behavior."""

        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with {args} and {kwargs}")
        return result

    return wrapper

@decorate
def hello_world():
    print('Hello world')

hello_world()

def hello_python():
    print('Hello Python')

hello_python = decorate(hello_python)
hello_python()
```

## Func Decorator With Args

```python
# Parameterized decorators in Python
# --------------------------------------------------------------------------------
# Unfortunately, Python does not support passing parameters to decorators
# directly. A decorator of a function has always one argument, which is the
# original function to be decorated.
#
# In order to pass parameters to a decorator, we need to create an enclosing
# function that takes the decorator parameters and returns a decorator
# function.
#
# The decorator function will then take the original function as an argument
# and return a wrapper function modifying the behavior of the original function.

def log(message="Operation"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{message}: {func.__name__} called with args: {args}")
            return result
        return wrapper
    return decorator

@log()
def add(a, b):
    return a + b

@log("Custom log")
def sub(a, b):
    return a - b

def div(a, b):
    return a / b

add(5, 3)
# Output: Operation: add called with args: (5, 3)

sub(10, 4)
# Output: Custom log: sub called with args: (10, 4)

div = log("Division operation")(div)
div(10, 2)
# Output: Division operation: div called with args: (10, 2)
```

## Func Default Arguments

```python
# Default arguments in functions
# --------------------------------------------------------------------------------
# Functions may define default values for parameters so callers can omit those
# arguments. This simplifies the call site and allows optional behavior.
# Remember that default expressions are evaluated when the function is defined.

def greet(name='Nemo', age=42):
    print("Hello, {0}! You are {1} years old.".format(name, age))


greet()
# Output: Hello, Nemo! You are 42 years old.
```

## Func Factory

```python
# Function factories to create specialized functions
# --------------------------------------------------------------------------------
# A function factory returns a new function tailored to the argument it
# receives. It enables creation of many small functions without repeating code.
# Each generated function captures the parameters provided to the factory.

def power_of(n):
    def power(x):
        return x ** n

    return power


# Square root
sqrt = power_of(0.5)
print(sqrt(100.0))

# Square
sqr = power_of(2)
print(sqr(10.0))
```

## Func Introspection

```python
# Inspect function attributes
# --------------------------------------------------------------------------------
# Python stores a variety of metadata about functions on the function object
# itself. Attributes such as ``__name__``, ``__doc__`` and ``__code__`` can be
# inspected at runtime to learn more about a function's definition. This
# 33_introspection ability is useful for troubleshooting and for frameworks that
# manipulate functions.

def foo(a, b=10, c=20, *args, **kwargs):
    """This is 'foo' function that does nothing."""

    pi = 3.14

    def bar(a=1, b=2, c=3, *args, **kwargs):
        """This is 'bar' function that does nothing."""

        print(pi)

        introspections = {
            '__globals__': bar.__globals__,
            '__name__': bar.__name__,
            '__doc__': bar.__doc__,
            '__code__': bar.__code__,
            '__defaults__': bar.__defaults__,
            '__closure__': bar.__closure__,
            '__dict__': bar.__dict__,
        }

        # A function has a name
        test = introspections['__name__']
        print("Getting function attribute __name__ -> {} ".format(test))

        # A function has a docstring
        test = introspections['__doc__']
        print("Getting function attribute __doc__ -> {} ".format(test))

        # A function has default arguments
        test = introspections['__defaults__']
        print("Getting function attribute __defaults__ -> {} ".format(test))

        # A function has access to the global namespace
        test = introspections['__globals__']
        print("Getting function attribute __globals__ -> {} ".format(test))

        # A function has a closure
        test = introspections['__closure__']
        print("Getting function attribute __closure__ -> {} ".format(test))

        # A function has a variables dictionary
        test = introspections['__dict__']
        print("Getting function attribute __dict__ -> {} ".format(test))

        # A function has a code object
        test = introspections['__code__']
        print("Getting function attribute __code__ -> {} ".format(test))

        # A code object has name
        print(test.co_name)

    bar()


# foo(1, 2, 3, 4, 5, c=30, d=40, e=50)
foo(a=1, d=40, e=50)
```

## Func Keyword Arguments

```python
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
```

## Func Keyword Only Arguments

```python
# Keyword-only arguments
# --------------------------------------------------------------------------------
# Keyword-only parameters must be specified by name in the call. This avoids
# ambiguity and makes the purpose of each argument clear. It is particularly
# helpful when a function accepts many optional parameters.

# The arguments a and b are keyword-only
def keyword_only_arguments(*, a, b):
    return a + b


# The argument a is positional or keyword, b is keyword-only
def one_keyword_only_argument(a, *, b):
    return a + b


# The argument a is positional only, b is keyword-only
def separate_arguments(a, /, *, b):
    return a + b
```

## Func Lambda Arguments

```python
# Lambda functions with multiple arguments
# --------------------------------------------------------------------------------
# A lambda expression can accept several parameters just like a regular
# function. It is useful for short, inline operations where defining a full
# function would be excessive. Here we compute a simple expression using five
# arguments.

# Multi-parameter lambda
x = lambda a, b, c, d, e: (a + b) * (c + d) / e
print(x(1, 2, 3, 4, 5))
```

## Func Lambda Assignment

```python
# Assigning a lambda expression to a variable
# --------------------------------------------------------------------------------
# Lambda expressions can be assigned to variables to create small, unnamed
# functions on the fly. Doing so lets you reuse the lambda just like a regular
# function object. This pattern is handy for callbacks or short computations.

nop = lambda: None
print(nop())
```

## Func Lambda Bytecodes

```python
# Lambda and def produce the same bytecode
# --------------------------------------------------------------------------------
# This script compiles a lambda expression and a regular function to compare
# their bytecode output. Both forms compile into nearly identical instructions.
# Using ``lambda`` therefore carries no extra runtime cost compared to ``def``.

import dis

func1 = lambda x: x * x


def func2(x):
    return x * x


print(dis.dis(func1))
print(dis.dis(func2))
```

## Func Lambda Conditional

```python
# Conditional lambda
# --------------------------------------------------------------------------------
# A lambda can contain a conditional expression to produce different values
# based on its input. This one returns ``1`` when the argument is positive and
# ``0`` otherwise. Such compact expressions are useful for simple
# transformations.
y = lambda b: 1 if b > 0 else 0
print(y(-1), y(0), y(1))
```

## Func Lambda Nested Conditions

```python
# Lambda function with nested conditionals
# --------------------------------------------------------------------------------
# This lambda expression checks two ranges using nested conditional operators.
# It returns ``1`` when the argument exceeds 10 or falls below -10 and ``0`` in
# all other cases. The expression remains concise despite the multiple branches.
z = lambda c: 1 if c > 10 else (1 if c < -10 else 0)
print(-11, -10, -1, 0, 1, 10, 11, sep='\t')
print(z(-11), z(-10), z(-1), z(0), z(1), z(10), z(11), sep='\t')
```

## Func Lambda Recursive

```python
# Lambda function with recursion
# --------------------------------------------------------------------------------
# Although lambdas are typically simple, they can also be used recursively.
# The expression here computes factorial by calling itself for successive
# decrements. Assigning the lambda to a variable is required so it can
# reference itself.

x = lambda a: a * x(a - 1) if a > 1 else 1
print(x(5))
```

## Func Lambda Syntax

```python
# Lambda functions
# --------------------------------------------------------------------------------
# Lambda expressions provide a compact way to create anonymous functions.
# They consist of a parameter list, a colon and a single expression that becomes
# the return value. Because they are limited to one expression, lambdas are best
# suited for small operations.

"""
lambda [param1, param2, ..]: expression

Lambda functions are one-line functions which return an expression using
the pre-defined parameters param1, param2, ... paramN.

Lambda functions are normally used for quick operations on data,
most notably in combination with map, filter, reduce.

"""

# Define a list to iterate over
data_in = [1, 2, 3]

# Use a lambda function to square the input and then map the result to a list `data_out`
data_out = list(map(lambda x: x * x, data_in))

# Print the result
print(data_in, data_out)
```

## Func Memoization

```python
# Memoization with an inner function that caches results
# --------------------------------------------------------------------------------
# The inner ``memoized_fibonacci`` function stores each computed Fibonacci
# number in the ``cache`` dictionary. On subsequent calls with the same
# argument, the cached value is returned instead of recalculating it. This
# avoids redundant work and illustrates the principle of memoization.

# Explicit memoization using a dictionary
def fibonacci(n):
    cache = {}

    def memoized_fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            result = n
        else:
            result = memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
        cache[n] = result
        return result

    return memoized_fibonacci(n)


print(fibonacci(5))
print(fibonacci(10))


# Memoization using a decorator (the internal cache is a dictionary)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(10))
```

## Func Nested

```python
# Nested functions and their access to enclosing variables
# --------------------------------------------------------------------------------
# Inner functions can access variables from the outer function that defines
# them. This ability creates a closure which preserves the environment even
# after the outer function has finished executing. It allows the inner function
# to operate using data that would otherwise be out of scope.

def absolute_value(x):
    # Emulate the built-in abs() function, e.g. abs(-1) == 1 and abs(1) == 1

    def negative_value():
        # An inner function can access the variables of the outer function

        return -x

    def positive_value():
        # An inner function can also access the variables of the outer function

        return x

    # Use the inner functions to return the correct value
    return negative_value() if x < 0 else positive_value()


print(absolute_value(-1))  # 1
print(absolute_value(1))  # 1
```

## Func Positional Arguments

```python
# Using positional arguments
# --------------------------------------------------------------------------------
# Each value is matched to a parameter based on where it appears, so the order
# of the provided arguments matters. Positional parameters correspond directly
# to the order defined in the function signature. Mixing up the order can lead
# to incorrect results or errors.

def greet(name, age):
    print("Hello, {0}! You are {1} years old.".format(name, age))


# Calling the greet() function with positional arguments
greet("Alice", 25)
```

## Func Positional Only Arguments

```python
# Positional-only arguments
# --------------------------------------------------------------------------------
# Some parameters can be declared positional-only so they cannot be passed by
# name. This keeps the API minimal and prevents accidental clashes with keyword
# arguments. The syntax uses a ``/`` in the parameter list to mark the end of
# positional-only parameters.

# The arguments a and b are positional-only
def positional_only_arguments(a, b, /):
    return a + b


# The argument a is positional-only, b is positional or keyword
def one_positional_only_argument(a, /, b):
    return a + b
```

## Func Recursion

```python
# Recursive functions in Python
# --------------------------------------------------------------------------------
# A recursive function repeatedly calls itself with a simpler version of the
# original problem. Each call works toward a base case that stops the recursion.
# This technique is often used for tasks that can be defined in terms of similar
# subproblems.

def factorial(n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    else:
        return n * factorial(n - 1)


test_function = factorial(5)
print(test_function)
```

## Func Scope

```python
# Understanding variable scope in Python
# --------------------------------------------------------------------------------
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
```

## Func Structure

```python
# Anatomy of a Python function
# --------------------------------------------------------------------------------
# A function definition begins with the ``def`` keyword followed by its name and
# parameters. The body can perform operations using those parameters and return
# a value. Well-documented functions include a docstring that briefly states
# their purpose.

def function_name(parameter1, parameter2):
    """ Docstring: description of the function """

    # Code to be executed when the function is called
    result = parameter1 + parameter2
    print(result)

    # Return statement (optional)
    return result
```

## Func Unpacking Arguments

```python
# Argument unpacking with `*args`
# --------------------------------------------------------------------------------
# When calling a function, the star operator can expand an iterable into
# positional arguments. This allows you to store the arguments in a list or
# other iterable and pass them all at once.

def my_function(a, b, c):
    print(a, b, c)


args = [1, 2, 3]
my_function(*args)
```

## Func Variable Arguments Python2

```python
# Handling a variable number of arguments in Python 2
# --------------------------------------------------------------------------------
# This code captures extra positional arguments with ``*args`` and extra
# keyword arguments with ``**kwargs`` when keyword-only parameters are
# unavailable. In Python 3 you can declare keyword-only parameters using the
# ``*`` separator instead of relying on ``**kwargs``. See
# ``func_variable_arguments_python3.py`` for comparison.

def variable_number_of_arguments(a, b, *args, **kwargs):
    print("a: {a}".format(a=a))
    print("b: {b}".format(b=b))
    print("args: {args}".format(args=args))
    print("kwargs: {kwargs}".format(kwargs=kwargs))


variable_number_of_arguments(1, 2, 3, c=4)
```

## Func Variable Arguments Python3

```python
# Mixing positional arguments with keyword-only arguments
# --------------------------------------------------------------------------------
# Python 3 lets you combine regular positional parameters with ``*args`` and
# keyword-only parameters that have default values. The `*` separator defines
# that the positional parameters until a key-value pair is encountered.

def variable_number_of_arguments(a, *args, b=1, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


variable_number_of_arguments(1, 2, 3, c=4)
```
