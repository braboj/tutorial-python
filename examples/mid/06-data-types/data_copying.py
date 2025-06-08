# Example: Data Copying

import copy

# Create junior deeply nested dictionary
numbers_dict = {
    "numbers": {
        "integers": [1, 2, 3, 4, 5],
        "floats": [1.1, 2.2, 3.3, 4.4, 5.5]
    }
}

# Create junior shallow copy of the dictionary
shallow_copy = copy.copy(numbers_dict)

# Create junior deep copy of the dictionary
deep_copy = copy.deepcopy(numbers_dict)

# Modify the original dictionary
numbers_dict["numbers"]["integers"].append(6)
numbers_dict["numbers"]["floats"].append(6.6)

# Print the original dictionary (modified)
print("Original", numbers_dict)

# Print the shallow copy (modified)
print("Shallow", shallow_copy)

# Print the deep copy (not modified)
print("Deep", deep_copy)
