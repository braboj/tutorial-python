# Generators

## Counter

```python
def counter(offset):

    # Execution starts
    while True:

        # Execution is halted
        yield offset

        # Execution resumption with next()
        offset += 1


# Get the iterator object by calling the generator function
gen = counter(1)

# Get next element using next() as function and object method
print(next(gen))

# Print the rest
for x in gen:
    print(x)

##################################################################################################
# Python 3.3+ : yield from
##################################################################################################
# def gen2():
#     yield from "Python"
#     yield from range(5)
#
# print("\ng2: ", end=", ")
# g2 = gen2()
# for x in g2:
#     print(x, end=", ")
# print()
```

## Memory Footprint

```python
import sys

# Create list comprehension and print size
l = [i for i in range(10)]
print("List size is {0}".format(sys.getsizeof(l)))

# Print items
for x in l:
    print(x)

# Create generator expression and print size
g = (k for k in range(10))
print("")
print("Generator expression size is {0}".format(sys.getsizeof(g)))

# Print items
for x in g:
    print(x)
```

## Fibonacci

```python
def fibonacci_number(f0=0, f1=1, limit=1):

    # Initialize
    a, b = f0, f1

    # Loop
    while True:
        yield a

        # Solution 01
        # a, b = b, a + b

        # Solution 02
        b = a + b
        a = b - a


test = fibonacci_number(f0=2, f1=3)

for i in range(10):
    print(next(test))
```

## Delegation

```python
# def city_generator():
#     cities = ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Ruse', 'Stara Zagora', 'Pleven', 'Sliven', 'Dobrich', 'Shumen']
#     for x in cities:
#         yield x


def city_ranking(n=1):

    def city_generator():
        cities = ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Ruse', 'Stara Zagora', 'Pleven', 'Sliven',
                  'Dobrich', 'Shumen']
        for x in cities:
            yield x

    g = city_generator()
    for x in range(n):
        yield next(g)


for city in city_ranking(n=5):
    print(city)
```

## Recursive

```python
import sys
import trace


# Using recursion in generator function
def oddnum(offset=1, limit=10):

    if (offset % 2) == 0:
        offset += 1

    if offset < limit:
        yield offset
    else:
        return

    for x in range(offset + 2, limit, 2):
        yield next(oddnum(x, limit))


def test():
    # Using for loop to print odd numbers till 10 from 1
    for nums in oddnum(limit=10):
        print (nums)


##################################################################################################
# TRACING
##################################################################################################

ENABLE = 0

tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=ENABLE,
    count=0)

# run the new command using the given tracer
tracer.runfunc(test)
```

## Generator Concept

```python
# Subroutine returning a collection object
def sub_even_numbers(stream):
    them = []
    for n in stream:
        if n % 2 == 0:
            them.append(n)
    return them


# Generator function which generates a sequence of values
def gen_even_numbers(stream):
    for n in stream:
        if n % 2 == 0:
            yield n


if __name__ == "__main__":

    # Get the even numbers using the subroutine
    result = sub_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(result)

    # Get the even numbers using the generator function
    result = gen_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for x in result:
        print(x, end=" ")
```

## Generator Delegation

```python
# Example: Generator Delegation

def sub_1():
    yield 1


def sub_2():
    yield 2


def sub_3():
    yield 3


def main_generator():
    yield from sub_1()
    yield from sub_2()
    yield from sub_3()


wrapper = main_generator()
for x in wrapper:
    print(x, end=", ")
```

## Generator Expression

```python
# Example: Generator expression

num = (x for x in range(100) if x % 2 == 0)
for x in num:
    print(x)
```

## Generator Expression Complex

```python
# Example: Complex generator expression with the the ternary operator (if-else)

# Yield "apple" if number is even else yield "pie"
generator = (("apple" if i % 2 == 0 else "pie") for i in range(6))
for x in generator:
    print(x)
```

## Generator Expression Equivalent

```python
# Example: Generator expression equivalent

def num():
    for x in range(100):
        if x % 2 == 0:
            yield x


num_generator = num()
for x in num_generator:
    print(x)
```

## Generator Expression Walrus

```python
# Example: Walrus operator in a generator expression

# The walrus operator (:=) assigns values to variables as part of a larger
# expression. It is also known as the assignment expression and is supported
# in Python 3.8 and above. It is useful for troubleshooting, dictionary creation,
# and more.

gen = (x for x in range(10) if (y := x % 2) == 1)
for x in gen:
    print(x, y)
```

## Generator Infinite

```python
# Example: Infinite sequence

def infinite_sequence():
    i = 0
    while True:
        yield i
        i += 1


gen = infinite_sequence()

# The generator is a type of iterator that implements the iterator protocol.

print(next(gen))
print(next(gen))
print(next(gen))

# ... and so on
```

## Generator Nested

```python
# Example: Nested generator

def inner_generator(n):
    for j in range(n):
        yield "Inner Value {}".format(j)


def outer_generator(n):
    for i in range(n):
        yield "Outer Value {}".format(i)
        for inner_value in inner_generator(i):
            yield inner_value


# Usage
n = 3
for value in outer_generator(n):
    print(value)
```

## Generator Passing

```python
# Example: Generator Passing

def generator():
    yield 1
    yield 2
    yield 3


def wrapper(g):
    yield from g


for x in wrapper(generator()):
    print(x, end=", ")
```

## Generator Recursive

```python
# Example: Recursive generator for Fibonacci numbers

def fibonacci(n):
    if n <= 0:
        return
    a, b = 0, 1
    yield a  # Yield the first Fibonacci number
    for _ in range(n - 1):
        a, b = b, a + b
        yield a


# Usage
n = 10  # Generate the first 10 Fibonacci numbers
for number in fibonacci(n):
    print(number)
```

## Letter Generator

```python
def letter_generator(text):
    print("Started")
    position = 0
    try:
        while True:
            try:
                offset = yield text[position]

                if offset is None:
                    position += 1
                else:
                    position = offset

            except ValueError:
                print("Value error on position = " + str(position))

    except GeneratorExit:
        print("Terminated")


letter = letter_generator("abc")

# Generate letters
print(next(letter))
print(next(letter))

# Reset generator and generate letter
print(letter.send(0))

# Generate a next letter
print(next(letter))

# Throw an exception to the generator
print(letter.throw(ValueError))

# Throw GeneratorExit to the generator
letter.close()
```
