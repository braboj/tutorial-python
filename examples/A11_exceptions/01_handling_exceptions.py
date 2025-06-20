# Structured Exception Handling
# ------------------------------------------------------------------------------
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
