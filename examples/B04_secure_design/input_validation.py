# Example: Input Validation
# ------------------------------------------------------------------------------
# Validates user input before using it. This prevents unexpected behaviour
# or vulnerabilities such as injection or crashes.

import re

user_input = input('Enter an age (0-120): ')

# Accept only digits using a regular expression
if not re.fullmatch(r"\d+", user_input):
    raise ValueError('Input must be a positive integer')

age = int(user_input)

if not 0 <= age <= 120:
    raise ValueError('Age out of expected range')

print(f'Your age is {age}')
