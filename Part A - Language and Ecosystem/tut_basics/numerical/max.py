"""
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])

Return the largest item in an iterable or the largest of two or more arguments. If one positional argument is
provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional
arguments are provided, the largest of the positional arguments is returned.

The key argument specifies a one-argument ordering function. The default argument specifies an object to return if
the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.

If multiple items are maximal, the function returns the first one encountered.

"""

number = [3, 2, 8, 5, 10, 6]
smallest_number = max(number)
print("The largest number is:", smallest_number)

languages = ["Python", "C Programmaxg", "Java", "JavaScript"]
smallest_string = max(languages)
print("The largest string is:", smallest_string)

square = {2: 4, 3: 9, -1: 1, -2: 4}

# the smallest key
key1 = max(square)
print("The largest key:", key1)

# the key whose value is the smallest
key2 = max(square, key=lambda k: square[k])
print("The key with the largest value:", key2)

# getting the smallest value
print("The largest value:", square[key2])

# the smallest key
default = max([], default=0xFF)
print("The default max:", default)

result = max(4, -5, 23, 5)
print("The maximum number is:", result)