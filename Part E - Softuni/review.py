###############################################################################
# 1. Find and replace a value in a list
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [1, 2, 3, 10, 5]

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i == 4:
        numbers.pop(i - 1)
        numbers.insert(i - 1, 10)
print(numbers)

# REVIEW: O points
# We want to use the value and not the index as defined in the task

# Proposal 1: Replaces all values using a for loop
for num in numbers:  # Look in numbers
    if num == 4:  # If you find the desired value
        val_index = numbers.index(num)  # Get its index
        numbers[val_index] = 10  # Use the index to replace the value
print(numbers)

# Proposal 2: Use list comprehension to replace all values
numbers = [10 if num == 4 else num for num in numbers]
print(numbers)

# Proposal 3: Replace only the first value found
numbers = [1, 2, 3, 4, 5]
index = numbers.index(4)
numbers[index] = 10
print(numbers)

###############################################################################
# 2. Sort the list in reverse order
# Difficulty: EASY
# -----------------------------------------------------------------------------
# DATA: [1, 2, 3, 4, 5]
# RES:  [5, 4, 3, 2, 1]


data = [1, 2, 3, 4, 5]
data.reverse()
print(data)

# REVIEW: 1 POINT
# Perfect solution

###############################################################################
# 3. Sort the list by length in reverse order
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Branko", "Theodor", "Hristo"]
# OUT:  ['Theodor', 'Branko', 'Hristo']


names = ["Branko", "Theodor", "Hristo"]
names.sort()
reversed_order = sorted(names, key=lambda i: -len(i))
print(reversed_order)

# REVIEW: 0.5 POINTS
# Use the method sort of the list object, it is easier to read
names.sort(key=lambda x: len(x), reverse=True)
print(data)

###############################################################################
# 4. Reverse the given list
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [5, 4, 3, 2, 1]


x = [1, 2, 3, 4, 5]
x.reverse()
print(x)

# REVIEW: 1 POINT
# Perfect solution


###############################################################################
# 5. Remove and return the element at index x
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  4 [1, 2, 3, 5]


numbers = [1, 2, 3, 4, 5]
x = numbers.pop(3)
print(x, numbers)

# REVIEW: 1 POINT
# Perfect solution


###############################################################################
# 6. Remove an element as a value from a list
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Hristo", "Branko", "Theodor"]
# OUT:  ["Hristo", "Theodor"]

names = ["Hristo", "Branko", "Theodor"]
names.pop(1)
print(names)

# REVIEW: 0 Points
# The solution doesn't match the task. In the task it is required to use the
# value to remove the element and not the index like in pop.

names = ["Hristo", "Branko", "Theodor"]
names.remove("Branko")
print(names)

###############################################################################
# 7. Insert an element at position x
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Hristo", "Theodor", "Branko"]
# OUT:  ["Hristo", "Theodor", "Vanya", "Branko"]

names = ["Hristo", "Theodor", "Branko"]
names.insert(2, "Vanya")
print(names)

# REVIEW: 1 POINT
# Perfect solution

###############################################################################
# 8. Add object at the end of the list. The object can be also a sublist
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5], [6, 7, 8, 9]
# OUT:  [1, 2, 3, 4, 5, [6, 7, 8, 9]]

# Hristo
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
list1.append(list2)
print(list1)

# REVIEW: 1 POINT
# Perfect solution

###############################################################################
# 9. Add object or objects at the end of the list. A sublist will be unpacked.
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5], [6, 7, 8, 9]
# OUT:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
list1.extend(list2)
print(list1)

# REVIEW: 1 POINT
# Perfect solution


###############################################################################
# 10. Count the number of occurences of a given item in a list
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Hello", "World!", "Hello", "Developer"], ITEM: "Hello"
# OUT:  2

words = ["Hello", "World!", "Hello", "Developer"]
x = words.count("Hello")
print(x)

# REVIEW: 1 POINT
# Perfect solution


###############################################################################
# 11. Get the first index of an element
# Difficulty: EASY
# -----------------------------------------------------------------------------
# IN:   ["Hello", "World!", "Hello", "Developer"], ITEM: "Hello"
# OUT:  0

