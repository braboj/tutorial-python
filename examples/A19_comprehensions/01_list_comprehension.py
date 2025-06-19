# List A19_comprehensions
# -----------------------------------------------------------------------------
# List A19_comprehensions allow you to create or filter lists concisely without
# explicit loops.

existing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension without condition
new_list_1 = [number**2 for number in existing_list]

# List comprehension with condition
new_list_2 = [number**2 for number in existing_list if number < 6]

print(new_list_1)
print(new_list_2)
