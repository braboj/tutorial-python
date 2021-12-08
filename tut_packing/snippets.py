test_string = "PYTHON"
test_list = [1, 2, 3, 4]
test_dict = {"A": 1, "B": 2}

# Unpack string
*test, = test_string
print(test)

# Unpack list
*test, = test_list
print(test)

# Unpack dictionary items
*test, = test_dict.items()
print(test)

# Copy dictionary
test = {**test_dict}
print(test)
print(test is test_dict)