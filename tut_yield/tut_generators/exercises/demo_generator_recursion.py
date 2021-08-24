import sys
import trace

##################################################################################################
# GENERATORS
##################################################################################################


# Using recursion in generator function
def oddnum(start):
    yield start
    start += 2
    while True:
        yield next(oddnum(start))
        start += 2


def test():
    # Using for loop to print odd numbers till 10 from 1
    for nums in oddnum(1):
        if nums < 10:
            print (nums)
        else:
            break


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
