###############################################################################
# Find and replace a value
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [1, 2, 3, 10, 5]


# data = [1, 2, 3, 4, 5]
# index = data.index(4)
# data[index] = 10
# print(data)


###############################################################################
# Sort the list in reverse order
# Difficulty: EASY
# -----------------------------------------------------------------------------
# DATA: [1, 2, 3, 4, 5]
# RES:  [5, 4, 3, 2, 1]


# data = [1, 2, 3, 4, 5]
# data.sort(reverse=True)
# print(data)


###############################################################################
# Sort the list by length in reverse order
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Branko", "Theodor", "Hristo"]
# OUT:  ['Theodor', 'Branko', 'Hristo']


# data = ["Branko", "Hristo", "Theodor"]
# data.sort(key=lambda x:len(x), reverse=True)
# print(data)


###############################################################################
# Reverse the given list
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [5, 4, 3, 2, 1]


# data = [1, 2, 3, 4, 5]
# print(data.reverse())


###############################################################################
# Remove and return the element at index x
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  4 [1, 2, 3, 5]


# data = [1, 2, 3, 4, 5]
# print(data.pop(3), data)


###############################################################################
# Remove an element as value from a list
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Hristo", "Branko", "Theodor"]
# OUT:  ["Hristo", "Theodor"]


# data = ["Hristo", "Branko", "Theodor"]
# data.remove("Branko")
# print(data)


###############################################################################
# Insert an element at position x
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Hristo", "Theodor", "Branko"]
# OUT:  ["Hristo", "Theodor", "Vanya", "Branko"]


# data = ["Hristo", "Theodor", "Branko"]
# data.insert(2, "Vyara")
# print(data)


###############################################################################
# Add object at the end of the list. The object can be also a sublist
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5], [6, 7, 8, 9]
# OUT:  [1, 2, 3, 4, 5, [6, 7, 8, 9]]


# data = [1, 2, 3, 4, 5]
# sublist = [6, 7, 8, 9]
# data.append(sublist)
# print(data)


###############################################################################
# Add object or objects at the end of the list. A sublist will be unpacked.
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5], [6, 7, 8, 9]
# OUT:  [1, 2, 3, 4, 5, 6, 7, 8, 9]


# data = [1, 2, 3, 4, 5]
# sublist = [6, 7, 8, 9]
# data.extend(sublist)
# print(data)


###############################################################################
# Count the number of occurences of a given item in a list
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Hello", "World!", "Hello", "Developer"], ITEM: "Hello"
# OUT:  2


# data = ["Hello", "World!", "Hello", "Developer"]
# print(data.count("Hello"))


###############################################################################
# Get the first index of an element
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Hello", "World!", "Hello", "Developer"], ITEM: "Hello"
# OUT:  0


# data = ["Hello", "World!", "Hello", "Developer"]
# print(data.index("Hello"))


###############################################################################
# Square all the items in a list
# Difficulty: Easy
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [1, 4, 9, 16, 25]


# data = [1, 2, 3, 4, 5]
# result = [x * x for x in data]
# print(result)

###############################################################################
# Remove empty elements from a list
# Difficulty: Easy
# -----------------------------------------------------------------------------
# IN:   [1, None, 2, None, 3, None, 4, None, 5, None]
# OUT:  [1, 2, 3, 4, 5]


# data = [1, None, 2, None, 3, None, 4, None, 5, None]
# result = [x for x in data if x is not None]
# print(result)


###############################################################################
# Hard: Concatenate two lists by index
# Difficulty: Hard
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]
# OUT:  [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]


# Short version
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
# result = [[x, y] for x, y in zip(a, b)]
# print(result)

# Long version
# def zip(a, b):
#     result = []
#     for x in range(min(len(a), len(b))):
#         result.append([a[x], b[x]])
#
#     return result
#
#
# result = zip(a, b)
# print(result)

###############################################################################
# Filter out all positive prime numbers in a list
# Difficulty: Hard
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [1, 3, 5]


# import math
#
#
# # creating function
# def prime(x):
#     # checking for negative numbers
#     if x <= 1:
#         return
#
#     #  for loop to iterate through number range to find its root if exist
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return
#
#     return x
#
#
# # calling function
# data = [1, 2, 3, 4, 5]
# result = [prime(x) for x in data  if prime(x) is not None]
# print(result)


###############################################################################
# Change every two numbers in a list
# Difficulty: Hard
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [2, 1, 4, 3, 5]

# def swap(sequence, pos1, pos2):
#     last = data.index(data[-1])
#     if pos1 <= last and pos2 <= last:
#         t = data[pos1], data[pos2]
#         data[pos2], data[pos1] = t
#     return sequence
#
#
# data = [1, 2, 3, 4, 5]
# result = data
# for i in range(0, len(data), 2):
#     result = swap(data, i, i + 1)
# print(result)
