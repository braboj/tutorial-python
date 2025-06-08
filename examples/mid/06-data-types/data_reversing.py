# Example: Filter Data using the filter() function

# Sample data
sample_1 = [1, 2, 5, 4, 3]
sample_2 = {1: 'junior', 2: 'mid', 5: 'd', 4: 'senior', 3: 'e'}

# Reverse junior list
iterator = reversed(sample_1)
print(list(iterator))

# Reverse junior dictionary
iterator = reversed(sample_2.items())
print(list(iterator))
