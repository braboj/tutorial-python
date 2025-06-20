# Bitwise Operators in Python
# ------------------------------------------------------------------------------
# Bitwise operators are used to perform bit-level operations on integers. These
# operators directly manipulate the binary representations of numbers. Each bit
# is calculated independently, based on the truth table of the operation.
#
# Truth table: & (AND)
# | A | B | A & B |
# |---|---|-------|
# | 0 | 0 |   0   |
# | 0 | 1 |   0   |
# | 1 | 0 |   0   |
# | 1 | 1 |   1   |

# Example:
#   0xAA  = 10101010 (binary)
#   0x55  = 01010101 (binary)
#   0xAA & 0x55 = 00000000 (binary)

# Initialize variables
a, b = 0xAA, 0x55

# Performs a binary AND operation between corresponding bits of a and b
print(hex(a & b))
# 0x00

# Performs a binary OR operation between corresponding bits of a and b
print(hex(a | b))
# 0xFF

# Performs a binary XOR operation between corresponding bits of a and b
print(hex(a ^ b))
# 0xFF

# Inverts all the bits of a (1's complement)
print(hex(~a))
# -0xAB

# Shifts the bits the left by 1 position, filling with 0 on the right
print(hex(a << 1))
# 0x154

# Shifts the bits the right by 1 position, discarding bits on the right
print(hex(a >> 1))
# 0x55
