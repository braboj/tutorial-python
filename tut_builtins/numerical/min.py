"""
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])

Return the smallest item in an iterable or the smallest of two or more arguments. If one positional argument is
provided, it should be an iterable. The smallest item in the iterable is returned. If two or more positional
arguments are provided, the smallest of the positional arguments is returned.

The key argument specifies a one-argument ordering function. The default argument specifies an object to return if
the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.

If multiple items are minimal, the function returns the first one encountered.

"""

number = [3, 2, 8, 5, 10, 6]
smallest_number = min(number)
print("The smallest number is:", smallest_number)

languages = ["Python", "C Programming", "Java", "JavaScript"]
smallest_string = min(languages)
print("The smallest string is:", smallest_string)

square = {2: 4, 3: 9, -1: 1, -2: 4}

# the smallest key
key1 = min(square)
print("The smallest key:", key1)    # -2

# the key whose value is the smallest
key2 = min(square, key=lambda k: square[k])
print("The key with the smallest value:", key2)    # -1

# getting the smallest value
print("The smallest value:", square[key2])    # 1

# the smallest key
default = min([], default=0xFF)
print("The default min:", default)

result = min(4, -5, 23, 5)
print("The minimum number is:", result)