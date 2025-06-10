# Example: OrderedDict

from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict()

# Add elements
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

# Print the OrderedDict
print(od)

# Move 'c' to the end
od.move_to_end('c')

# Print the OrderedDict
print(od)

# Move 'c' to the start
od.move_to_end('c', last=False)

# Print the OrderedDict
print(od)
