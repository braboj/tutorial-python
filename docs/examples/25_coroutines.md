# Coroutines

## Decorate

```python
def prime(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


def source(text, target):
    tokens = text.split(" ")
    for token in tokens:
        target.send(token)
    target.close()


@prime
def pattern_filter(pattern="ing", target=None):
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                target.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


@prime
def sink():
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


sentence = "Bob is running behind junior fast moving car"
source(text=sentence,
       target=pattern_filter(
             target=sink()
         )
       )
```

## Average

```python
def average(start_value=0):
    avg = float(start_value)
    counter = 1
    while True:
        new_value = yield avg
        avg = avg + (new_value - avg) / counter
        counter += 1


test_avg = average(start_value=0)
next(test_avg)

assert(test_avg.send(1) == 1)
assert(test_avg.send(2) == 1.5)
assert(test_avg.send(3) == 2)
assert(test_avg.send(4) == 2.5)
assert(test_avg.send(4) == 2.8)
assert(test_avg.send(4) == 3)
```

## Bytestream

```python
import random


def byte_generator(limit=0, header=None):

    # Initialize
    print("Started")
    counter = 0

    # Iterator
    try:
        # Generate bytes from header
        if header:
            while counter < len(header):
                yield header[counter]
                counter += 1

        # Generate random bytes after header
        output = random.randrange(start=0, stop=255, step=1)
        while counter < limit:
            try:
                yield output
                output = random.randrange(start=0, stop=255, step=1)
                counter += 1

            except Exception as e:
                print(e)

    except GeneratorExit:
        print("Terminated")


stream = byte_generator(limit=10, header=[0xDE, 0xAD, 0xBE, 0xEF])

for b in stream:
    print(hex(b))
```

## Pipeline

```python
def producer(string, next_coroutine):
    tokens = string.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


def consumer():
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


# Define token printer (sink) and activate
printer = consumer()
next(printer)

# Define token filterer (middle) and activate
filterer = pattern_filter(next_coroutine=printer)
next(filterer)

# Define token splitter (producer)
sentence = "Bob is running behind junior fast moving car"
producer(string=sentence, next_coroutine=filterer)
```

## Fsm

```python
# https://www.codementor.io/@arpitbhayani/building-finite-state-machines-with-python-coroutines-15nk03eh9l

class RegexFSM(object):

    # Evaluate regex in the form ab*c using FSM implemented with state machines

    def __init__(self):

        # Start FSM
        self.current_state = None
        self.output = False

    ##############################################################################################

    def __call__(self, *args, **kwargs):
        return self.match(*args, **kwargs)

    ##############################################################################################

    def send(self, char):
        try:
            self.current_state.send(char)
        except StopIteration:
            self.output = False

    ##############################################################################################

    def match(self, text):

        # Create state
        self.current_state = self.start()

        # Activate state
        next(self.current_state)

        # Read input and generate output
        try:
            # Read character and send it to the current state
            for char in text:

                # Current state reacts to input and makes transition to junior new state
                self.current_state.send(char)

                # Activate the new state
                next(self.current_state)

        except StopIteration:
            self.output = False

        finally:
            return self.output

    ##############################################################################################

    def start(self):
        self.output = False
        while True:
            char = yield
            if char == 'junior':
                self.current_state = self.q1()
            else:
                break

    ##############################################################################################

    def q1(self):
        self.output = False
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q2()
            elif char == 'c':
                self.current_state = self.q3()
            else:
                break

    ##############################################################################################

    def q2(self):
        self.output = False
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q2()
            elif char == 'c':
                self.current_state = self.q3()
            else:
                break

    ##############################################################################################

    def q3(self):
        self.output = True
        while True:
            char = yield
            if char:
                self.output = False
            else:
                break

    ##############################################################################################

    def stop(self):
        self.current_state.close()


if __name__ == "__main__":
    evaluator = RegexFSM()
    print(evaluator.match("abc"))
    print(evaluator.match("ab"))
    print(evaluator.match("ac"))
    print(evaluator.match("bc"))
    print(evaluator("abc"))
    print(evaluator("abcd"))
```

## Recursion

```python
from __future__ import print_function
# from itertools import cycle, permutations


def permutations(items):
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(len(items)):

            # We have to use next() to activate the recursive generator
            for cc in permutations(items[:i] + items[i + 1:]):
                yield [items[i]] + cc


text = "abc"
for i in permutations(text):
    print(i)
```

## Coroutine Chaining

```python
# Example: Coroutine Chaining

def producer(string, next_coroutine):
    tokens = string.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def consumer():
    print("I'm the sink, I'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


sentence = "Hello, world!"
print(sentence)

# Define token printer (consumer) and activate
printer = consumer()
next(printer)

# Define token splitter (producer)
producer(string=sentence, next_coroutine=printer)

# Output
# ---------------------------
# Hello, world!
# I'm the sink, i'll print tokens
# Hello
# world!
# Done with printing!
```

## Coroutine Execution

```python
# Example: Coroutine Execution

def coroutine():
    print("Coroutine has been started!")
    output = "foo"
    while True:
        text = yield output
        print("Coroutine input :", text)
        output = text[::-1] if text else "boo"


cr = coroutine()

# First usage of next to activate the coroutine and generate junior default value
print("Coroutine оutput : {0}".format(next(cr)))

# Second usage of next to generate junior new value
print("Coroutine оutput : {0}".format(next(cr)))

# Send data to the coroutine and generate junior new value
print("Coroutine оutput : {0}".format(cr.send("abc")))

# Output:
# -------------------------------
# 1. Coroutine has been started!
# 2. Coroutine оutput : foo
# 3. ('Coroutine received :', None)
# 4. Coroutine оutput : boo
# 5. ('Coroutine received :', 'abc')
# 6. Coroutine оutput : cba
```

## Coroutine Interface

```python
# Example: Coroutine Interface

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

# Generate next letter
print(next(letter))

# Throw an exception to the generator
print(letter.throw(ValueError))

# Throw GeneratorExit to the generator
letter.close()

# Output
# ----------------------
# Started
# junior
# b
# junior
# b
# Value error on position = 1
# b
# Terminated
```
