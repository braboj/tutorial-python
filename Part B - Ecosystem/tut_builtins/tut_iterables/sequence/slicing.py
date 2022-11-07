###############################################################################
# SLICE BUILTIN
###############################################################################

"""
slice(stop)
slice(start, stop, step)

start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if
not provided.

"""

sequence = list(range(10))

s = slice(1)
print(sequence[s])
print(sequence[:1])

s = slice(1, None, None)
print(sequence[s])
print(sequence[1:])

s = slice(0, 2, None)
print(sequence[s])
print(sequence[0:2])

s = slice(0, 10, 2)
print(sequence[s])
print(sequence[0:10:2])

print(sequence[-1:])
print(sequence[:-1])
print(sequence[-8:-1])
print(sequence[-8:-1:2])


###############################################################################
# [::] LITERAL
###############################################################################

""""
LIST[START : STOP : STEP]
START : Initial value included in the slice
STOP  : First value that is not in the slice
STEP  : Index increment
[::] is literal for slice(start, stop, step)

"abcdef"[::-1] is transformed to "abcdef"[6:-7:-1]

let len be the length of the sequence. If step is positive, the defaults for start and end are 0 and len
else the defaults for start and end are len and -len - 1.
"""

test = range(10)

# Print whole list
print(test[::])

# Print reversed starting with the last element
print(test[::-1])
print(test[None:None:-1])
print(test[len(test):(-len(test) - 1):-1])

# First 3 elements starting from 0
print(test[:3])

# Last 3 elements starting from -3
print(test[-3:])

# Everything except first and last element
print(test[1:-1])

# Everything except first and last element but reversed
print(test[-2:-len(test):-1])

# Stepped slicing
print(test[::2])
print(test[::-2])

# Rotate last byte
x = test[-1:] + test[:-1]
print(x)
x = x[-1:] + x[:-1]
print(x)
