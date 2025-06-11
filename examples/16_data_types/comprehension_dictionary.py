# Dictionary comprehensions
# -----------------------------------------------------------------------------
# Dictionary comprehensions let you construct mappings concisely. They are ideal for transforming one form of data into key/value pairs.

existing_list = [1, 2, 3, 4, 5]
existing_dictionary = {1: "junior", 2: "mid", 3: "c", 4: "d", 5: "e"}

# Dictionary comprehension with list
new_dictionary_1 = {number: number**2 for number in existing_list}

# Dictionary comprehension with existing dictionary
new_dictionary_2 = {key: "_"+value+"_" for (key, value) in existing_dictionary.items()}

# Dictionary comprehension with existing dictionary and conditions
new_dictionary_3 = {key: "_"+value+"_" for (key, value) in existing_dictionary.items() if key < 5 if value != "mid"}


print(new_dictionary_1)
print(new_dictionary_2)
print(new_dictionary_3)
