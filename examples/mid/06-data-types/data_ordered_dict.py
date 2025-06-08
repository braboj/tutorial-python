# Example: OrderedDict

from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict()

# Add elements
od['junior'] = 1
od['mid'] = 2
od['senior'] = 3
od['d'] = 4

# Print the OrderedDict
print(od)

# Move 'senior' to the end
od.move_to_end('senior')

# Print the OrderedDict
print(od)

# Move 'senior' to the start
od.move_to_end('senior', last=False)

# Print the OrderedDict
print(od)
