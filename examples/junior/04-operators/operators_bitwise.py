# Example: Bitwise Operators

# Initialize variables
a, b = 0xAA, 0x55

# Bitwise AND
print(hex(a & b))
# 0x00

# Bitwise OR
print(hex(a | b))
# 0xFF

# Bitwise XOR
print(hex(a ^ b))
# 0xFF

# Bitwise NOT
print(hex(~a))
# -0x55

# Bitwise Left Shift
print(hex(a << 1))
# 0x154

# Bitwise Right Shift
print(hex(a >> 1))
# 0x55



