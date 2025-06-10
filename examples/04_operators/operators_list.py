# Common list operators in Python
# -----------------------------------------------------------------------------
# This file contains examples of the most commonly used operators on lists,
# including indexing, slicing, concatenation, repetition, and membership tests.

my_list = [1, 2, 3, 4, 5]

# Indexing
print(my_list[0])   # Access the first element
print(my_list[-1])  # Access the last element

# Slicing
print(my_list[1:4]) # Get a sublist from index 1 to 3
print(my_list[:3])  # Get the first three elements

# Concatenation
new_list = my_list + [6, 7, 8]
print(new_list)  # Combine two lists

# Repetition
repeated_list = my_list * 2
print(repeated_list)  # Repeat the list twice

# Membership test
print(3 in my_list)  # Check if 3 is in the list
print(10 not in my_list)  # Check if 10 is not in the list