words = ["Hello", "World!", "Hello", "Developer"]
x = words.index("Hello")
print(x)

# REVIEW: 1 POINT
# Perfect solution


###############################################################################
# 12. Square all the items in a list
# Difficulty: Easy
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
new_numbers = []
for i in numbers:
    x = i ** 2
    new_numbers.append(x)
# new_numbers = [lambda i: i**2, numbers]
print(new_numbers)

# REVIEW: 0.5 POINT
# The solution can be implemented using a list comprehension, The statement
# new_numbers = [lambda i: i**2, numbers] will generate a list of a function and arreay
# and not give the required results.

result = [x * x for x in numbers]
print(result)

###############################################################################
# 13. Remove empty elements from a list
# Difficulty: Easy
# -----------------------------------------------------------------------------
# IN:   [1, None, 2, None, 3, None, 4, None, 5, None]
# OUT:  [1, 2, 3, 4, 5]

numbers = [1, None, 2, None, 3, None, 4, None, 5, None]
new_numbers = []

for i in numbers:
    if i != None:
        new_numbers.append(i)
print(new_numbers)

# REVIEW: 0.5 POINTS
# The warning given by PyCharm is because None must be compared with the 'is'
# operator. The solution above can be implemented with list comprehensions.

# Proposal 1:
for i in numbers:
    if i is not None:
        new_numbers.append(i)
print(new_numbers)

# Proposal 2:
result = [num for num in numbers if x is not None]
print(result)

###############################################################################
# 14. Hard: Concatenate two lists by index
# Difficulty: Hard
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]
# OUT:  [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]

numbers = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

list1 = numbers[0]
list2 = numbers[1]
list3 = []
list4 = []
for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
    list4.append(list3)
    list3 = []

print(list4)

numbers = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
list1 = numbers[0]
list2 = numbers[1]
x = list(zip(list1, range(1, len(list2) + 1)))
print(x)

# REVIEW: 0 points
# The task requires to concatenate 2 separate arrays into one and not combine
# the two array into one such as [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

# Proposal 1:
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
result = [[x, y] for x, y in zip(a, b)]
print(result)


# Proposal 2:
def my_zip(a, b):
    result = []
    for x in range(min(len(a), len(b))):
        result.append([a[x], b[x]])

    return result


result = my_zip(a, b)
print(result)

###############################################################################
# 15. Filter out all positive prime numbers in a list
# Difficulty: Hard
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [1, 3, 5]

numbers = [1, 2, 3, 4, 5]
new_list = []
for num in numbers:
    if num % 2 != 0:
        new_list.append(num)
print(new_list)


# REVIEW: 0 POINTS
# This solution will identify 9 as a prime number, which is not correct.
# The definition of prime numbers is to be positive, to divide by 1 and
# the number itself. With this definition the number 1 is not a prime
# number.

# Proposal
import math


def prime(x):

    # Prime numbers must be positive and divide by one and the number itself.
    # This is the classical definition of prime numbers.
    if x <= 1:
        return

    #  Use the square root method for time optimization
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return

    return x


# Filter out the list
data = [1, 2, 3, 4, 5]
result = [prime(x) for x in data if prime(x) is not None]
print(result)


###############################################################################
# 16. Change every two numbers in a list
# Difficulty: Hard
# -----------------------------------------------------------------------------
# IN:   [1, 2, 3, 4, 5]
# OUT:  [2, 1, 4, 3, 5]

numbers = [1, 2, 3, 4, 5, 6, 7]
y = len(numbers) // 2
i = 0
for n in range(y):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    i += 2
print(numbers)

# REVIEW: 1 POINT
# WAAW! VERY GOOD SOLUTION, BRAVO!


###############################################################################
# QUIZ
###############################################################################

# https://www.w3schools.com/python/python_quiz.asp
# https://quizizz.com/admin/quiz/5c068cfae4c9a9001b21ef52/python-lists
# https://pynative.com/python-list-quiz/
# https://www.geeksforgeeks.org/python-list-quiz/
# https://realpython.com/quizzes/python-lists-tuples/viewer
# https://cs20.ca/Python/PracticeQuizzes/Lists.html
# https://myandroid.site/python-list-quiz/
