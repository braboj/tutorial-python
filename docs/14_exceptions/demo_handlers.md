# demo_handlers

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
