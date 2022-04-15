import random
import os
import hashlib
# Check if the OS has a randomness source
print(os.urandom(1))

# Initialize the random generator
# If the OS has not randomness source the system time will be used to initialize the random generator
#
random.seed()

# Get the random generator state
state = random.getstate()
print(state)

# Set the random generator state
random.setstate(state)
