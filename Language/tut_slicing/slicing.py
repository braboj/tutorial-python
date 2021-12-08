# LIST[START : STOP : STEP]
# START : Initial value included in the slice
# STOP  : First value that is not in the slice
# STEP  :
# [::] is literal for slice(start, stop, step)

"""

And I know that "abcdef"[::-1] is transformed to "abcdef"[6:-7:-1], so, the best way to explain would be: let len be
the length of the sequence. If step is positive, the defaults for start and end are 0 and len. Else if step is
negative, the defaults for start and end are len and -len - 1.
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
