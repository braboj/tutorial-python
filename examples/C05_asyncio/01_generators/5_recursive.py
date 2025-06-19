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
