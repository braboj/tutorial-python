from decimal import Decimal

# for integers
print(round(10))

# for floating point
print(round(10.7))

# even choice
print(round(5.5))

# normal float
num = 2.675
print(round(num, 2))

# using decimal.Decimal (passed float as string for precision)
num = Decimal('2.675')
print(round(num, 2))