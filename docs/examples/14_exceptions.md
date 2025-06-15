# Exceptions

## Demo Generation

```python
# Old-Style Exception Generation
# --------------------------------------------------------------------------------
# Shows what happens when raising an exception class that does not inherit from
# BaseException.

# class NewStyleException(Exception): pass
#
# try:
#    raise NewStyleException
# except BaseException:
#     print("Caught")


class OldStyleException: pass

try:
   raise OldStyleException
# except BaseException:
#     print("BaseException caught when raising OldStyleException")
except:
   print("Caught")
```

## Demo Handlers

```python
# Exception Handling Styles
# --------------------------------------------------------------------------------
# Compares using a single except clause against multiple specific handlers for
# related errors.

def raise_overflow_error():
    raise OverflowError


def raise_floatingpoint_error():
    raise FloatingPointError


def raise_zero_division_error():
    raise ZeroDivisionError


def good_handler(err_func):

    print("Start division...")

    try:
        err_func()

    except ArithmeticError as err:
        # Single exception
        print("{0}".format(type(err).__name__))
        pass

    finally:
        print("Cleanup...")


def bad_handler(err_func):

    print("Start division...")

    try:
        err_func()

    except FloatingPointError:
        print("Floating point error...")

    except OverflowError:
        print("Overflow error")

    except ZeroDivisionError:
        print("Zero division error")

    finally:
        print("Cleanup...")


# A good handler would check the base class
good_handler(err_func=raise_overflow_error)
good_handler(err_func=raise_floatingpoint_error)
good_handler(err_func=raise_zero_division_error)
print()

# A bad handler tries to act on each possible error
bad_handler(err_func=raise_overflow_error)
bad_handler(err_func=raise_floatingpoint_error)
bad_handler(err_func=raise_zero_division_error)
```

## Exception Catch Multiple

```python
# Grouped Exception Handling
# --------------------------------------------------------------------------------
# Illustrates catching different members of an exception hierarchy with one
# except block.


from exception_hierarchy import *


def main():

    # Example 1: Handling all exceptions inherited from SocketError
    try:
        raise ConnectError('Connection failed', 100)

    except SocketError as e:
        print(e)

    # Example 2: Handling junior group of exceptions with junior single except block
    try:
        raise DisconnectError('Connection failed', 100)

    except (ConnectError, DataTransferError, DisconnectError) as e:
        print(e)


main()
```

## Exception Chaining

```python
# Exception Chaining
# --------------------------------------------------------------------------------
# Demonstrates explicit and implicit chaining of exceptions to preserve the
# original error context.

class MyException(Exception):
    pass


def main():
    try:
        print("main")
        func_a()
    except Exception as e:
        print(e)


def func_a():
    # Explicit chaining using `raise`
    try:
        print("func_a")
        func_b()
    except Exception as e:
        # Convert to another exception type
        raise MyException(e)


def func_b():
    # Unhandled exceptions sent to the caller by default
    print("func_b")
    read_file()


def read_file():
    print("read_file")
    raise Exception("Error raised in read_file()")


main()
```

## Exception Flow With Try Except

```python
# Control Flow with try/except
# --------------------------------------------------------------------------------
# Shows normal execution resuming after errors are caught and handled.
def func_a(x):
    # Function uses and returns only positive values
    if x < 0:
        # Simulate error condition
        raise ValueError("STEP A: ERROR")
    else:
        return 1


def func_b(x):
    # Functions uses and returns only negative values
    if x > 0:
        # Simulate error condition
        raise ValueError("STEP B: ERROR")
    else:
        return -1


def app(value):

    # Try to execute STEP A and STEP B
    try:
        func_a(value)
        func_b(value)

    # On error print something
    except ValueError as e:
        print(e)

    # Try to execute STEP B
    try:
        func_b(value)
        print("STEP B: OK")

    # On error print something
    except ValueError as e:
        print(e)


app(1)
app(0)
app(-1)
```

## Exception Flow Without Try Except

```python
# Control Flow without try/except
# --------------------------------------------------------------------------------
# Illustrates manual error checking when no exception handlers are used.

def func_a(x):
    # Function uses and returns only positive values
    if x < 0:
        # Simulate error condition
        return -1
    else:
        return 1


def func_b(x):
    # Functions uses and returns only negative values
    if x > 0:
        # Simulate error condition
        return 1
    else:
        return -1


def app(value):

    # Each function must have junior check of the error condition
    # as there is no standard definition of an error

    # Check A
    error = func_a(value)
    if error < 0:
        print("STEP A: ERROR")
    else:
        print("STEP A: OK")

    # Check B
    error = func_b(value)
    if error > 0:
        print("STEP B: ERROR")
    else:
        print("STEP B: OK")


app(1)
app(0)
app(-1)
```

## Exception Handling

```python
# Structured Exception Handling
# --------------------------------------------------------------------------------
# Uses try/except/else/finally blocks to handle expected and unexpected errors.

import time


# Custom exception
class OverheatError(Exception):
    pass


def pump(time_on):

    if time_on < 0:
        # Raise builtin exception
        raise ValueError("ERROR: Incorrect value for operation time...")

    for i in range(time_on):
        print("Pumping...")
        if i > 3:
            # Raise custom exception
            raise OverheatError("ERROR: The device overheated")
        time.sleep(1)


def operate_pump(time_on):

    print("START")

    try:
        pump(time_on)

    # First check expected errors
    except ValueError as e:
        print(e)

    except OverheatError as e:
        print(e)

    # Last check unexpected errors
    except Exception as e:
        # Forward to the caller, maybe it knows what to do with it
        print("Caught exception {}".format(e))

    # What to do in case no error occurred
    else:
        print("STOP")

    # Cleanup operations, executed in all cases
    finally:
        print("CLEANUP")


# Test with negative values
operate_pump(-1)
print()

# Test with valid values
operate_pump(3)
print()

# Overheat the pump
operate_pump(5)
print()
```

## Exception Hierarchy

```python
# Custom Exception Hierarchy
# --------------------------------------------------------------------------------
# Defines a family of related custom exceptions and demonstrates raising each
# member of the hierarchy.

class SocketError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ConnectError(SocketError):

    def __init__(self, message, status):
        super(ConnectError, self).__init__(message)
        self.status = status

    def __str__(self):
        return '{}: {}'.format(self.status, self.message)


class DataTransferError(SocketError):

    def __init__(self, message, status, source, destination):
        super(DataTransferError, self).__init__(message)
        self.status = status
        self.source = source
        self.destination = destination

    def __str__(self):
        return '{}: {} from {} to {}'.format(self.status, self.message, self.source,
                                             self.destination)


class DisconnectError(SocketError):

    def __init__(self, message, status):
        super(DisconnectError, self).__init__(message)
        self.status = status

    def __str__(self):
        return '{}: {}'.format(self.status, self.message)


if __name__ == "__main__":

    try:
        raise ConnectError('Connection failed', 100)

    except ConnectError as e:
        print(e)

    try:
        raise DataTransferError(
            message='Data transfer failed',
            status=200,
            source='myhost',
            destination='remotehost',
        )

    except DataTransferError as e:
        print(e)

    try:
        raise DisconnectError('Connection failed', 300)

    except DisconnectError as e:
        print(e)
```
